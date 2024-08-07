import tkinter as tk
from tkinter import messagebox
import os

class Register:
    def __init__(self, root) -> None:
        self.root = root
        self.root.title("Register")
        self.gui()

    def gui(self):
        self.user = tk.Entry(self.root)
        self.pwd = tk.Entry(self.root, show='*')  # Hide password input
        self.acct_cr = tk.Button(self.root, text="Create Account", command=self.append_to_file)

        self.user.pack(pady=5, padx=5)
        self.pwd.pack(pady=5, padx=5)
        self.acct_cr.pack(pady=2, padx=2)

    def append_to_file(self):
        usr = self.user.get()
        pwd = self.pwd.get()
        filename = "Login/login/login.txt"
        
        # Ensure the directory exists
        os.makedirs(os.path.dirname(filename), exist_ok=True)
        
        with open(filename, "a") as file:
            file.write(f"{usr},{pwd}\n")
        messagebox.showinfo("Success", "Account created successfully.")

if __name__ == '__main__':
    root = tk.Tk()
    app = Register(root)
    root.mainloop()