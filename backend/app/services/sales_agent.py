from app.services.langchain_agent import llm_generate
from app.services.product_service import recommend_products_from_db, simple_recommender
from app.services.session_manager import store_message

async def generate_sales_response(session_id: str, user_text: str):
    """
    Returns (reply_text, products_list)
    products_list is a list of product dicts from MongoDB (can be empty).
    """
    text_lower = user_text.lower()

    if any(k in text_lower for k in ["shoe", "shoes", "sneaker", "trainer", "running"]):
        products = await recommend_products_from_db(user_text, limit=3)
        if not products:
            products = await simple_recommender(limit=3)

        if not products:
            reply = "I couldn’t find shoes in our catalog right now. Want to try a different category?"
            await store_message(session_id, "bot", reply)
            return reply, []

        lines = []
        for idx, p in enumerate(products, start=1):
            name = p.get("name")
            sku = p.get("sku")
            price = p.get("price")
            lines.append(f"{idx}) {name} (SKU: {sku}, ₹{price})")

        reply = (
            "Here are some options from our catalog:\n\n"
            + "\n".join(lines)
            + "\n\nYou can ask me to check size or store availability for any of these."
        )

        await store_message(session_id, "bot", reply)
        return reply, products

    prompt = (
        "You are a concise, helpful retail sales agent for a fashion & footwear brand. "
        "Be direct and avoid asking unnecessary questions. "
        "If the user clearly asks for a product, suggest next steps like size, budget, or style. "
        f"User said: {user_text}. "
        "Give a friendly, short response (1–2 sentences)."
    )

    reply = await llm_generate(prompt)
    await store_message(session_id, "bot", reply)
    return reply, []
