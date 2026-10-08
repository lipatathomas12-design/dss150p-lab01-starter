import json
from datetime import datetime, timezone
from pathlib import Path

import requests

# TODO: paste the URL given by the instructor (in the README on the LMS)
API_URL = "https://jsonplaceholder.typicode.com/posts"

OUTPUT_FILE = Path("data/raw/api_snapshot.json")


def main():
    # Steps 1-2: send an HTTP GET request with a 10-30 second timeout
    try:
        response = requests.get(API_URL, timeout=20)
    except requests.exceptions.RequestException as e:
        # Per the troubleshooting guide: record the error, do NOT invent a response
        print(f"Request failed: {e}")
        raise SystemExit(1)

    # Step 3: fail clearly if the HTTP status code is not successful (4xx/5xx)
    response.raise_for_status()
    print("Status code :", response.status_code)

    # Step 4: print the Content-Type header
    print("Content-Type:", response.headers.get("Content-Type"))

    # Step 5: parse the JSON response
    payload = response.json()

    # Step 6: is the top level a list or an object/dictionary?
    print("Top-level type:", type(payload).__name__)

    # Step 7: print the number of records if the structure permits it
    if isinstance(payload, list):
        print("Number of records:", len(payload))
        sample = payload[0] if payload else None
    elif isinstance(payload, dict):
        print("Top-level keys:", list(payload.keys()))
        # Many APIs wrap the records in a key such as "data" or "results"
        records = next((v for v in payload.values() if isinstance(v, list)), None)
        if records is not None:
            print("Number of records (in nested list):", len(records))
            sample = records[0] if records else None
        else:
            sample = payload
    else:
        sample = payload

    # Step 8: print one sample record
    print("Sample record:")
    print(json.dumps(sample, indent=2, ensure_ascii=False))

    # Step 9: save the response to data/raw/api_snapshot.json
    OUTPUT_FILE.parent.mkdir(parents=True, exist_ok=True)
    with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
        json.dump(payload, f, indent=2, ensure_ascii=False)
    print("Saved to:", OUTPUT_FILE)

    # Step 10: retrieval timestamp in UTC -> copy this into docs/source_inventory.md
    print("retrieved_at_utc:", datetime.now(timezone.utc).isoformat())


if __name__ == "__main__":
    main()