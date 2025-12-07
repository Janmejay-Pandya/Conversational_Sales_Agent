from fastapi import APIRouter
from app.services.payment_service import process_payment

router = APIRouter()

@router.post("/pay")
async def pay(payload: dict):
    return await process_payment(payload)
