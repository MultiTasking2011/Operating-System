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
        self.output = None
        self.gui()


    def gui(self):
        #creation
        self.one = tk.Button(self.root, text="1", font="inconsolata", command = self.one)
        self.two = tk.Button(self.root, text="2", font="inconsolata", command = self.two)
        self.three = tk.Button(self.root, text="3", font="inconsolata", command = self.three)
        self.four = tk.Button(self.root, text="4", font="inconsolata", command = self.four)
        self.five = tk.Button(self.root, text="5", font="inconsolata", command = self.five)
        self.six = tk.Button(self.root, text="6", font="inconsolata", command = self.six)
        self.seven = tk.Button(self.root, text="7", font="inconsolata", command = self.seven)
        self.eight = tk.Button(self.root, text="8", font="inconsolata", command = self.eight)
        self.nine = tk.Button(self.root, text="9", font="inconsolata", command = self.nine)
        self.zero = tk.Button(self.root, text="0", font="inconsolata", command = self.zero)
        self.multiplication = tk.Button(self.root, text="x", font="inconsolata", command=self.opmultiplication)
        self.division = tk.Button(self.root, text="÷", font="inconsolata", command=self.opdivision)
        self.addition = tk.Button(self.root, text="+", font="inconsolata", command=self.opaddition)
        self.subtraction = tk.Button(self.root, text="-", font="inconsolata", command=self.opsubtraction)
        self.clear = tk.Button(self.root, text="C", font="inconsolata", command=self.clearing)
        self.squareroot = tk.Button(self.root, text="√", font="inconsolata", command=self.opsqrt)
        self.cuberoot = tk.Button(self.root, text="∛", font="inconsolata", command = self.opcbrt)
        self.decimalpoint = tk.Button(self.root, text=".", font="inconsolata", command = self.decimal)
        self.approx = tk.Button(self.root, text="≈", font="inconsolata")
        self.equals = tk.Button(self.root, text="=", font="inconsolata", command=self.compute)
        self.text = tk.Text(self.root, width = 22, height = 3)

        #placing
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
        self.text.place(relx = 0, rely = 0)

    #code
    def one(self):
        self.numbercreation.append(str(1))
        self.text.delete(1.0, tk.END)
        self.text.insert(tk.END, self.numbercreation)

    def two(self):
        self.numbercreation.append(str(2))
        self.text.delete(1.0, tk.END)
        self.text.insert(tk.END, self.numbercreation)

    def three(self):
        self.numbercreation.append(str(3))
        self.text.delete(1.0, tk.END)
        self.text.insert(tk.END, self.numbercreation)

    def four(self):
        self.numbercreation.append(str(4))
        self.text.delete(1.0, tk.END)
        self.text.insert(tk.END, self.numbercreation)

    def five(self):
        self.numbercreation.append(str(5))
        self.text.delete(1.0, tk.END)
        self.text.insert(tk.END, self.numbercreation)

    def six(self):
        self.numbercreation.append(str(6))
        self.text.delete(1.0, tk.END)
        self.text.insert(tk.END, self.numbercreation)

    def seven(self):
        self.numbercreation.append(str(7))
        self.text.delete(1.0, tk.END)
        self.text.insert(tk.END, self.numbercreation)

    def eight(self):
        self.numbercreation.append(str(8))
        self.text.delete(1.0, tk.END)
        self.text.insert(tk.END, self.numbercreation)

    def nine(self):
        self.numbercreation.append(str(9))
        self.text.delete(1.0, tk.END)
        self.text.insert(tk.END, self.numbercreation)

    def zero(self):
        self.numbercreation.append(str(0))
        self.text.delete(1.0, tk.END)
        self.text.insert(tk.END, self.numbercreation)

    def decimal(self):
        self.numbercreation.append('.')
        self.text.delete(1.0, tk.END)
        self.text.insert(tk.END, self.numbercreation)

    def clearing(self):
        self.text.delete(1.0, tk.END)
        self.numbercreation.clear()
        self.operationlist.clear()
        self.numberlist.clear()

    def finishnumber(self):
        self.number = float(''.join(self.numbercreation))
        self.numberlist.append(self.number)
        self.numbercreation.clear()

    def opmultiplication(self):
        self.finishnumber()
        self.text.delete(1.0, tk.END)
        self.operationlist.append('m')

    def opdivision(self):
        self.finishnumber()
        self.text.delete(1.0, tk.END)
        self.operationlist.append('d')

    def opaddition(self):
        self.finishnumber()
        self.text.delete(1.0, tk.END)
        self.operationlist.append('a')

    def opsubtraction(self):
        self.finishnumber()
        self.text.delete(1.0, tk.END)
        self.operationlist.append('s')

    def opsqrt(self):
        self.finishnumber()
        self.text.delete(1.0, tk.END)
        self.operationlist.append('srt')

    def opcbrt(self):
        self.finishnumber()
        self.text.delete(1.0, tk.END)
        self.operationlist.append('crt')

    def compute(self):
        self.finishnumber()
        if int((len(self.numberlist))/2) == len(self.operationlist):
            print(self.numberlist, self.operationlist)
            print((len(self.numberlist))/2, len(self.operationlist))
        else:
            self.text.delete(1.0, tk.END)
            self.text.insert(tk.END, "Error")


        

if __name__ == '__main__':
    root=tk.Tk()
    app = calculator(root)
    root.mainloop()

