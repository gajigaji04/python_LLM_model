import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

messages = [
    {"role": "system", "content": "당신은 친절한 AI 도우미입니다."}
]

print("🤖 LLM 챗봇 시작 (종료하려면 exit 입력)")

while True:
    user_input = input("You: ")

    if user_input.lower() == "exit":
        print("AI: 대화를 종료합니다.")
        break

    messages.append({"role": "user", "content": user_input})

    response = client.chat.completions.create(
        model="gpt-4.1-mini",
        messages=messages
    )

    reply = response.choices[0].message.content

    print("AI:", reply)

    messages.append({"role": "assistant", "content": reply})
