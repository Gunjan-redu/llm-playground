from dotenv import load_dotenv
import anthropic

load_dotenv()

tools = [{
    "name": "get_weather",
    "description": "get the weather of a city ",
    "input_schema":{
        "type": "object",
        "properties": { "city": { "type": "string" , "description": "The city name"  } },
    "required": ["city"]
    }
}


]

client = anthropic.Anthropic()

message = client.messages.create(
    model= "claude-haiku-5-5",
    max_tokens= 200,
    tools = tools,
    messages=[{"role": "user", "content": "What's the weather in Mumbai?"}]

)

print(message)
print(type(message))