from fastapi import APIRouter
from .api import chat, session
from .api.workers import recommendation, inventory, payment, fulfillment, loyalty, post_purchase

api_router=APIRouter()

#chat
api_router.include_router(chat.router,prefix="/chat",tags=["Chat"])
api_router.include_router(session.router,prefix="/sessions",tags=["Sessions"])

#worker Agents

api_router.include_router(recommendation.router,prefix="/worker/recommend",tags=["Worker: Recommendation"])
api_router.include_router(inventory.router,prefix="/worker/inventory",tags=["Worker: Inventory"])
api_router.include_router(payment.router,prefix="/worker/payment",tags=["Worker: Payment"])
api_router.include_router(fulfillment.router,prefix="/worker/fulfillment",tags=["Worker: Fulfillment"])
api_router.include_router(loyalty.router,prefix="/worker/loyalty",tags=["Worker: Loyalty"])
api_router.include_router(post_purchase.router,prefix="/worker/support",tags=["Worker: Post-Purchase"])