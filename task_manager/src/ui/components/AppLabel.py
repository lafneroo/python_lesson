"""
==============================
    подпись (обёртка tk.Label)
==============================
"""
import tkinter as tk


class AppLabel(tk.Label):
    def __init__(self, master, **kwargs):
        kwargs.setdefault("bg", "black")
        kwargs.setdefault("fg", "white")
        super().__init__(master, **kwargs)
