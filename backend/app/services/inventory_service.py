from app.db.collections import inventory

async def check_inventory(sku: str, store_id: str):
    record = await inventory().find_one({"sku": sku})
    if not record:
        return 0
    return record["locations"].get(store_id, 0)
