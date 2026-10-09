CREATE SCHEMA IF NOT EXISTS lab;

CREATE TABLE IF NOT EXISTS lab.customers (
    -- Primary key: profiling found 247 distinct customer_id values in 250 rows
    -- (C0036 and C0145 are exact duplicates; C0090 appears with two different
    -- people). The raw file must be cleaned before loading, but customer_id is
    -- the only reliable business key, so it is defined as the primary key here.
    customer_id      TEXT PRIMARY KEY,
    first_name       TEXT NOT NULL,
    last_name        TEXT NOT NULL,
    email            TEXT,            -- nullable: 3 missing values in the source
    city             TEXT,            -- nullable: 2 missing values in the source
    signup_date      DATE NOT NULL,   -- stored as YYYY-MM-DD text in the CSV
    customer_segment TEXT NOT NULL,

    -- Segment must be one of the 4 values seen in the data
    CONSTRAINT ck_customers_segment
        CHECK (customer_segment IN ('Professional', 'Retail', 'SME', 'Student')),
    -- All IDs in the file look like C0001
    CONSTRAINT ck_customers_id_format
        CHECK (customer_id ~ '^C[0-9]{4}$')
);