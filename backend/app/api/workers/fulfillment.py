from fastapi import APIRouter
from app.services.fulfillment_service import reserve_item

router = APIRouter()

@router.post("/reserve")
async def reserve(payload: dict):
    return await reserve_item(payload)
