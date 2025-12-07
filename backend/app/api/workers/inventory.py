from fastapi import APIRouter
from app.services.inventory_service import check_inventory

router = APIRouter()

@router.get("/check")
async def check(sku: str, store_id: str):
    stock = await check_inventory(sku, store_id)
    return {"sku": sku, "stock": stock}
