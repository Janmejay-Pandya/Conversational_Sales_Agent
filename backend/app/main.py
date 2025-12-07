from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .router import api_router
from .db.mongo import connect_to_mongo, close_mongo_connection

app = FastAPI(title="Omnichannel Sales Agent Backend")

# CORS for frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# Routers
app.include_router(api_router)

@app.on_event("startup")
async def startup_event():
    await connect_to_mongo()

@app.on_event("shutdown")
async def shutdown_event():
    await close_mongo_connection()
