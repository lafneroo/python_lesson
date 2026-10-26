import tkinter as tk
from .components.AppButton import AppButton


"основной отрисовщик"
class interface:
    def __init__(self, collection, width=500, height=500,):
        self.root = tk.Tk()

        self.width = width
        self.height = height
        self.root.geometry(f"{width}x{height}")
        self.root.iconbitmap("../assets/icon.ico")
        self.root.title("Task Manager")
        self.root.configure(bg="black")
        self.task_lists = collection


    "отображает меню"
    def show_menu(self):
        AppButton(self.root, "primary", text="показать задачи", command=lambda:self.show_tasks()).pack()

    "отображение задач"
    def show_tasks(self):
        task_box = tk.Listbox(self.root)
        for task in self.task_lists:
            task_box.insert(tk.END, task[0]["name"])
        task_box.pack()

