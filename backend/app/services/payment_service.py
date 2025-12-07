import httpx

PAYMENT_API = "http://localhost:8003/authorize"

async def process_payment(amount, method="card", force_fail=False):
    async with httpx.AsyncClient() as client:
        response = await client.post(PAYMENT_API, json={
            "amount": amount,
            "method": method,
            "force_fail": force_fail
        })
        return response.json()
