import random
import string
import tkinter as tk
from tkinter import ttk


# Function to generate a password
def generate_password():
    length = int(length_var.get())
    use_special = special_var.get()

    letters = string.ascii_letters
    digits = string.digits
    special_chars = string.punctuation if use_special else ""
    all_chars = letters + digits + special_chars

    if length < 4:
        result_label.config(text="Password too short!")
        return

    # Ensure password contains at least one of each required character type
    password = [
        random.choice(letters),
        random.choice(digits),
        random.choice(special_chars) if use_special else random.choice(letters)
    ]
    password += [random.choice(all_chars) for _ in range(length - len(password))]
    random.shuffle(password)

    result_label.config(text="".join(password))


# Initialize the app window
app = tk.Tk()
app.title("Password Generator")
app.geometry("400x200")
app.resizable(False, False)

# Label for title
title_label = tk.Label(app, text="Password Generator", font=("Arial", 16, "bold"))
title_label.pack(pady=10)

# Length selection
length_frame = tk.Frame(app)
length_frame.pack(pady=5)
length_label = tk.Label(length_frame, text="Length:")
length_label.pack(side="left", padx=5)
length_var = tk.StringVar(value="12")
length_entry = tk.Entry(length_frame, textvariable=length_var, width=5)
length_entry.pack(side="left")

# Special characters toggle
special_var = tk.BooleanVar(value=True)
special_check = tk.Checkbutton(app, text="Include Special Characters", variable=special_var)
special_check.pack(pady=5)

# Generate button
generate_button = ttk.Button(app, text="Generate Password", command=generate_password)
generate_button.pack(pady=10)

# Result display
result_label = tk.Label(app, text="", font=("Courier", 12, "bold"), fg="blue")
result_label.pack(pady=10)

# Run the app
app.mainloop()