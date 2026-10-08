import sys
import warnings
from pathlib import Path
import pandas as pd

warnings.filterwarnings("ignore", category=UserWarning)  # hide date-format guess warnings

# Folder with the raw files. Optional: pass another folder as an argument.
RAW = Path(sys.argv[1]) if len(sys.argv) > 1 else Path("data/raw")


def make_hashable(df):
    """Nested values (dicts/lists) can't be counted by pandas.
    This returns a COPY where they are turned into text. The original is untouched."""
    out = df.copy()
    for col in out.columns:
        if out[col].map(lambda v: isinstance(v, (dict, list))).any():
            out[col] = out[col].astype(str)
    return out


def find_date_columns(df):
    """Treat a text column as date-like only if >=80% of its non-null values parse as dates."""
    date_cols = []
    for col in df.columns:
        if pd.api.types.is_datetime64_any_dtype(df[col]):
            date_cols.append(col)
        elif pd.api.types.is_string_dtype(df[col]) or df[col].dtype == "object":
            sample = df[col].dropna().astype(str)
            if sample.empty:
                continue
            parsed = pd.to_datetime(sample, errors="coerce", utc=True)
            if parsed.notna().mean() >= 0.8:
                date_cols.append(col)
    return date_cols


def profile(name, path, df):
    safe = make_hashable(df)
    size = path.stat().st_size

    print(f"\n{'=' * 60}\n{name}\n{'=' * 60}")
    print(f"File size : {size} bytes ({size / 1024:.2f} KB)")
    print(f"Shape     : {df.shape[0]} rows x {df.shape[1]} columns")
    print(f"Columns   : {list(df.columns)}")

    print("\nData types:")
    print(df.dtypes.to_string())

    print("\nMissing (null) values per column:")
    print(df.isnull().sum().to_string())

    print(f"\nFully duplicated rows: {safe.duplicated().sum()}")

    print("\nDistinct values per column:")
    print(safe.nunique().to_string())

    print("\nFirst 5 records:")
    print(df.head().to_string())

    numeric = df.select_dtypes(include="number")
    if not numeric.empty:
        print("\nNumeric columns - min / max:")
        print(numeric.agg(["min", "max"]).T.to_string())

    date_cols = find_date_columns(df)
    if date_cols:
        print("\nDate/time columns - earliest / latest:")
        for col in date_cols:
            parsed = pd.to_datetime(df[col], errors="coerce", utc=True)
            bad = parsed.isna().sum() - df[col].isna().sum()
            print(f"  {col}: earliest={parsed.min()}  latest={parsed.max()}  "
                  f"(unparseable values: {bad})")
    else:
        print("\nNo date/time columns detected.")


def main():
    sources = {
        "customers.csv": pd.read_csv,
        "orders.json": pd.read_json,
        "products.parquet": pd.read_parquet,
    }
    for filename, reader in sources.items():
        path = RAW / filename
        if not path.exists():
            print(f"\n[ERROR] {path} not found. Check the path.")
            continue
        profile(filename, path, reader(path))


if __name__ == "__main__":
    main()