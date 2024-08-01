import tkinter as tk
import random
import string

class PasswordGeneratorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Password Generator")

        self.length_label = tk.Label(root, text="Enter desired password length:")
        self.length_label.pack()

        self.length_entry = tk.Entry(root)
        self.length_entry.pack()

        self.complexity_label = tk.Label(root, text="Select complexity:")
        self.complexity_label.pack()

        self.complexity_var = tk.StringVar(value="medium")
        self.simple_radio = tk.Radiobutton(root, text="Simple (only letters)", variable=self.complexity_var, value="simple")
        self.simple_radio.pack()
        self.medium_radio = tk.Radiobutton(root, text="Medium (letters and numbers)", variable=self.complexity_var, value="medium")
        self.medium_radio.pack()
        self.complex_radio = tk.Radiobutton(root, text="Complex (letters, numbers, and symbols)", variable=self.complexity_var, value="complex")
        self.complex_radio.pack()

        self.generate_button = tk.Button(root, text="Generate Password", command=self.generate_password)
        self.generate_button.pack()

        self.password_label = tk.Label(root, text="Generated Password:")
        self.password_label.pack()
        self.password_display = tk.Entry(root, state="readonly")
        self.password_display.pack()

    def generate_password(self):
        try:
            length = int(self.length_entry.get())
            complexity = self.complexity_var.get()

            if complexity == "simple":
                chars = string.ascii_letters
            elif complexity == "medium":
                chars = string.ascii_letters + string.digits
            else:
                chars = string.ascii_letters + string.digits + string.punctuation

            password = ''.join(random.choice(chars) for _ in range(length))
            self.password_display.config(state="normal")
            self.password_display.delete(0, tk.END)
            self.password_display.insert(0, password)
            self.password_display.config(state="readonly")
        except ValueError:
            self.password_display.config(state="normal")
            self.password_display.delete(0, tk.END)
            self.password_display.insert(0, "Please enter a valid number")
            self.password_display.config(state="readonly")

if __name__ == "__main__":
    root = tk.Tk()
    app = PasswordGeneratorApp(root)
    root.mainloop()











