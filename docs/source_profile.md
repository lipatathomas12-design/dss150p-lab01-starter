# Source Profile Interpretation

## 1. customers.csv
- **Size/shape:** 250 rows x 7 columns (about 17.5 KB). All columns are read as text.
- **Duplicate risk:** 2 rows are exact copies (C0036 and C0145 each appear twice).
  Also, `customer_id` has only 247 distinct values, so the key is not unique yet.
- **Conflicting key:** C0090 appears twice with different people (Paolo Aquino vs
  Hannah Reyes). Dropping exact duplicates will not fix this one, so a
  pipeline needs a rule or the source owner's confirmation.
- **Nullability:** `email` has 3 missing values and `city` has 2. Other columns are complete.
- **Date handling:** `signup_date` is stored as text (YYYY-MM-DD). It parses cleanly,
  ranging from 2025-01-04 to 2026-05-16. It should be converted to a DATE type.

## 2. orders.json
- **Size/shape:** 250 rows x 9 columns (about 76 KB). No nulls and no duplicate rows.
- **Nested structure:** `shipping` is a nested object with `region` and `method`.
  It must be flattened before loading into a relational table.
- **Key and relationships:** `order_id` is unique (250 distinct) and works as the
  primary key. `customer_id` has 159 distinct values, and 5 orders point to a
  customer_id that does not exist in customers.csv (orphan records).
- **Date representation:** `order_timestamp` is text in ISO format with no time zone,
  ranging from 2026-01-02 to 2026-06-30. The time zone should be confirmed with the owner.
- **Consistency:** `total_amount` equals `subtotal + shipping_fee` on every row.
  This is a good quality rule to enforce.

## 3. products.parquet
- **Size/shape:** 200 rows x 7 columns (about 14 KB). No nulls and no duplicates.
- **Key:** `product_id` is unique (200 distinct), so it is a safe primary key.
- **Types:** Types are stored in the file (float64, int32), so there is less type
  ambiguity than the CSV or JSON. `stock_quantity` ranges from 0 to 250 and `unit_price`
  from 392.85 to 84,796.84.
- **Low-cardinality fields:** `category` and `brand` have 6 values each, which suits
  validation against an allowed list.

  ## 4. REST API (jsonplaceholder.typicode.com/posts)
- **Structure:** The top level is a list of 100 flat records, each with `userId`, `id`,
  `title` and `body`. The raw response is saved unchanged in data/raw/api_snapshot.json.
- **Key:** `id` looks like the business key (1 to 100). Uniqueness should be
  checked before relying on it.
- **Content mismatch:** These are generic placeholder posts, not orders or customers.
  The `userId` does not link to `customer_id` in customers.csv, so this source
  cannot be joined to the other files.
- **Text risk:** `body` contains embedded newline characters (`\n`), which can
  break naive CSV exports or line-based processing.
- **Stability risk:** This is a public third-party service with no schema guarantee
  or SLA, so it could change or be unavailable.