import tkinter as tk

def button_click(char):
    if char == "=":
        try:
            text_input.config(text=str(eval(text_input.cget("text"))))
        except:
            text_input.config(text="Error")
    elif char == "C":
        text_input.config(text="")
    else:
        current_text = text_input.cget("text")
        if current_text == "Error":
            text_input.config(text=char)
        else:
            text_input.config(text=current_text + char)

root = tk.Tk()
root.title("Калькулятор")

text_input = tk.Label(root, text="", bg="white", anchor="e", font=("Arial", 20))
text_input.grid(row=0, column=0, columnspan=4, sticky="nsew")

buttons = ["7", "8", "9", "/", "4", "5", "6", "*", "1", "2", "3", "-", "C", "0", "=", "+"]
row = 1
col = 0

for btn_text in buttons:
    action = button_click if btn_text in "0123456789+-*/=C" else None
    tk.Button(root, text=btn_text, command=lambda t=btn_text: action(t), font=("Arial", 16)).grid(row=row, column=col, sticky="nsew")
    col += 1
    if col > 3:
        col = 0
        row += 1

for i in range(4):
    root.grid_columnconfigure(i, weight=1)
for i in range(5):
    root.grid_rowconfigure(i, weight=1)

root.mainloop()