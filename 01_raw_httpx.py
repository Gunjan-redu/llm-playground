import httpx, os
from dotenv import load_dotenv

load_dotenv()

r = httpx.post(
    "https://api.anthropic.com/v1/messages",
    headers={
        "x-api-key": os.environ["ANTHROPIC_API_KEY"],
        "anthropic-version": "2023-06-01",
        "content-type": "application/json",
    },
    json={
        "model": "claude-haiku-5-5",
        "max_tokens": 200,
        "messages": [{"role": "user", "content": "Explain in two sentences what an API is, to a 10-year-old."}],
    },
    timeout=30.0,
)
print(r.status_code)
print(r.json()["content"][0]["text"])
print(r.json()["usage"])

