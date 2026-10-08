# Data Contracts & Schema Validation Rules

## 1. Customers Data Contract (`customers.csv`)
* **Target Source:** `data/customers.csv`
* **Schema Definition:**
  * `customer_id`: `string` (Not Null, Unique Primary Key)[cite: 1]
  * `first_name`: `string` (Not Null)[cite: 1]
  * `last_name`: `string` (Not Null)[cite: 1]
  * `email`: `string` (Nullable - threshold: max 5% missing allowed)[cite: 1]
  * `city`: `string` (Nullable - threshold: max 5% missing allowed)[cite: 1]
  * `signup_date`: `string` / `date` (Not Null, ISO format `YYYY-MM-DD`)[cite: 1]
  * `customer_segment`: `string` (Not Null, Enum: ['Professional', 'Retail', 'SME', 'Student'])[cite: 1]
* **SLA & Quality Constraints:**
  * Zero tolerance for duplicate `customer_id` values[cite: 1].
  * Maximum acceptable row duplication rate: < 1% (must purge the 2 duplicate rows identified in profiling)[cite: 1].

## 2. Orders Data Contract (`orders.json`)
* **Target Source:** `data/orders.json`[cite: 1]
* **Schema Definition:**
  * `order_id`: `string` (Not Null, Unique Primary Key)[cite: 1]
  * `customer_id`: `string` (Not Null, Foreign Key to customers)[cite: 1]
  * `order_timestamp`: `string` / `datetime` (Not Null)[cite: 1]
  * `status`: `string` (Not Null, Enum: ['Packed', 'Delivered', 'Cancelled', 'Pending', ...])[cite: 1]
  * `item_count`: `integer` (Not Null, Min: 1, Max: 10)[cite: 1]
  * `subtotal`: `float` (Not Null, Min: > 0)[cite: 1]
  * `shipping_fee`: `integer` or `float` (Not Null, Min: 0)[cite: 1]
  * `total_amount`: `float` (Not Null, Equals `subtotal + shipping_fee`)[cite: 1]
  * `shipping`: `object` / `dict` (Not Null, must contain nested keys `region` and `method`)[cite: 1]
* **SLA & Quality Constraints:**
  * Schema evolution policy: Upstream additions of nested keys inside `shipping` are permitted, but `region` and `method` must remain present[cite: 1].

## 3. Products Data Contract (`products.parquet`)
* **Target Source:** `data/products.parquet`[cite: 1]
* **Schema Definition:**
  * `product_id`: `string` (Not Null, Unique Primary Key)[cite: 1]
  * `product_name`: `string` (Not Null)[cite: 1]
  * `category`: `string` (Not Null)[cite: 1]
  * `brand`: `string` (Not Null)[cite: 1]
  * `unit_price`: `float` (Not Null, Min > 0)[cite: 1]
  * `stock_quantity`: `integer` (Not Null, Min >= 0)[cite: 1]
  * `weight_kg`: `float` (Not Null, Min > 0)[cite: 1]
* **SLA & Quality Constraints:**
  * Zero missing values allowed across all mandatory fields[cite: 1].
  * Binary file format integrity enforced via PyArrow/Pandas engine execution[cite: 1].