import uuid
from datetime import datetime, timezone
from app.db.collections import sessions

async def create_session(customer_id: str):
    session_id = str(uuid.uuid4())
    await sessions().insert_one({
        "session_id": session_id,
        "customer_id": customer_id,
        "history": [],
        "created_at": datetime.now(timezone.utc)
    })
    return session_id

async def store_message(session_id: str, sender: str, text: str):
    await sessions().update_one(
        {"session_id": session_id},
        {"$push": {"history": {"sender": sender, "text": text, "ts": datetime.utcnow()}}}
    )
