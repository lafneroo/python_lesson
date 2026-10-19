import tkinter as tk

class interface:
    def __init__(self, *args, **kwargs):
        self.root = tk.Tk()

        self.root.geometry("500x500")
        self.root.iconbitmap("../assets/icon.ico")
        self.root.title("Task Manager")

        self.root.mainloop()

interface = interface()

