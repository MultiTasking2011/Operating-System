import tkinter as tk
from tkinter import messagebox
import registerinterface

class login():
    def __init__(self, root) -> None:
        self.root = root
        self.root.title("Login")
        self.gui()


    def gui(self):
        self.signin = tk.Button(self.root, text="Sign In")
        self.register = tk.Button(self.root, text="Register", command="")
        # self.user = tk.Entry.get(self.root)
        # self.pwd = tk.Entry.get(self.root)

        # self.user.pack(pady=5, padx=5)
        # self.pwd.pack(pady=5, padx=5)
        self.signin.pack(pady=2, padx=2)
        self.register.pack(pady=2, padx=2)




if __name__ == '__main__':
    root=tk.Tk()
    app = login(root)
    root.mainloop()

