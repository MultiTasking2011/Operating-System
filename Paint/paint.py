import tkinter as tk
from tkinter import messagebox, colorchooser

class tinkerproject():
    def __init__(self, root):
        self.root = root
        self.root.title("Paint")
        self.window()
        self.pencolor = "black"
        self.pensize = 5
        self.xcoordinate = None
        self.ycoordinate = None
        self.bind_events()
    
    def window(self):
        self.buttoncolor = tk.Button(self.root,text="Choose color", command=self.colorchange)
        self.buttoncolor.pack( padx=5, pady=5)
        self.buttonclear = tk.Button(self.root, text = "Clear canvas", command=self.clearcanvas)
        self.buttonclear.pack(padx=5, pady=5)
        self.canvas = tk.Canvas(self.root, bg='white', width=300, height=300)
        self.canvas.pack(fill=tk.BOTH, expand=True)

    def bind_events(self):
        self.canvas.bind('<B1-Motion>', self.paint) # Left mouse button is held down, and mouse is moved
        self.canvas.bind('<Button-1>', self.start_paint) # Left btn is clicked
        self.canvas.bind('<ButtonRelease-1>' ,self.reset)  # Left btn is released


    def start_paint(self, event):
        self.xcoordinate, self.ycoordinate = event.x, event.y
    
    def reset(self, event):
        self.xcoordinate, self.ycoordinate = None, None
    
    def paint(self, event):
        if self.xcoordinate and self.ycoordinate:
            self.canvas.create_line(event.x-1, event.y-1, event.x, event.y, fill=self.pencolor, width=self.pensize)
            self.xcoordinate, self.ycoordinate = event.x, event.y


    def colorchange(self):
        color = colorchooser.askcolor()[1]
        print(color)
        if color:
            self.pencolor = color

    def clearcanvas(self):
        self.canvas.delete('all')

if __name__ == '__main__':
    root=tk.Tk()
    app = tinkerproject(root)
    root.mainloop()
