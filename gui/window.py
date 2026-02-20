import tkinter as tk
from config.settings import BG_COLOR

def create_main_window():
    root = tk.Tk()
    root.title("💬 로컬 AI와의 대화")
    root.geometry("800x400")
    root.configure(bg=BG_COLOR)

    canvas = tk.Canvas(root, bg=BG_COLOR, highlightthickness=0)
    scrollbar = tk.Scrollbar(root, command=canvas.yview)
    scrollable_frame = tk.Frame(canvas, bg=BG_COLOR)

    # Scrollable frame 등록
    canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
    canvas.configure(yscrollcommand=scrollbar.set)
    canvas.pack(side="top", fill="both", expand=True)
    scrollbar.pack(side="right", fill="y")

    # 창 크기 변경 시 wraplength 업데이트
    def update_bubbles_wraplength(event=None):
        for widget in scrollable_frame.winfo_children():
            if isinstance(widget, tk.Label):
                widget.config(wraplength=max(canvas.winfo_width()-40, 100))

    canvas.bind("<Configure>", update_bubbles_wraplength)

    # 입력창
    entry_frame = tk.Frame(root, bg=BG_COLOR)
    entry_frame.pack(side="bottom", fill="x", padx=10, pady=5)

    entry = tk.Entry(entry_frame, font=("Helvetica",12), bg="#2e2e2e", fg="#ffffff", insertbackground="#ffffff")
    entry.pack(side="left", fill="x", expand=True, padx=(0,5))

    send_btn = tk.Button(entry_frame, text="전송", bg="#444444", fg="#ffffff")
    send_btn.pack(side="right")

    return root, scrollable_frame, canvas, entry, send_btn