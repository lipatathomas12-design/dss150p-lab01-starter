# DSS150P Laboratory Activity #1: Data Engineering Lifecycle Workspace

**Name:** [Thomas Walter Lipata]
**Student Number:** [2024109933]
**Section:** [CM17]

## Purpose
Set up a reproducible local data-engineering workspace (Python, Git, Docker, PostgreSQL),
profile five source types (CSV, JSON, Parquet, REST API, PostgreSQL), and create a basic
schema and data contract for one source (customers.csv).

## Software Requirements
- Python 3.x
- Git
- Docker Desktop with Docker Compose
- Visual Studio Code (or any code editor)
- Internet access only for the REST API and package installation

## How to Reproduce (Windows PowerShell, run from the repository root)
1. Create and activate the virtual environment, then install packages:
2. Start PostgreSQL and confirm it is running:
3. Run the scripts (see below).
4. Load the instructor's sample table and apply the schema:

## Start and Stop PostgreSQL
- Start: `docker compose up -d`
- Stop (data kept): `docker compose down`
- Stop and delete the database volume: `docker compose down -v`

## How to Run Each Script
- `python src/verify_environment.py` connects to PostgreSQL and prints its version and database name.
- `python src/profile_sources.py` profiles customers.csv, orders.json and products.parquet in `data/raw/`.
- `python src/inspect_api.py` calls the REST API (https://jsonplaceholder.typicode.com/posts) and saves the response to `data/raw/api_snapshot.json`.

## Sources
- **customers.csv:** 250 rows, 7 columns. Has duplicate and conflicting customer_id values and a few missing emails and cities.
- **orders.json:** 250 rows, 9 columns. Has a nested `shipping` object and 5 orders whose customer_id is not in customers.csv.
- **products.parquet:** 200 rows, 7 columns. Clean, typed, and unique product_id.
- **REST API:** jsonplaceholder /posts, 100 flat placeholder records. They cannot be joined to the other sources.
- **PostgreSQL:** table `support_tickets`, 250 rows, 8 columns, primary key `ticket_id`.

## Known Limitations / Unresolved Questions
- The owner and update schedule of each source are unknown and need source owner confirmation.
- customer_id is not unique in customers.csv (C0090 is a conflicting duplicate), so the CSV cannot be loaded into lab.customers until it is cleaned.
- Timestamps in orders.json and support_tickets have no time zone.
- The REST API returns generic placeholder data, not business data.
- No data was bulk-loaded into the lab.customers table, as instructed.

## AI Usage
I used Claude (Anthropic) to help draft the profiling, API and schema scripts, the
data contract, and to explain error messages. I ran every script myself, checked the
output against the real data files, and changed the wording of the documents. [Edit this
paragraph so it says exactly what you did. You must be able to explain every line of code.]
I also Used Google gemini to start up my project.