import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk, Image
import os

class LoginChecker:
    def __init__(self, user, pwd):
        self.user = user
        self.pwd = pwd

    def check_login(self, filename='login.txt'):
        with open(filename, 'r') as file:
            for line in file:
                if self.user in line and self.pwd in line:
                    user_index = line.find(self.user)
                    pwd_index = line.find(self.pwd)
                    if user_index < pwd_index:
                        return True

class Login:
    def __init__(self, root) -> None:
        self.root = root
        self.root.title("Login")
        self.gui()

    def gui(self):
        self.signin = tk.Button(self.root, text="Sign In", command=self.check_credentials)
        self.register = tk.Button(self.root, text="Register", command=self.subprocessfunc)
        self.user = tk.Entry(self.root)
        self.pwd = tk.Entry(self.root, show="*")

        self.user.pack(pady=5, padx=5)
        self.pwd.pack(pady=5, padx=5)
        self.signin.pack(pady=2, padx=2)
        self.register.pack(pady=2, padx=2)

    def subprocessfunc(self):
        current_dir = os.getcwd()
        target_dir = '/Applications/Documents/Suraj/Coding Folder/My Projects/Operating System/Login'
        if current_dir != target_dir:
            os.chdir(target_dir)
        with open("registerinterface.py") as file:
            exec(file.read())

    def check_credentials(self):
        user = self.user.get()
        pwd = self.pwd.get()
        checker = LoginChecker(user, pwd)
        if checker.check_login("Login/login/login/login.txt"):
            messagebox.showinfo("Login Success", "Credentials found in the correct order.")
            with open("Home Page/homepagegui.py") as file:
                exec(file.read())
        else:
            messagebox.showerror("Login Failed", "Credentials not found or not in the correct order.")

if __name__ == '__main__':
    root = tk.Tk()
    app = Login(root)
    root.mainloop()