from gui.window import create_main_window
from gui.widgets import add_bubble
from ai.chat import get_ai_response, load_messages, save_messages
from config.settings import EMOJI_ASCII
import threading

messages = load_messages()

# GUI 생성
root, scrollable_frame, canvas, entry, send_btn = create_main_window()

# 기존 메시지 화면에 표시
for msg in messages:
    content = msg["content"]
    if msg["role"] == "user":
        add_bubble(scrollable_frame, canvas, content, is_user=True)
    elif msg["role"] == "assistant":
        # 감정 라인 제거하고 표시
        lines = content.split("\n", 1)
        content_only = lines[1] if len(lines) > 1 else lines[0]
        add_bubble(scrollable_frame, canvas, content_only, is_user=False)

# -----------------------
# 새 메시지 전송
# -----------------------
def send_message(event=None):
    user_input = entry.get().strip()
    if not user_input:
        return
    entry.delete(0, "end")

    # 사용자 말풍선
    add_bubble(scrollable_frame, canvas, user_input, is_user=True)
    messages.append({"role": "user", "content": user_input})

    # AI 로딩 말풍선
    loading_label = add_bubble(scrollable_frame, canvas, "AI가 답장 중...", is_user=False)

    # AI 응답 스레드
    def ai_thread():
        content, emotion = get_ai_response(messages)
        # 메인 스레드에서 GUI 업데이트
        def finish():
            loading_label.config(text=f"{EMOJI_ASCII.get(emotion,'(-_-)')} {content}")
            messages.append({"role": "assistant", "content": f"감정:{emotion}\n{content}"})
            save_messages(messages)
        root.after(0, finish)

    threading.Thread(target=ai_thread, daemon=True).start()

# 버튼 & 엔터키
send_btn.config(command=send_message)
entry.bind("<Return>", send_message)

root.mainloop()