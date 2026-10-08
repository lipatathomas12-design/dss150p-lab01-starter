## Lifecycle Table

| Lifecycle Element | What It Mean | Example in This Lab | Primary Tool/Asset | Possible Failures |
| :--- | :--- | :--- | :--- | :--- |
| **Source system** | Origin points where raw data is generated or captured | `customers.csv`, `orders.json`, `products.parquet`, REST API, PostgreSQL | File system, External API, Database | Missing files, API timeouts, schema drift |
| **Storage** | Persistence layers where raw or processed data lands | Local directories (`/data`), PostgreSQL database tables (`dss150_db`) | Docker volumes, PostgreSQL, Local disk | Disk space limits, connection refused errors |
| **Processing/Transformation** | Cleaning, parsing, restructuring, and reshaping data | Profiling scripts (`src/profile_sources.py`), JSON parsing | Python, Pandas, SQLAlchemy | Type conversion errors, `NameError`, out-of-memory errors |
| **Data quality/validation** | Checking constraints, nullability, formats, and business rules | Data contract rules (`docs/data_contract.yaml`), `CHECK` constraints | YAML, SQL constraints | Unhandled nulls, duplicate keys, violating domain ranges |
| **Delivery** | Moving data or schemas to targets or tables for consumption | Deploying schemas via SQL (`create_schema.sql`), loading database tables | PostgreSQL, SQL scripts | Constraint violations during insertion |
| **Consumer** | End users, dashboards, or applications that use the data | Downstream analysts, business reporting teams, applications | BI tools, Python apps, Data Analysts | Misinterpreted schemas, bad data leading to flawed analytics |

---

## Data Flow Diagram

```text
[ CSV Source ] ----+
                   |
[ JSON Source ] ---+---> [ Pipeline Process ] ---> [ Storage / Destination ] ---> [ Downstream Analyst ]
                   |      (Python / Pandas)         (PostgreSQL Database)          (Business Consumer)
[ Parquet Source ]-+
                   |
[ REST API ] ------+