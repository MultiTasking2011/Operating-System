import tkinter as tk

class BasicWindow:
    def __init__(self, root):
        self.root = root
        self.root.title("code")
        self.homepage()
    
    def homepage(self):
        self.calcimage = "download.png"
        self.calculator = tk.Button(width = 1, height = 1, image="download.png")
        self.calculator.pack(self.root)

if __name__ == "__main__":
    root = tk.Tk()
    app = BasicWindow(root)
    root.mainloop()