from app.db.collections import orders
import uuid

async def reserve_item(payload):
    order_id = str(uuid.uuid4())
    await orders().insert_one({
        "order_id": order_id,
        "sku": payload["sku"],
        "store_id": payload["store_id"],
        "status": "reserved"
    })
    return {"order_id": order_id, "status": "reserved"}

async def track_order(order_id):
    doc = await orders().find_one({"order_id": order_id})
    return doc or {"error": "Order not found"}
