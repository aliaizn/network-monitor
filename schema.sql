-- schema.sql
-- Netwok Monitoring Dashboard



CREATE TABLE devices (
       id SERIAL PRIMARY KEY,
       name VARCHAR(100) NOT NULL,
       ip_address INET NOT NULL,
       device_type VARCHAR(100) DEFAULT 'generic',
       created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);


CREATE TABLE pings (
       id SERIAL PRIMARY KEY,
       device_id INTEGER NOT NULL,
       status BOOLEAN NOT NULL,
       latency_ms REAL,
       pinged_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
       FOREIGN KEY (device_id) REFERENCES devices(id) ON DELETE CASCADE
);


CREATE INDEX idx_pings_device_time ON pings (device_id, pinged_at);
