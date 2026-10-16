import tkinter as tk

number = 0

def start():
    global number
    number += 1
    counter.config(text = number)

root = tk.Tk()

root.geometry("600x600")
root.iconbitmap("../assets/icon.ico")
root.title("Task Manager")

frame = tk.Frame(root,width=100,height=100)
frame.pack(padx=100, pady=100)

tk.Button(frame, text = "Добро пожаловать", background = "orange", padx=70, pady= 20, command=start).pack(pady=20)
counter = (tk.Label(frame, text = f'{number}' ))
counter.pack()

root.mainloop()