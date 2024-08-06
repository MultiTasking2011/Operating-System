import tkinter as tk
from tkinter import messagebox


class register():
    def __init__(self, root) -> None:
        self.root = root
        self.root.title("Register")
        self.gui()


    def gui(self):
        self.acct_cr = tk.Button(self.root, text="Create Account")
        self.user = tk.Entry(self.root)
        self.pwd = tk.Entry(self.root)

        self.user.pack(pady=5, padx=5)
        self.pwd.pack(pady=5, padx=5)
        self.acct_cr.pack(pady=2, padx=2)

if __name__ == '__main__':
    root=tk.Tk()
    app = register(root)
    root.mainloop()

