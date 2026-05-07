* Network Monitoring Dashboard
  A containerised, full‑stack web application that continuously checks
  the availability of network endpoints via TCP health checks and
  displays the results on a live dashboard.

  Built with a focus on infrastructure awareness in restricted
  network environments.

** Live Demo
   (Insert your Render URL after deployment)
   [[http://localhost:5000][Local development]]

** Features
   - TCP health checks for any IP:port (no ICMP dependency, works in Docker)
   - Supports multiple device types with custom port mappings
   - PostgreSQL database with automatic schema initialisation
   - RESTful JSON API:
     - GET /devices — all devices
     - POST /devices — add a new device
     - GET /devices/<id>/pings — pings for a specific device
     - GET /pings — last 100 pings
   - Clean HTML dashboard with auto‑refresh (every 30 seconds)
   - Automatic continuous monitoring (collector runs every 60 seconds)
   - Fully containerised with Docker Compose (one command to start)

** Technology Stack
   - Python 3.10 + Flask (backend & API)
   - PostgreSQL 16 (data storage)
   - psycopg2 (database driver)
   - Docker & Docker Compose (container orchestration)
   - Vanilla HTML/JavaScript (frontend)
   - TCP socket connectivity (health checks)

** Project Structure
   #+begin_example
   .
   ├── Dockerfile
   ├── docker-compose.yml
   ├── requirements.txt
   ├── app.py
   ├── collector.py
   ├── schema.sql* Network Monitoring Dashboard
  A containerised, full‑stack web application that continuously checks
  the availability of network endpoints via TCP health checks and
  displays the results on a live dashboard.

  Built as a portfolio project for Junior DevOps / Backend roles,
  with a special focus on infrastructure awareness in restricted
  network environments.

** Live Demo
   (Insert your Render URL after deployment)
   [[http://localhost:5000][Local development]]

** Features
   - TCP health checks for any IP:port (no ICMP dependency, works in Docker)
   - Supports multiple device types with custom port mappings
   - PostgreSQL database with automatic schema initialisation
   - RESTful JSON API:
     - GET /devices — all devices
     - POST /devices — add a new device
     - GET /devices/<id>/pings — pings for a specific device
     - GET /pings — last 100 pings
   - Clean HTML dashboard with auto‑refresh (every 30 seconds)
   - Automatic continuous monitoring (collector runs every 60 seconds)
   - Fully containerised with Docker Compose (one command to start)

** Technology Stack
   - Python 3.10 + Flask (backend & API)
   - PostgreSQL 16 (data storage)
   - psycopg2 (database driver)
   - Docker & Docker Compose (container orchestration)
   - Vanilla HTML/JavaScript (frontend)
   - TCP socket connectivity (health checks)

** Project Structure
   #+begin_example
   .
   ├── Dockerfile
   ├── docker-compose.yml
   ├── requirements.txt
   ├── app.py
   ├── collector.py
   ├── schema.sql
   ├── index.html
   └── README.org
   #+end_example

** How to Run Locally
   1. Ensure Docker and Docker Compose are installed.
   2. Clone the repository:
      git clone https://github.com/aliaizn/network-monitor.git
      cd network-monitor
   3. Start the application:
      docker compose up --build
   4. Open http://localhost:5000
   5. Add a device via the API (example):
      curl -X POST http://localhost:5000/devices \
        -H "Content-Type: application/json" \
        -d '{"name":"Localhost","ip_address":"127.0.0.1","device_type":"host"}'
   6. The collector runs automatically inside the container every minute.

** Network Context
   This project was developed from within Iran, where international
   connectivity is often restricted. The dashboard intentionally
   monitors both domestic and international endpoints, illustrating
   how TCP checks can reveal blocked paths even when ICMP ping is
   unavailable.  The tool serves as a practical example of
   infrastructure‑aware monitoring under real‑world constraints.

** Author
   [Your Name] — aspiring Junior DevOps / Backend Engineer
   GitHub: https://github.com/aliaizn

** License
   MIT
   ├── index.html
   └── README.org
   #+end_example

** How to Run Locally
   1. Ensure Docker and Docker Compose are installed.
   2. Clone the repository:
      git clone https://github.com/aliaizn/network-monitor.git
      cd network-monitor
   3. Start the application:
      docker compose up --build
   4. Open http://localhost:5000
   5. Add a device via the API (example):
      curl -X POST http://localhost:5000/devices \
        -H "Content-Type: application/json" \
        -d '{"name":"Localhost","ip_address":"127.0.0.1","device_type":"host"}'
   6. The collector runs automatically inside the container every minute.

** Network Context
   This project was developed from within Iran, where international
   connectivity is often restricted. The dashboard intentionally
   monitors both domestic and international endpoints, illustrating
   how TCP checks can reveal blocked paths even when ICMP ping is
   unavailable.  The tool serves as a practical example of
   infrastructure‑aware monitoring under real‑world constraints.

** Author
   [Ali Aizn] — Developer
   GitHub: https://github.com/aliaizn

** License
   MIT
