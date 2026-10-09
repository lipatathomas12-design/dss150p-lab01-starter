| Field / Property | CSV Source | JSON Source | Parquet Source | REST API Source | PostgreSQL Source |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **Source name** | `customers.csv` | `orders.json` | `products.parquet` | `jsonplaceholder.typicode.com/posts` | `support_tickets` (PostgreSQL sample table) |
| **Source-system type** | Flat file / local storage | Semi-structured file | Columnar binary file | Web service / HTTP endpoint | Relational database |
| **Data format** | CSV | JSON | Parquet | JSON | SQL table |
| **Structured / semi-structured / unstructured** | Structured | Semi-structured | Structured | Semi-structured | Structured |
| **Expected update pattern** | Static / batch drop | Periodic batch | Periodic batch | On demand | Transactional / continuous |
| **Likely acquisition method** | Local file read (pandas) | Local file read (pandas) | Local file read (pandas + pyarrow) | HTTP GET (`requests`) | SQL query via SQLAlchemy |
| **Schema location or owner** | Inferred from the file header | Implicit, defined by the file itself | Embedded in the file metadata | API response structure | Database catalog (`information_schema`) and `sql/seed_support_tickets.sql` |
| **Possible primary / business key** | `customer_id` | `order_id` | `product_id` | `id` | `ticket_id` |
| **Potential schema-evolution risk** | Column order changes, missing headers | Nested fields added or changed | Column types changed, columns added or dropped | Changed JSON payload structure | DDL changes, columns dropped or retyped |
| **Potential data-quality risk** | Missing values, duplicate and conflicting IDs | Orphan `customer_id` values, nested `shipping` object | Corrupt file, version mismatch | Timeouts, 5xx errors, rate limiting, placeholder data | Unassigned tickets, NULL `resolved_at`, no time zone on timestamps |

**REST API retrieval timestamp (UTC):** 2026-10-08T16:34:58.811657+00:00

Endpoint: https://jsonplaceholder.typicode.com/posts (HTTP 200, application/json; charset=utf-8)
