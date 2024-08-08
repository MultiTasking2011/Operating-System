import tkinter as tk
from PIL import Image, ImageTk, Image
import os

class BasicWindow:
    def __init__(self, root):
        self.root = root
        self.root.title("Home")
        self.root.geometry('1800x800')  # Set a fixed window size
        self.images = []  # Store image references
        self.homepage()

    def homepage(self):
        # List of image files and their positions with padding adjustments
        image_info = [
            ("download.png", 0.05, 0.13),
            ("clock.png", 0.35, 0.13),
            ("chess.png", 0.65, 0.13),
            ("paint.png", 0.95, 0.13),
            ("textedit.png", 0.05, 0.48),
            ("terminal.png", 0.35, 0.48),
            ("search.png", 0.65, 0.48),
            ("download.jpeg", 0.95, 0.48),
            ("quiverr.png", 0.05, 0.83),
            ("files.png", 0.35, 0.83),
            ("data.jpg", 0.65, 0.83),
            ("calender.png", 0.95, 0.83)
        ]

        for img_file, relx, rely in image_info:
            img_path = f"Home Page/{img_file}"
            assert os.path.exists(img_path), f"{img_path} not found."

            self.image = Image.open(img_path)
            self.resized_image = self.image.resize((150, 150), Image.Resampling.LANCZOS)
            self.image_obj = ImageTk.PhotoImage(self.resized_image)

            button = tk.Button(self.root, image=self.image_obj)
            button.place(relx=relx, rely=rely, anchor='center', width=150, height=150)

            self.images.append(self.image_obj)  # Keep reference to avoid garbage collection

if __name__ == "__main__":
    root = tk.Tk()
    app = BasicWindow(root)
    root.mainloop()