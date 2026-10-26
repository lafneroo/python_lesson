import tkinter as tk
from .components.AppButton import AppButton

"основной отрисовщик"
class interface:
    def __init__(self, width=500, height=500):
        self.root = tk.Tk()

        self.width = width
        self.height = height
        self.root.geometry(f"{width}x{height}")
        self.root.iconbitmap("../assets/icon.ico")
        self.root.title("Task Manager")
        self.root.configure(bg="black")



    "отображает меню"
    def show_menu(self):
        AppButton(self.root, "primary").pack()

    "отображение задач"
    def show_tasks(self):
        lable = tk.Label(self.root, text="задача1").pack()

