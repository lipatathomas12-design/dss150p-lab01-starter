
| Field / Property | CSV Source | JSON Source | Parquet Source | REST API Source | PostgreSQL Source |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **Source name** | `customers.csv` | `orders.json`[cite: 1] | `products.parquet`[cite: 1] | REST API Endpoint[cite: 1] | PostgreSQL Sample Table[cite: 1] |
| **Source-system Type** | Flat File / Local Storage | Semi-structured File | Columnar Binary File | Web Service / HTTP Endpoint | Relational Database |
| **Data format** | CSV[cite: 1] | JSON[cite: 1] | Parquet[cite: 1] | JSON[cite: 1] | SQL Table |
| **Structured / Semi-structured / Unstructured** | Structured | Semi-structured | Structured | Semi-structured | Structured |
| **Expected update pattern** | Static / Batch drop | Periodic batch | Periodic batch | Real-time / On-demand | Transactional / Continuous |
| **Likely acquisition method** | Local file read (Pandas) | Local file read (Pandas) | Local file read (PyArrow) | HTTP GET (`requests`)[cite: 1] | SQL SQLAlchemy connection |
| **Schema location or owner** | Inferred from file header | Implicit / Documented | Embedded in file metadata | API response schema | Database catalog (`information_schema`) |
| **Possible primary business key** | Customer ID | Order ID | Product ID | Record ID / Identifier | Primary Key constraint |
| **Potential schema-evolution risk** | Column order shifts, missing headers | Nested array changes, extra fields | Type changes, added/dropped columns | Changing JSON payload structure | DDL changes, column drops |
| **Potential data-quality risk** | Null values, formatting inconsistencies | Malformed JSON, missing attributes | Corruption, binary version mismatch | Timeouts, 5xx server errors, rate limiting[cite: 1] | Constraint violations, stale data |

*Note: Retrieval timestamp for the REST API snapshot will be recorded here once pulled.*