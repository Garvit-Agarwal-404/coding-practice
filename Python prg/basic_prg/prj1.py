import tkinter as tk
from tkinter import messagebox
import random
import string
import pyperclip

def generate_password():
    length = length_var.get()
    if length <= 0:
        messagebox.showerror("Invalid", "Length must be greater than 0")
        return

    chars = ""
    if use_lower.get(): chars += string.ascii_lowercase
    if use_upper.get(): chars += string.ascii_uppercase
    if use_digits.get(): chars += string.digits
    if use_special.get(): chars += string.punctuation

    if not chars:
        messagebox.showerror("Invalid", "Select at least one character type")
        return

    password = ''.join(random.choice(chars) for _ in range(length))
    password_entry.delete(0, tk.END)
    password_entry.insert(0, password)

def copy_to_clipboard():
    pyperclip.copy(password_entry.get())
    messagebox.showinfo("Copied", "Password copied to clipboard!")

# GUI setup
root = tk.Tk()
root.title("Password Generator")
root.geometry("350x300")

length_var = tk.IntVar(value=12)
use_lower = tk.BooleanVar(value=True)
use_upper = tk.BooleanVar()
use_digits = tk.BooleanVar()
use_special = tk.BooleanVar()

tk.Label(root, text="Password Length:").pack()
tk.Spinbox(root, from_=4, to=32, textvariable=length_var, width=5).pack()

tk.Checkbutton(root, text="Include Lowercase", variable=use_lower).pack()
tk.Checkbutton(root, text="Include Uppercase", variable=use_upper).pack()
tk.Checkbutton(root, text="Include Digits", variable=use_digits).pack()
tk.Checkbutton(root, text="Include Special Chars", variable=use_special).pack()

tk.Button(root, text="Generate Password", command=generate_password).pack(pady=10)

password_entry = tk.Entry(root, width=30)
password_entry.pack()

tk.Button(root, text="Copy to Clipboard", command=copy_to_clipboard).pack(pady=5)

root.mainloop()
