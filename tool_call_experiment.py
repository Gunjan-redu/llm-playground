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




messages = [{"role": "user", "content": "what is the weather of Mumbai?"}]



client = anthropic.Anthropic()
while True:
    message = client.messages.create(
        model= "claude-haiku-5-5",
        max_tokens= 200,
        tools = tools,
        messages=messages
    )

    if message.stop_reason != "tool_use":
        break

    messages.append({"role": "assistant", "content":  message.content})

    for block in message.content:
        if block.type == "tool_use":
            result = f"The weather 30deg C in {block.input['city']}"
            messages.append({"role": "user",  "content": [{
                    "type": "tool_result",
                    "tool_use_id": block.id,
                    "content": result,
                }] })


print(message.content)
