#src/config.py
from openai import OpenAI

def init_client():
    client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key="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",
    )
    return client