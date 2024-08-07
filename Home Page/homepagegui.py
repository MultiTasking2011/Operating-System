import tkinter as tk
from PIL import Image, ImageTk

class BasicWindow:
    def __init__(self, root):
        self.root = root
        self.root.title("Home")
        self.homepage()
    
    def homepage(self):
        # Open and resize the image
        image = Image.open("Home Page/download.png")
        resized_image = image.resize((40, 40), Image.ANTIALIAS)
        
        # Convert the image to PhotoImage
        self.calcimage = ImageTk.PhotoImage(resized_image)
        
        # Create a button with the resized image
        self.calculator = tk.Button(self.root, image=self.calcimage)
        self.calculator.pack()

if __name__ == "__main__":
    root = tk.Tk()
    app = BasicWindow(root)
    root.mainloop()