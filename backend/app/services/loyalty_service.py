async def apply_loyalty(payload):
    return {"discount": 100, "final_price": payload.get("price", 0) - 100}
