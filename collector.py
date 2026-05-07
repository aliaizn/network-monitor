import os
import socket
import time
from datetime import datetime

import psycopg2

# Database connection (from environment with fallback)
DB_HOST = os.environ.get("DB_HOST", "localhost")
DB_NAME = os.environ.get("DB_NAME", "monitoring")
DB_USER = os.environ.get("DB_USER", "postgres")
DB_PASS = os.environ.get("DB_PASS", "devpass")

# Which port to check for each device type
PORT_MAP = {
    'host': 5000,    # Our Flask app
    'router': 443,
    'dns': 53,
    'generic': 443,
}

def get_devices():
    """Return all devices from the database."""
    conn = psycopg2.connect(host=DB_HOST, dbname=DB_NAME,
                            user=DB_USER, password=DB_PASS)
    cur = conn.cursor()
    cur.execute("SELECT id, name, ip_address, device_type FROM devices")
    devices = [(row[0], row[1], str(row[2]), row[3]) for row in cur.fetchall()]
    cur.close()
    conn.close()
    return devices

def check_tcp(ip_address, port, timeout=2):
    """Try to establish a TCP connection. Return (status, latency_ms)."""
    start = time.time()
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(timeout)
    try:
        result = sock.connect_ex((ip_address, port))
        latency = (time.time() - start) * 1000
        if result == 0:
            return True, round(latency, 2)
        else:
            return False, None
    except Exception:
        return False, None
    finally:
        sock.close()

def store_check(device_id, status, latency_ms):
    """Insert a check record into the pings table."""
    conn = psycopg2.connect(host=DB_HOST, dbname=DB_NAME,
                            user=DB_USER, password=DB_PASS)
    cur = conn.cursor()
    cur.execute(
        "INSERT INTO pings (device_id, status, latency_ms, pinged_at) "
        "VALUES (%s, %s, %s, %s)",
        (device_id, status, latency_ms, datetime.utcnow())
    )
    conn.commit()
    cur.close()
    conn.close()

def main():
    print("Collecting checks...")
    devices = get_devices()
    if not devices:
        print("No devices found. Add some to the database first.")
        return
    for dev_id, name, ip, dtype in devices:
        port = PORT_MAP.get(dtype, 80)
        status, latency = check_tcp(ip, port)
        store_check(dev_id, status, latency)
        print(f"{name} ({ip}:{port}): {'UP' if status else 'DOWN'}"
              + (f" - {latency} ms" if latency else ""))

if __name__ == "__main__":
    main()
