import ollama
import json
import os
from config.settings import EMOJI_ASCII, SYSTEM_PROMPT

MEMORY_FILE = "data/chat_memory.json"

def load_messages():
    if os.path.exists(MEMORY_FILE):
        with open(MEMORY_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    return [{"role": "system", "content": SYSTEM_PROMPT}]

def save_messages(messages):
    with open(MEMORY_FILE, "w", encoding="utf-8") as f:
        json.dump(messages, f, ensure_ascii=False, indent=2)

def get_ai_response(messages):
    try:
        response = ollama.chat(model="llama3", messages=messages)
        content = response.get("message", {}).get("content", "응답 없음")

        emotion = "무관심"
        if content.startswith("감정:"):
            try:
                emotion_line, rest = content.split("\n", 1)
                tag = emotion_line.replace("감정:", "").strip()
                if tag in EMOJI_ASCII:
                    emotion = tag
                content = rest.strip()
            except Exception:
                pass
        return content, emotion
    except Exception as e:
        return "오류 발생! 다시 시도해 주세요.", "무관심"