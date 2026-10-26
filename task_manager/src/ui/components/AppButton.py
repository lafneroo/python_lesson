import tkinter as tk

class AppButton(tk.Button):
    def __init__(self, master, status, text, command):
        super().__init__(master,width=12, height=2, text=text, command=command)
        self.status = status
        self.settings()


    def settings(self):
        if self.status == "primary":
            self.configure(background='green', activebackground="yellow", activeforeground="black")
        elif self.status == "secondary":
            self.configure(background='blue', activebackground="pink", activeforeground="white")
        else:
            self.configure(background='black', activebackground="white", activeforeground="yellow")