import tkinter as tk

root = tk.Tk()
root.geometry("400x400")

size = 6
i = 0

while i < size * size:
    row = i // size
    col = i % size

    # Единственный if для проверки узора
    if row == 0 or row == size - 1 or col == 0 or col == size - 1:
        tk.Button(root, text="X").place(x=col * 50 + 50, y=row * 50 + 50, width=45, height=45)

    i += 1

root.mainloop()