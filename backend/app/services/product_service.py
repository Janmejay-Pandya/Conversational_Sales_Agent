from app.db.collections import products

def _build_product_filter(user_text: str):
    text = user_text.lower()
    query = {}

    if any(w in text for w in ["shoe", "shoes", "sneaker", "trainer", "running"]):
        query["category"] = "shoes"

    # have to add more categories later (bags, dress, etc.)
    return query

def _serialize_product(doc: dict) -> dict:
    """
    Convert a raw MongoDB document into a JSON-safe product dict
    that the frontend can consume.
    """
    if not doc:
        return {}

    return {
        "sku": doc.get("sku"),
        "name": doc.get("name"),
        "category": doc.get("category"),
        "brand": doc.get("brand"),
        "price": doc.get("price"),
        "images": doc.get("images", []),
    }

async def recommend_products_from_db(user_text: str, limit: int = 3):
    query = _build_product_filter(user_text)
    cursor = products().find(query).limit(limit)
    docs = [doc async for doc in cursor]
    return [_serialize_product(d) for d in docs]

async def simple_recommender(limit: int = 3):
    cursor = products().find().limit(limit)
    docs = [doc async for doc in cursor]
    return [_serialize_product(d) for d in docs]
