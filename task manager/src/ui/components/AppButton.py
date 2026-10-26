import tkinter as tk

class AppButton(tk.Button):
    def __init__(self, master, status):
        super().__init__(master,width=10, height=2)
        self.status = status
        self.configure(background='red', activebackground="orange")
    def settings(self):
        if self.status == "primary":
            self.configure(background='green', activebackground="yellow")
        if self.status == "secondary":
            self.configure(background='blue', activebackground="pink")
        else:
            self.configure(background='black', activebackground="white")