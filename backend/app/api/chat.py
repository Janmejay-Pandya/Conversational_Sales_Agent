from fastapi import APIRouter
from pydantic import BaseModel
from app.services.session_manager import create_session, store_message
from app.services.sales_agent import generate_sales_response

router = APIRouter()

class StartSession(BaseModel):
    customer_id: str

class UserMessage(BaseModel):
    text: str

@router.post("/start")
async def start_chat(payload: StartSession):
    session_id = await create_session(payload.customer_id)
    return {"session_id": session_id}

@router.post("/{session_id}/message")
async def send_message(session_id: str, payload: UserMessage):
    await store_message(session_id, "user", payload.text)
    reply, products = await generate_sales_response(session_id, payload.text)
    print("BOT REPLY:", reply)
    return {
        "reply": reply,
        "products": products,
    }
