* Network Monitoring Dashboard

  A containerised, full‑stack web application that continuously checks the
  availability of network endpoints via TCP health checks and displays the
  results on a live dashboard.

  Built entirely from within Iran, where international connectivity is
  heavily restricted. The project demonstrates the ability to design,
  containerise, and debug a multi‑service application under real‑world
  constraints — including blocked registries, unavailable package mirrors,
  and layer‑3/layer‑4 censorship.

** Why this project
   - Shows end‑to‑end system design: backend API, persistent database,
     health‑check collector, and frontend dashboard.
   - Uses TCP sockets instead of ICMP ping, avoiding Docker privilege
     requirements and blocked protocols.
   - Developed and tested inside a censored network; the dashboard
     intentionally monitors both domestic and international endpoints,
     making state‑imposed blockages visible.
   - Fully containerised: a single ~docker compose up~ command starts the
     entire stack.

** Features
   - TCP health checks for any IP:port, configurable by device type.
   - PostgreSQL database with automatic schema initialisation.
   - RESTful JSON API:
     - ~GET /devices~ — all devices
     - ~POST /devices~ — add a new device
     - ~GET /devices/<id>/pings~ — pings for a specific device
     - ~GET /pings~ — last 100 pings
   - Clean HTML dashboard with auto‑refresh (every 30 seconds).
   - Automatic continuous monitoring (collector runs every 60 seconds
     inside the container).

** Technology Stack
   - Python 3.10 + Flask (backend & API)
   - PostgreSQL 16 (data storage)
   - psycopg2 (database driver)
   - Docker & Docker Compose (container orchestration)
   - Vanilla HTML / JavaScript (frontend)
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
      #+begin_src shell
      git clone https://github.com/aliaizn/network-monitor.git
      cd network-monitor
      #+end_src
   3. Start the application:
      #+begin_src shell
      docker compose up --build
      #+end_src
   4. Open ~http://localhost:5000~ in your browser.
   5. Add a device via the API (example):
      #+begin_src shell
      curl -X POST http://localhost:5000/devices \
        -H "Content-Type: application/json" \
        -d '{"name":"Localhost","ip_address":"127.0.0.1","device_type":"host"}'
      #+end_src
   6. The collector runs automatically inside the container every minute.

** Network Context
   This project was developed from within Iran, where international
   connectivity is often restricted. The dashboard intentionally monitors
   both domestic and international endpoints, illustrating how TCP checks
   can reveal blocked paths even when ICMP ping is unavailable.  The tool
   serves as a practical example of infrastructure‑aware monitoring under
   real‑world constraints.

** Author
   [Ali Aizn] – Developer
   GitHub: https://github.com/aliaizn
