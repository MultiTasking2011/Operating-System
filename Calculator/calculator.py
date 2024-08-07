import tkinter as tk
from tkinter import messagebox
import math

class calculator():
    def __init__(self, root) -> None:
        self.root = root
        self.root.title("Calculator")
        self.numbercreation = list()
        self.operationlist = list()
        self.numberlist = list()
        self.gui()


    def gui(self):
        self.one = tk.Button(self.root, text="1", font="inconsolata")
        self.two = tk.Button(self.root, text="2", font="inconsolata")
        self.three = tk.Button(self.root, text="3", font="inconsolata")
        self.four = tk.Button(self.root, text="4", font="inconsolata")
        self.five = tk.Button(self.root, text="5", font="inconsolata")
        self.six = tk.Button(self.root, text="6", font="inconsolata")
        self.seven = tk.Button(self.root, text="7", font="inconsolata")
        self.eight = tk.Button(self.root, text="8", font="inconsolata")
        self.nine = tk.Button(self.root, text="9", font="inconsolata")
        self.zero = tk.Button(self.root, text="0", font="inconsolata")
        self.multiplication = tk.Button(self.root, text="x", font="inconsolata")
        self.division = tk.Button(self.root, text="÷", font="inconsolata")
        self.addition = tk.Button(self.root, text="+", font="inconsolata")
        self.subtraction = tk.Button(self.root, text="-", font="inconsolata")
        self.clear = tk.Button(self.root, text="C", font="inconsolata")
        self.squareroot = tk.Button(self.root, text="√", font="inconsolata")
        self.cuberoot = tk.Button(self.root, text="∛", font="inconsolata")
        self.decimalpoint = tk.Button(self.root, text=".", font="inconsolata")
        self.approx = tk.Button(self.root, text="≈", font="inconsolata")
        self.equals = tk.Button(self.root, text="=", font="inconsolata")

        self.zero.place(relx = 0.1, rely= 0.9, anchor="center")
        self.one.place(relx = 0.1, rely= 0.75, anchor="center")
        self.two.place(relx = 0.3, rely= 0.75, anchor="center")
        self.three.place(relx = 0.5, rely= 0.75, anchor="center")
        self.four.place(relx = 0.1, rely= 0.6, anchor="center")
        self.five.place(relx = 0.3, rely= 0.6, anchor="center")
        self.six.place(relx = 0.5, rely= 0.6, anchor="center")
        self.seven.place(relx = 0.1, rely= 0.45, anchor="center")
        self.eight.place(relx = 0.3, rely= 0.45, anchor="center")
        self.nine.place(relx = 0.5, rely= 0.45, anchor="center")
        self.decimalpoint.place(relx = 0.3, rely= 0.9, anchor="center")
        self.clear.place(relx = 0.5, rely= 0.9, anchor="center")
        self.equals.place(relx = 0.7, rely= 0.9, anchor="center")
        self.addition.place(relx = 0.7, rely= 0.75, anchor="center")
        self.subtraction.place(relx = 0.7, rely= 0.6, anchor="center")
        self.multiplication.place(relx = 0.7, rely= 0.45, anchor="center")
        self.division.place(relx = 0.7, rely= 0.3, anchor="center")
        self.squareroot.place(relx = 0.1, rely= 0.3, anchor="center")
        self.cuberoot.place(relx = 0.3, rely= 0.3, anchor="center")
        self.approx.place(relx = 0.5, rely= 0.3, anchor="center")

if __name__ == '__main__':
    root=tk.Tk()
    app = calculator(root)
    root.mainloop()

