import tkinter as tk
from PIL import Image, ImageTk
import os

class BasicWindow:
    def __init__(self, root):
        self.root = root
        self.root.title("Home")
        self.root.geometry('800x480')  # Adjusted window size
        self.images = []  # Store image references
        self.homepage()

    def homepage(self):
        # List of image files and their positions with padding adjustments
        image_info = [
            ("download.png", 0.075, 0.13),
            ("clock.png", 0.35, 0.13),
            ("chess.png", 0.65, 0.13),
            ("paint.png", 0.925, 0.13),
            ("textedit.png", 0.075, 0.48),
            ("terminal.png", 0.35, 0.48),
            ("search.png", 0.65, 0.48),
            ("download.jpeg", 0.925, 0.48),
            ("quiverr.png", 0.075, 0.83),
            ("files.png", 0.35, 0.83),
            ("data.jpg", 0.65, 0.83),
            ("calender.png", 0.925, 0.83)
        ]

        for img_file, relx, rely in image_info:
            img_path = f"Home Page/{img_file}"
            assert os.path.exists(img_path), f"{img_path} not found."

            self.image = Image.open(img_path)
            self.resized_image = self.image.resize((120, 120), Image.Resampling.LANCZOS)  # Adjusted button size
            self.image_obj = ImageTk.PhotoImage(self.resized_image)

            button = tk.Button(self.root, image=self.image_obj)
            button.place(relx=relx, rely=rely, anchor='center', width=120, height=120)  # Adjusted button size

            self.images.append(self.image_obj)  # Keep reference to avoid garbage collection

if __name__ == "__main__":
    root = tk.Tk()
    app = BasicWindow(root)
    root.mainloop()