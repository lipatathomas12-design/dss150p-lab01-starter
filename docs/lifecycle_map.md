| Lifecycle Element | What It Means | Example in This Lab | Primary Tool/Artifact | Possible Failure |
| :--- | :--- | :--- | :--- | :--- |
| **Source system** | Where data is created or captured | `customers.csv`, `orders.json`, `products.parquet`, the REST API, PostgreSQL | File system, external API, database | Missing files, API timeouts, schema drift |
| **Ingestion/acquisition** | Pulling data from each source into the pipeline | Reading the CSV, JSON and Parquet files, an HTTP GET to the REST API, a SQL query to PostgreSQL | pandas, requests, SQLAlchemy | Missing files, API timeouts, connection refused, wrong paths |
| **Storage** | Where raw or processed data is kept | Local folder `data/raw/`, PostgreSQL database `dss150p_lab` | Docker volume, PostgreSQL, local disk | Disk space limits, connection refused |
| **Processing/transformation** | Cleaning, parsing and reshaping data | `src/profile_sources.py`, flattening the nested `shipping` JSON | Python, pandas | Type conversion errors, out-of-memory errors |
| **Data quality/validation** | Checking constraints, nulls, formats and business rules | Data contract rules in `docs/data_contract.yaml`, `CHECK` constraints in `sql/01_create_schema.sql` | YAML, SQL constraints | Unhandled nulls, duplicate keys, values outside allowed ranges |
| **Delivery** | Moving data or schemas to the target for use | Creating the `lab.customers` table with `sql/01_create_schema.sql` | PostgreSQL, SQL scripts | Constraint violations during insertion |
| **Consumer** | Who uses the data | Downstream analysts, reporting teams, applications | BI tools, Python apps | Misread schemas, bad data leading to wrong reports |


```text
[ CSV Source ]      ----+
[ JSON Source ]     ----+
[ Parquet Source ]  ----+--->  [ Pipeline Process ]  --->  [ Storage / Destination ]  --->  [ Downstream Analyst ]
[ REST API ]        ----+      (Python / pandas)           (PostgreSQL database)             (Application consumer)
[ PostgreSQL ]      ----+
```