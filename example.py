# NovaPAI Python SDK Example
# Install: pip install openai
# Docs: https://api.novapai.ai

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


# ── List Available Models ───────────────────────────────────
models = client.models.list()
for model in models.data:
    print(model.id)
