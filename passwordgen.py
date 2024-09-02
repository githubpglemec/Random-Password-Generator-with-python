import tkinter as tk
from tkinter import messagebox
import random
import string

def generate_passwords():
    try:
        num_passwords = int(num_passwords_entry.get())
        password_length = int(password_length_entry.get())

        if password_length < 8 or password_length > 15:
            messagebox.showerror("Invalid Length", "Password length must be between 8 and 15.")
            return

        passwords = []
        for _ in range(num_passwords):
            password_characters = string.ascii_letters + string.digits + string.punctuation
            password = ''.join(random.choice(password_characters) for i in range(password_length))
            passwords.append(password)

        passwords_text.delete(1.0, tk.END)
        passwords_text.insert(tk.END, "\n".join(passwords))

    except ValueError:
        messagebox.showerror("Input Error", "Please enter valid numbers for password count and length.")

# Create the main application window
root = tk.Tk()
root.title("Random Password Generator")

# Create and place the labels, entries, and buttons
tk.Label(root, text="Number of Passwords:").grid(row=0, column=0, padx=10, pady=10)
num_passwords_entry = tk.Entry(root)
num_passwords_entry.grid(row=0, column=1, padx=10, pady=10)

tk.Label(root, text="Password Length:").grid(row=1, column=0, padx=10, pady=10)
password_length_entry = tk.Entry(root)
password_length_entry.grid(row=1, column=1, padx=10, pady=10)

generate_button = tk.Button(root, text="Generate Passwords", command=generate_passwords)
generate_button.grid(row=2, column=0, columnspan=2, pady=10)

passwords_text = tk.Text(root, height=10, width=50)
passwords_text.grid(row=3, column=0, columnspan=2, padx=10, pady=10)

# Run the main loop
root.mainloop()
