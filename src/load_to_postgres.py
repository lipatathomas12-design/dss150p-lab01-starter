import os
import pandas as pd
from sqlalchemy import create_engine

# PostgreSQL connection string from your docker-compose environment
# Format: postgresql://user:password@host:port/dbname
DB_USER = os.getenv("DB_USER", "postgres")
DB_PASSWORD = os.getenv("DB_PASSWORD", "postgres")
DB_HOST = os.getenv("DB_HOST", "localhost")
DB_PORT = os.getenv("DB_PORT", "5432")
DB_NAME = os.getenv("DB_NAME", "dss150p_db")

DATABASE_URL = f"postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"

def load_data():
    print("Connecting to PostgreSQL...")
    engine = create_engine(DATABASE_URL)

    # 1. Load Customers CSV
    print("Loading customers.csv...")
    customers_df = pd.read_csv("data/customers.csv")
    # Clean duplicates identified in profiling
    customers_df = customers_df.drop_duplicates()
    customers_df.to_sql("dim_customers", engine, if_exists="replace", index=False)
    print(f"Loaded {len(customers_df)} rows into dim_customers.")

    # 2. Load Products Parquet
    print("Loading products.parquet...")
    products_df = pd.read_parquet("data/products.parquet")
    products_df.to_sql("dim_products", engine, if_exists="replace", index=False)
    print(f"Loaded {len(products_df)} rows into dim_products.")

    # 3. Load Orders JSON (handle flattened shipping or raw json)
    print("Loading orders.json...")
    orders_df = pd.read_json("data/orders.json")
    # Convert nested shipping dict to string for database compatibility if needed
    orders_df["shipping"] = orders_df["shipping"].astype(str)
    orders_df.to_sql("fact_orders", engine, if_exists="replace", index=False)
    print(f"Loaded {len(orders_df)} rows into fact_orders.")

    print("\nAll data successfully loaded into PostgreSQL!")

if __name__ == "__main__":
    load_data()