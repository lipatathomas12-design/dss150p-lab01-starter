import os
import json
import pandas as pd

def profile_file(file_path, file_type="csv"):
    print(f"\n==========================================")
    print(f"PROFILING: {file_path}")
    print(f"==========================================")
    
    if not os.path.exists(file_path):
        print(f"Error: File not found at {file_path}")
        return

    size_bytes = os.path.getsize(file_path)
    size_kb = size_bytes / 1024
    print(f"File Size: {size_bytes} bytes ({size_kb:.2f} KB)")

    try:
        if file_type == "csv":
            df = pd.read_csv(file_path)
        elif file_type == "json":
            # Read JSON safely (handles standard record/orient JSONs)
            df = pd.read_json(file_path)
        elif file_type == "parquet":
            df = pd.read_parquet(file_path)
        else:
            print("Unsupported format.")
            return
    except Exception as e:
        print(f"Failed to read file: {e}")
        return

    rows, cols = df.shape
    print(f"Rows: {rows} | Columns: {cols}")
    print(f"Columns: {list(df.columns)}")

    print("\n--- Column Details (Type & Nulls) ---")
    for col in df.columns:
        null_count = df[col].isnull().sum()
        dtype = df[col].dtype
        print(f"  - {col}: type = {dtype}, missing values = {null_count}")

   
    try:
        temp_df = df.copy()
        for col in temp_df.columns:
            if temp_df[col].apply(lambda x: isinstance(x, (dict, list))).any():
                temp_df[col] = temp_df[col].astype(str)
        duplicates = temp_df.duplicated().sum()
        print(f"\nFully Duplicated Rows: {duplicates}")
    except Exception as e:
        print(f"\nFully Duplicated Rows: Could not calculate ({e})")

    print("\n--- Distinct Values Count ---")
    for col in df.columns:
        try:
            if df[col].nunique() < 50:
                print(f"  - {col}: {df[col].nunique()} distinct values")
        except:
            pass

    print("\n--- First 5 Records ---")
    print(df.head())

    print("\n--- Numeric Columns Summary (Min / Max) ---")
    numeric_cols = df.select_dtypes(include=["number"]).columns
    if len(numeric_cols) > 0:
        for col in numeric_cols:
            print(f"  - {col}: min = {df[col].min()}, max = {df[col].max()}")
    else:
        print("  No numeric columns found.")

if __name__ == "__main__":
    profile_file("data/customers.csv", "csv")
    profile_file("data/orders.json", "json")
    profile_file("data/products.parquet", "parquet")