from fastapi import FastAPI
from pydantic import BaseModel
import uvicorn
import random

app = FastAPI(title="Mock Payment Gateway")

class PaymentPayload(BaseModel):
    amount: float
    method: str
    card_last4: str | None = None
    force_fail: bool | None = False


@app.post("/authorize")
async def authorize(payload: PaymentPayload):

    # Force decline if requested (for demo)
    if payload.force_fail:
        return {"status": "declined", "reason": "forced_failure"}

    # Simulated decline for large amounts
    if payload.amount > 6000:
        return {"status": "declined", "reason": "insufficient_funds"}

    # Simulated random network error
    if random.random() < 0.1:
        return {"status": "error", "reason": "network_error"}

    return {
        "status": "success",
        "transaction_id": f"TXN-{random.randint(10000,99999)}"
    }


if __name__ == "__main__":
    uvicorn.run(app, host="localhost", port=8003)
