"""
==============================
    список задач (обёртка tk.Listbox)
==============================
"""
import tkinter as tk


class AppListbox(tk.Listbox):
    def __init__(self, master, **kwargs):
        kwargs.setdefault("font", ("Arial", 10))
        kwargs.setdefault("exportselection", False)  # сохранять выделение при клике на кнопки
        super().__init__(master, **kwargs)
