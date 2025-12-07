from motor.motor_asyncio import AsyncIOMotorClient
from app.config.settings import settings

mongo_client=None
db=None

async def connect_to_mongo():
    global mongo_client,db
    print("Connecting to mongo")
    mongo_client=AsyncIOMotorClient(settings.MONGO_URI)
    db=mongo_client[settings.DATABASE_NAME]
    print(db)
    print("Connected to Mongo")

async def close_mongo_connection():
    global mongo_client
    mongo_client.close()

