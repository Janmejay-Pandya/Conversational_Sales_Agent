from groq import Groq
from app.config.settings import settings

client = Groq(api_key=settings.GROQ_API_KEY)

async def llm_generate(prompt: str) -> str:
    response = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.6,
    )
    print("LLM RAW RESPONSE:", response)
    print("LLM CONTENT:", response.choices[0].message.content)

    return response.choices[0].message.content
