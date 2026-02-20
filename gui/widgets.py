import tkinter as tk
from config.settings import BG_COLOR, USER_BG, AI_BG, TEXT_COLOR, FONT

def add_bubble(parent_frame, canvas, text, is_user=True):
    bubble = tk.Label(
        parent_frame,
        text=text,
        bg=USER_BG if is_user else AI_BG,
        fg=TEXT_COLOR,
        font=FONT,
        wraplength=max(canvas.winfo_width()-40, 100),  # 최소 100px
        justify="left",
        padx=10,
        pady=5
    )
    bubble.pack(anchor="e" if is_user else "w", pady=5, padx=10)
    parent_frame.update_idletasks()
    canvas.update_idletasks()
    canvas.yview_moveto(1.0)  # 항상 스크롤 아래
    return bubble