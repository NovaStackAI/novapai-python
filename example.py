# NovaPAI Python SDK Example
# Install: pip install openai
# Docs: https://novapai.ai

import json
from openai import OpenAI

client = OpenAI(
    api_key="your-api-key",
    base_url="https://api.novapai.ai/router/v1"
)

# ── Basic Chat ──────────────────────────────────────────────
response = client.chat.completions.create(
    model="deepseek-v4-pro",
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "Hello!"}
    ]
)
print(response.choices[0].message.content)


# ── Streaming ───────────────────────────────────────────────
stream = client.chat.completions.create(
    model="deepseek-v4-pro",
    messages=[{"role": "user", "content": "Tell me a joke"}],
    stream=True
)
for chunk in stream:
    if chunk.choices[0].delta.content:
        print(chunk.choices[0].delta.content, end="", flush=True)
print()


# ── Multi-turn Conversation ─────────────────────────────────
messages = [{"role": "system", "content": "You are a helpful assistant."}]

def chat(user_input):
    messages.append({"role": "user", "content": user_input})
    response = client.chat.completions.create(
        model="deepseek-v4-pro",
        messages=messages
    )
    reply = response.choices[0].message.content
    messages.append({"role": "assistant", "content": reply})
    return reply

print(chat("What is 1+1?"))
print(chat("Multiply that by 10"))


# ── Function Calling ────────────────────────────────────────
tools = [{
    "type": "function",
    "function": {
        "name": "get_weather",
        "description": "Get current weather for a city",
        "parameters": {
            "type": "object",
            "properties": {
                "city": {"type": "string", "description": "City name"}
            },
            "required": ["city"]
        }
    }
}]

response = client.chat.completions.create(
    model="deepseek-v4-pro",
    messages=[{"role": "user", "content": "What's the weather in Tokyo?"}],
    tools=tools
)

tool_call = response.choices[0].message.tool_calls[0]
print(f"Function: {tool_call.function.name}")
print(f"Args: {tool_call.function.arguments}")

# Simulate function result and continue conversation
function_result = {"city": "Tokyo", "temperature": 22, "condition": "sunny"}
messages = [
    {"role": "user", "content": "What's the weather in Tokyo?"},
    response.choices[0].message,
    {
        "role": "tool",
        "tool_call_id": tool_call.id,
        "content": json.dumps(function_result)
    }
]
final = client.chat.completions.create(
    model="deepseek-v4-pro",
    messages=messages
)
print(final.choices[0].message.content)


# ── JSON Mode (Structured Output) ───────────────────────────
response = client.chat.completions.create(
    model="deepseek-v4-pro",
    messages=[
        {"role": "system", "content": "Extract company info as JSON."},
        {"role": "user", "content": "Apple Inc. is based in Cupertino, founded in 1976."}
    ],
    response_format={
        "type": "json_object"
    }
)
data = json.loads(response.choices[0].message.content)
print(json.dumps(data, indent=2))


# ── List Available Models ───────────────────────────────────
models = client.models.list()
for model in models.data:
    print(model.id)
