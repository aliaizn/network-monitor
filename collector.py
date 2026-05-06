import subprocess
import psycopg2
from datetime import datetime

# Database connection
DB_HOST = "localhost"
DB_NAME = "monitoring"
DB_USER = "postgres"
DB_PASS = "devpass"

def get_devices():
    """Retrun all devices from the database."""
    conn = psycopg2.connect(host=DB_HOST, dbname=DB_NAME,
                           user=DB_USER, password=DB_PASS)
    cur = conn.cursor()
    cur.execute("SELECT id, name, ip_address FROM devices")
    devices = [(row[0], row[1], str(row[2])) for row in cur.fetchall()]
    cur.close()
    conn.close()
    return devices

def ping_device(ip_address):
    """Ping an IP address, return (status, latency_ms)."""
    try:
        result = subprocess.run(
            ["ping", "-c", "2", ip_address],
            capture_output=True, text=True, timeout=5
        )
        if result.returncode == 0:
            # Extract latency from 'rtt min/avg/max/mdev = 12,345/...'
            parts = result.stdout.split("rtt min/avg/max/mdev = ")
            if len(parts) > 1:
                avg = parts[1].split("/")[1]
                return True, float(avg)
            return True, None
        return False, None
    except subprocess.TimeoutExpired:
        return False, None
    except Exception:
        return False, None

def store_ping(device_id, status, latency_ms):
    """Insert a ping record into the database"""
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
    print("Collecting pings...")
    devices = get_devices()
    if not devices:
        print("No devices found. Add some to the database first.")
        return
    for device_id, name, ip in devices:
        status, latency = ping_device(ip)
        store_ping(device_id, status, latency)
        print(f"{name} ({ip}): {'UP' if status else 'DOWN'}"
              +(f" - {latency:.2f} ms" if latency else ""))

if __name__ == "__main__":
    main()
