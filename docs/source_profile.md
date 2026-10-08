# Source Metadata Profiles & Interpretations

## 1. Customers Dataset (`customers.csv`)
* **Dimensions:** 250 rows, 7 columns.
* **Data Quality Issues:** 
  * Missing values found in `email` (3 missing) and `city` (2 missing).
  * 2 fully duplicated rows detected.
* **Keys & Identifiers:** `customer_id` serves as the primary key (no nulls).
* **Actionable Insight:** These duplicates and nulls must be cleaned during the data ingestion pipeline phase.

## 2. Orders Dataset (`orders.json`)
* **Dimensions:** 250 rows, 9 columns.
* **Data Quality Issues:** Zero missing values across all standard fields. No row duplicates.
* **Structural Characteristics:** Contains a nested dictionary column (`shipping`) holding nested keys like `region` and `method`.
* **Keys & Identifiers:** `order_id` acts as the primary key; `customer_id` acts as the foreign key referencing customers.
* **Actionable Insight:** The `shipping` JSON object needs to be unpacked/flattened before writing into a traditional relational database table like PostgreSQL.

## 3. Products Dataset (`products.parquet`)
* **Dimensions:** 200 rows, 7 columns.
* **Data Quality Issues:** Pristine data quality with zero missing values and zero duplicates.
* **Data Types:** High-efficiency binary columnar storage format with correct data types (`float64`, `int32`).
* **Keys & Identifiers:** `product_id` serves as the primary key.
* **Actionable Insight:** Ready for direct ingestion into downstream storage layers without heavy structural transformation.