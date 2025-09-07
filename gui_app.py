import tkinter as tk
from tkinter import messagebox
import random

# characters
LOWER = "abcdefghijklmnoprstuvwxyz"
UPPER = "ABCDEFGHİJKLMNOPRSTUVWXYZ"
NUMBERS = "0123456789"
SYMBOLS = "[](){}*;,./\\._-<>!'^+%&=?"

# tkinter gui
root = tk.Tk()
root.title("Password Generator")
root.geometry("500x300")
root.configure(bg="#0D0D0D")
root.resizable(False, False)

# custom font
FONT = ("Press Start 2P", 10)

# logic
def generate_password():
    char_set = ""
    if var_lower.get():
        char_set += LOWER
    if var_upper.get():
        char_set += UPPER
    if var_numbers.get():
        char_set += NUMBERS
    if var_symbols.get():
        char_set += SYMBOLS

    length = slider.get()
    
    if not char_set:
        messagebox.showerror("Error", "Select at least one character type!")
        return
    if length > len(char_set):
        messagebox.showerror("Error", "Length too long for unique sampling!")
        return

    password = "".join(random.sample(char_set, length))
    password_var.set(password)

def copy_password():
    root.clipboard_clear()
    root.clipboard_append(password_var.get())
    root.update()
    messagebox.showinfo("Copied", "Password copied to clipboard!")

# gui widgets
title = tk.Label(
    root,
    text="PASSWORD GENERATOR",
    font=("Press Start 2P", 14),
    bg="#0D0D0D",
    fg="#FFA500"
)
title.pack(pady=10)

password_var = tk.StringVar()
password_entry = tk.Entry(
    root,
    textvariable=password_var,
    font=FONT,
    bg="#000000",
    fg="#FFFFFF",
    justify="center",
    width=30,
    relief="flat"
)
password_entry.pack(pady=10)

# character type checkboxes
checkbox_frame = tk.Frame(root, bg="#0D0D0D")
checkbox_frame.pack(pady=5)

var_lower = tk.BooleanVar(value=True)
var_upper = tk.BooleanVar(value=True)
var_numbers = tk.BooleanVar(value=True)
var_symbols = tk.BooleanVar(value=True)

tk.Checkbutton(
    checkbox_frame, text="Lowercase", font=FONT, bg="#0D0D0D", fg="#FFD700",
    activebackground="#000000", activeforeground="#FFD700", selectcolor="#000000",
    variable=var_lower
).grid(row=0, column=0, padx=5, pady=2)

tk.Checkbutton(
    checkbox_frame, text="Uppercase", font=FONT, bg="#0D0D0D", fg="#FFD700",
    activebackground="#000000", activeforeground="#FFD700", selectcolor="#000000",
    variable=var_upper
).grid(row=0, column=1, padx=5, pady=2)

tk.Checkbutton(
    checkbox_frame, text="Numbers", font=FONT, bg="#0D0D0D", fg="#FFD700",
    activebackground="#000000", activeforeground="#FFD700", selectcolor="#000000",
    variable=var_numbers
).grid(row=1, column=0, padx=5, pady=2)

tk.Checkbutton(
    checkbox_frame, text="Symbols", font=FONT, bg="#0D0D0D", fg="#FFD700",
    activebackground="#000000", activeforeground="#FFD700", selectcolor="#000000",
    variable=var_symbols
).grid(row=1, column=1, padx=5, pady=2)

# password length slider
slider_label = tk.Label(
    root,
    text="Password Length:",
    font=FONT,
    bg="#0D0D0D",
    fg="#FFD700"
)
slider_label.pack()

slider = tk.Scale(
    root,
    from_=6,
    to=32,
    orient="horizontal",
    font=FONT,
    bg="#0D0D0D",
    fg="#FFFFFF",
    troughcolor="#FFA500",
    highlightthickness=0
)
slider.set(16)
slider.pack(pady=5)

# buttons
btn_frame = tk.Frame(root, bg="#0D0D0D")
btn_frame.pack(pady=10)

generate_btn = tk.Button(
    btn_frame,
    text="GENERATE",
    font=FONT,
    bg="#FFA500",
    fg="#0D0D0D",
    activebackground="#FFD700",
    activeforeground="#000000",
    command=generate_password,
    width=12
)
generate_btn.grid(row=0, column=0, padx=5)

copy_btn = tk.Button(
    btn_frame,
    text="COPY",
    font=FONT,
    bg="#FFD700",
    fg="#0D0D0D",
    activebackground="#FFA500",
    activeforeground="#000000",
    command=copy_password,
    width=8
)
copy_btn.grid(row=0, column=1, padx=5)

# run
root.mainloop()