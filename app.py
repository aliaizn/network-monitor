from flask import Flask, request, jsonify
import psycopg2
import psycopg2.extras  # for dict-like rows

app = Flask(__name__)

#Database configuration (same as collector)
DB_HOST = "localhost"
DB_NAME = "monitoring"
DB_USER = "postgres"
DB_PASS = "devpass"

def get_db_connection():
    """Return a database connection and configuration row factory."""
    conn = psycopg2.connect(
        host=DB_HOST,
        dbname=DB_NAME,
        user=DB_USER,
        password=DB_PASS
    )
    #This makes rows behave like dictionaries (column: value)
    conn.cursor_factory = psycopg2.extras.RealDictCursor
    return conn

@app.route('/devices', methods=['GET', 'POST'])
def devices():
    conn = get_db_connection()
    cur = conn.cursor()
    if request.method == 'GET':
        cur.execute("SELECT * FROM devices ORDER BY id")
        rows = cur.fetchall()
        cur.close()
        conn.close()
        return jsonify(rows)
    else: # POST - add a new device
        data = request.get_json()
        name = data['name']
        ip = data['ip_address']
        dtype = data.get('device_type', 'generic')
        cur.execute(
            "INSERT INTO devices (name, ip_address, device_type) VALUES (%s, %s, %s) RETURNING id", (name, ip, dtype)
        )
        new_id = cur.fetchone()['id']
        conn.commit()
        cur.close()
        conn.close()
        return jsonify({'id': new_id, 'message': 'Device added'}), 201

@app.route('/devices/<int:device_id>/pings', methods=['GET'])
def pings_for_device(device_id):
    conn = get_db_connection()
    cur = conn.cursor()
    # Last 100 pings for this device
    cur.execute(
        "SELECT status, latency_ms, pinged_at FROM pings "
        "WHERE device_id = %s ORDER BY pinged_at DESC LIMIT 100",
        (device_id,)
    )
    rows = cur.fetchall()
    cur.close()
    conn.close()
    return jsonify(rows)

@app.route('/pings', methods=['GET'])
def all_recent_pings():
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute(
        "SELECT d.name, d.ip_address, p.status, p.latency_ms, p.pinged_at "
        "FROM pings p JOIN devices d ON p.device_id = d.id "
        "ORDER BY p.pinged_at DESC LIMIT 100"
    )
    rows = cur.fetchall()
    cur.close()
    conn.close()
    return jsonify(rows)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)


