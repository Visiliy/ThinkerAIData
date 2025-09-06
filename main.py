from qwen_api import Qwen
from qwen_api.core.types.chat import ChatMessage
from dotenv import load_dotenv

load_dotenv()

client = Qwen()

messages = [ChatMessage(
    role="user",
    content="Hello",
    web_search=False,
    thinking=False
)]

response = client.chat.create(
    messages=messages,
    model="qwen-max-latest"
)

print(response.choices.message.content)
