from fastapi import WebSocket

connected_clients = {}

async def connect(session_id: str, websocket: WebSocket):
    await websocket.accept()
    connected_clients.setdefault(session_id, []).append(websocket)

async def broadcast(session_id: str, message: str):
    for ws in connected_clients.get(session_id, []):
        await ws.send_text(message)
