from fastapi import APIRouter
from app.db.collections import sessions

router=APIRouter()

@router.get("/{session_id}/history")
async def get_history(session_id: str):
    doc= await sessions().find_one({"session_id":session_id})
    return doc.get("history",[]) if doc else []
