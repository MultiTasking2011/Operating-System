import tkinter as tk
from tkinter import colorchooser

class TinkerProject:
    def __init__(self, root):
        self.root = root
        self.root.title("Paint")
        
        self.pencolor = "red"
        self.pensize = 5
        self.xcoordinate = None
        self.ycoordinate = None
        self.shape = "Line"
        
        self.create_widgets()
        self.bind_events()

    def create_widgets(self):
        self.buttoncolor = tk.Button(self.root, text="Choose Color", command=self.colorchange)
        self.buttoncolor.pack(padx=5, pady=5)
        
        self.buttonclear = tk.Button(self.root, text="Clear Canvas", command=self.clearcanvas)
        self.buttonclear.pack(padx=5, pady=5)
        
        self.shape_var = tk.StringVar(value="Line")
        self.shape_menu = tk.OptionMenu(self.root, self.shape_var, "Line", "Rectangle", "Oval", command=self.setshape)
        self.shape_menu.pack(side=tk.LEFT, padx=5, pady=5)
        
        self.canvas = tk.Canvas(self.root, bg='white', width=600, height=400)
        self.canvas.pack(fill=tk.BOTH, expand=True)

    def bind_events(self):
        self.canvas.bind('<Button-1>', self.start_draw)
        self.canvas.bind('<B1-Motion>', self.draw)
        self.canvas.bind('<ButtonRelease-1>', self.stop_draw)

    def start_draw(self, event):
        self.xcoordinate, self.ycoordinate = event.x, event.y

    def draw(self, event):
        if self.xcoordinate and self.ycoordinate:
            if self.shape == "Line":
                self.canvas.create_line(self.xcoordinate, self.ycoordinate, event.x, event.y, fill=self.pencolor, width=self.pensize)
            elif self.shape == "Rectangle":
                self.canvas.delete("temp")
                self.canvas.create_rectangle(self.xcoordinate, self.ycoordinate, event.x, event.y, outline=self.pencolor, tags="temp")
            elif self.shape == "Oval":
                self.canvas.delete("temp")
                self.canvas.create_oval(self.xcoordinate, self.ycoordinate, event.x, event.y, outline=self.pencolor, tags="temp")

    def stop_draw(self, event):
        if self.shape in ["Rectangle", "Oval"]:
            self.canvas.delete("temp")
            if self.shape == "Rectangle":
                self.canvas.create_rectangle(self.xcoordinate, self.ycoordinate, event.x, event.y)
            elif self.shape == "Oval":
                self.canvas.create_oval(self.xcoordinate, self.ycoordinate, event.x, event.y)
        self.xcoordinate, self.ycoordinate = None, None

    def colorchange(self):
        color = colorchooser.askcolor()[1]
        if color:
            self.pencolor = color

    def setshape(self, shape):
        self.shape = shape

    def clearcanvas(self):
        self.canvas.delete('all')

if __name__ == '__main__':
    root = tk.Tk()
    app = TinkerProject(root)
    root.mainloop()
