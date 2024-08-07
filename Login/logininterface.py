import tkinter as tk
from tkinter import messagebox

class login():
    def __init__(self, root) -> None:
        self.root = root
        self.root.title("Login")
        self.gui()


    def gui(self):
        self.signin = tk.Button(self.root, text="Sign In")
        self.register = tk.Button(self.root, text="Register", command=self.subprocessfunc)
        self.user = tk.Entry(self.root)
        self.pwd = tk.Entry(self.root, show="*")

        self.user.pack(pady=5, padx=5)
        self.pwd.pack(pady=5, padx=5)
        self.signin.pack(pady=2, padx=2)
        self.register.pack(pady=2, padx=2)

    def subprocessfunc(self):
        with open("registerinterface.py") as file:
            exec(file.read())



if __name__ == '__main__':
    root=tk.Tk()
    app = login(root)
    root.mainloop()

