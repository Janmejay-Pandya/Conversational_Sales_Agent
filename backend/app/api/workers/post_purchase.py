from fastapi import APIRouter
from app.services.fulfillment_service import track_order

router = APIRouter()

@router.get("/track")
async def track(order_id: str):
    return await track_order(order_id)
