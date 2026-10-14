import anthropic
from dotenv import load_dotenv
from pydantic import BaseModel, ValidationError


class Person(BaseModel):
    name: str
    age: int
    profession: str

load_dotenv()

#TEXT= "Priya is a 34-year-old architect from Pune who loves teaching origami on weekends. She has a friend Lakshmi."

TEXT = "Priya is an architect from Pune who loves origami."

prompt = f"""Extract the person's name, age, and profession from this text.
Respond with ONLY valid JSON in exactly this shape: {{"name": ..., "age": ..., "profession": ...}}
No other text, no markdown fences.

Text: {TEXT}
"""

client = anthropic.Anthropic()

for i in range(5):
    message = client.messages.parse(
        model="claude-haiku-5-5",
        max_tokens= 200,
        messages= [{"role": "user", "content": prompt}],
        output_format = Person
    )

    print(message.parsed_output)


