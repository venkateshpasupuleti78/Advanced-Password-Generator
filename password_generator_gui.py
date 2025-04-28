import string
import secrets
import pyperclip
import tkinter as tk
from tkinter import messagebox

def generate_password():
    length = length_var.get()
    use_upper = upper_var.get()
    use_lower = lower_var.get()
    use_digits = digits_var.get()
    use_symbols = symbols_var.get()

    characters = ''
    if use_upper:
        characters += string.ascii_uppercase
    if use_lower:
        characters += string.ascii_lowercase
    if use_digits:
        characters += string.digits
    if use_symbols:
        characters += string.punctuation

    if not characters:
        messagebox.showerror("Error", "Please select at least one character type!")
        return

    try:
        length = int(length)
        if length <= 0:
            messagebox.showerror("Error", "Length must be positive!")
            return
    except ValueError:
        messagebox.showerror("Error", "Invalid length!")
        return

    password = ''.join(secrets.choice(characters) for _ in range(length))
    password_entry.delete(0, tk.END)
    password_entry.insert(0, password)
    pyperclip.copy(password)
    save_password(password)
    messagebox.showinfo("Success", "Password generated and copied to clipboard!")

def save_password(password):
    with open('generated_passwords_gui.txt', 'a') as f:
        from datetime import datetime
        now = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        f.write(f"{now} - {password}\n")

# --- GUI Setup ---

root = tk.Tk()
root.title("🔐 Advanced Password Generator")
root.geometry("400x400")
root.resizable(False, False)
root.configure(bg="#f0f0f0")

# Title Label
title = tk.Label(root, text="🔐 Password Generator", font=("Arial", 18, "bold"), bg="#f0f0f0", fg="#333")
title.pack(pady=10)

# Frame for options
frame = tk.Frame(root, bg="#f0f0f0")
frame.pack(pady=10)

length_label = tk.Label(frame, text="Password Length:", bg="#f0f0f0")
length_label.grid(row=0, column=0, sticky="w")
length_var = tk.Entry(frame)
length_var.grid(row=0, column=1)

upper_var = tk.BooleanVar()
lower_var = tk.BooleanVar()
digits_var = tk.BooleanVar()
symbols_var = tk.BooleanVar()

upper_check = tk.Checkbutton(frame, text="Include Uppercase", variable=upper_var, bg="#f0f0f0")
upper_check.grid(row=1, column=0, sticky="w", pady=2)
lower_check = tk.Checkbutton(frame, text="Include Lowercase", variable=lower_var, bg="#f0f0f0")
lower_check.grid(row=2, column=0, sticky="w", pady=2)
digits_check = tk.Checkbutton(frame, text="Include Digits", variable=digits_var, bg="#f0f0f0")
digits_check.grid(row=1, column=1, sticky="w", pady=2)
symbols_check = tk.Checkbutton(frame, text="Include Symbols", variable=symbols_var, bg="#f0f0f0")
symbols_check.grid(row=2, column=1, sticky="w", pady=2)

# Generate button
generate_button = tk.Button(root, text="Generate Password", command=generate_password, bg="#4CAF50", fg="white", font=("Arial", 12, "bold"))
generate_button.pack(pady=15)

# Password Entry
password_entry = tk.Entry(root, width=30, font=("Arial", 14), justify="center")
password_entry.pack(pady=10)

# Footer
footer = tk.Label(root, text="By Venkatesh ✨", bg="#f0f0f0", fg="#888", font=("Arial", 10))
footer.pack(side="bottom", pady=5)

root.mainloop()
import string
import secrets
import pyperclip
import tkinter as tk
from tkinter import messagebox

def generate_password():
    length = length_var.get()
    use_upper = upper_var.get()
    use_lower = lower_var.get()
    use_digits = digits_var.get()
    use_symbols = symbols_var.get()

    characters = ''
    if use_upper:
        characters += string.ascii_uppercase
    if use_lower:
        characters += string.ascii_lowercase
    if use_digits:
        characters += string.digits
    if use_symbols:
        characters += string.punctuation

    if not characters:
        messagebox.showerror("Error", "Please select at least one character type!")
        return

    try:
        length = int(length)
        if length <= 0:
            messagebox.showerror("Error", "Length must be positive!")
            return
    except ValueError:
        messagebox.showerror("Error", "Invalid length!")
        return

    password = ''.join(secrets.choice(characters) for _ in range(length))
    password_entry.delete(0, tk.END)
    password_entry.insert(0, password)
    pyperclip.copy(password)
    save_password(password)
    messagebox.showinfo("Success", "Password generated and copied to clipboard!")

def save_password(password):
    with open('generated_passwords_gui.txt', 'a') as f:
        from datetime import datetime
        now = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        f.write(f"{now} - {password}\n")

# --- GUI Setup ---

root = tk.Tk()
root.title("🔐 Advanced Password Generator")
root.geometry("400x400")
root.resizable(False, False)
root.configure(bg="#f0f0f0")

# Title Label
title = tk.Label(root, text="🔐 Password Generator", font=("Arial", 18, "bold"), bg="#f0f0f0", fg="#333")
title.pack(pady=10)

# Frame for options
frame = tk.Frame(root, bg="#f0f0f0")
frame.pack(pady=10)

length_label = tk.Label(frame, text="Password Length:", bg="#f0f0f0")
length_label.grid(row=0, column=0, sticky="w")
length_var = tk.Entry(frame)
length_var.grid(row=0, column=1)

upper_var = tk.BooleanVar()
lower_var = tk.BooleanVar()
digits_var = tk.BooleanVar()
symbols_var = tk.BooleanVar()

upper_check = tk.Checkbutton(frame, text="Include Uppercase", variable=upper_var, bg="#f0f0f0")
upper_check.grid(row=1, column=0, sticky="w", pady=2)
lower_check = tk.Checkbutton(frame, text="Include Lowercase", variable=lower_var, bg="#f0f0f0")
lower_check.grid(row=2, column=0, sticky="w", pady=2)
digits_check = tk.Checkbutton(frame, text="Include Digits", variable=digits_var, bg="#f0f0f0")
digits_check.grid(row=1, column=1, sticky="w", pady=2)
symbols_check = tk.Checkbutton(frame, text="Include Symbols", variable=symbols_var, bg="#f0f0f0")
symbols_check.grid(row=2, column=1, sticky="w", pady=2)

# Generate button
generate_button = tk.Button(root, text="Generate Password", command=generate_password, bg="#4CAF50", fg="white", font=("Arial", 12, "bold"))
generate_button.pack(pady=15)

# Password Entry
password_entry = tk.Entry(root, width=30, font=("Arial", 14), justify="center")
password_entry.pack(pady=10)

# Footer
footer = tk.Label(root, text="By Venkatesh ✨", bg="#f0f0f0", fg="#888", font=("Arial", 10))
footer.pack(side="bottom", pady=5)

root.mainloop()
