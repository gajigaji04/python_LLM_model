import ollama
import json
import os

# 대화 기록 저장 파일
MEMORY_FILE = "chat_memory.json"

# 이전 대화 불러오기
if os.path.exists(MEMORY_FILE):
    with open(MEMORY_FILE, "r", encoding="utf-8") as f:
        messages = json.load(f)
else:
    messages = [
        {"role": "system", "content": "너는 장난기 많고 유머러스한 AI야. 한국어로 자연스럽게 대답해라."}
    ]

print("🤖 재밌는 한국어 AI 시작 (exit 입력하면 종료)")

while True:
    user_input = input("You: ")

    if user_input.lower() == "exit":
        print("AI 종료")
        break

    # 사용자 메시지 추가
    messages.append({"role": "user", "content": user_input})

    # Ollama 모델에게 요청
    try:
        response = ollama.chat(
            model="llama3",
            messages=messages
        )
        ai_message = response["message"]["content"]
    except Exception as e:
        ai_message = "오류 발생! 다시 시도해 주세요."
        print("⚠️", e)

    print("AI:", ai_message)

    # AI 메시지 기록
    messages.append({"role": "assistant", "content": ai_message})

    # 대화 저장
    with open(MEMORY_FILE, "w", encoding="utf-8") as f:
        json.dump(messages, f, ensure_ascii=False, indent=2)