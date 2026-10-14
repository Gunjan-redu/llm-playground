import anthropic
from dotenv import load_dotenv

load_dotenv()
client = anthropic.Anthropic()

def talk(query):
    message = client.messages.create(
        model= "claude-haiku-5-5",
        max_tokens= 200,
        messages=[{"role": "user", "content": query}],
        system = "You are a patient teacher explaining to a 12-year-old"

    )

    return "".join(block.text for block in message.content if block.type == "text")