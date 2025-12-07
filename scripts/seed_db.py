# scripts/seed_db.py
import json
from pymongo import MongoClient
from pathlib import Path

MONGO_URI = "mongodb+srv://jay110504:42hBGhBpEEqphnn9@cluster1.byhut.mongodb.net/retail_ai?retryWrites=true&w=majority"
DB_NAME = "retail_ai"

def load_json(filepath):
    return json.loads(Path(filepath).read_text())

def main():
    client = MongoClient(MONGO_URI)
    db = client[DB_NAME]

    print("Clearing existing collections...")
    db.customers.delete_many({})
    db.products.delete_many({})
    db.inventory.delete_many({})
    db.promotions.delete_many({})
    db.stores.delete_many({})

    print("Inserting stores, customers, products, inventory, promotions...")

    SAMPLE_DIR = Path(__file__).parent / "data"
    if SAMPLE_DIR.exists():
        db.stores.insert_many(load_json(SAMPLE_DIR / "stores.json"))
        db.customers.insert_many(load_json(SAMPLE_DIR / "customers.json"))
        db.products.insert_many(load_json(SAMPLE_DIR / "products.json"))
        db.inventory.insert_many(load_json(SAMPLE_DIR / "inventory.json"))
        db.promotions.insert_many(load_json(SAMPLE_DIR / "promotions.json"))
        print("Inserted from scripts/data/*.json")
    else:
        print("No scripts/data folder found. Please save the provided JSON blocks into scripts/data/*.json and re-run.")
        return

    print("Seeding complete.")

if __name__ == "__main__":
    main()
