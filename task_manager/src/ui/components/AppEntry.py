"""
==============================
    поле ввода (обёртка tk.Entry)
==============================
"""
import tkinter as tk


class AppEntry(tk.Entry):
    def __init__(self, master, **kwargs):
        kwargs.setdefault("bg", "white")
        kwargs.setdefault("fg", "black")
        kwargs.setdefault("insertbackground", "black")
        super().__init__(master, **kwargs)
