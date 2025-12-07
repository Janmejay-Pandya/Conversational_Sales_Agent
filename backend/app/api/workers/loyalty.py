from fastapi import APIRouter
from app.services.loyalty_service import apply_loyalty

router = APIRouter()

@router.post("/apply")
async def apply(payload: dict):
    return await apply_loyalty(payload)
