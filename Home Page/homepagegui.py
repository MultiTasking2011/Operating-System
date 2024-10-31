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
            ("download.png", 0.975, 0.95),
            ("clock.png", 0.975, 0.95),
            ("chess.png", 0.975, 0.95),
            ("paint.png", 0.975, 0.95),
            ("textedit.png", 0.975, 0.95),
            ("terminal.png", 0.975, 0.95),
            ("search.png", 0.975, 0.95),
            ("download.jpeg", 0.975, 0.95),
            ("quiverr.png", 0.975, 0.95),
            ("files.png", 0.975, 0.95),
            ("data.jpg", 0.975, 0.95),
            ("calender.png", 0.975, 0.95)
        ]

        for img_file, relx, rely in image_info:
            img_path = f"Home Page/{img_file}"
            assert os.path.exists(img_path), f"{img_path} not found."

            self.image = Image.open(img_path)
            self.resized_image = self.image.resize((40, 40), Image.Resampling.LANCZOS)  # Adjusted button size
            self.image_obj = ImageTk.PhotoImage(self.resized_image)

            button = tk.Button(self.root, image=self.image_obj)
            button.place(relx=relx, rely=rely, anchor='center', width=35, height=35)  # Adjusted button size

            self.images.append(self.image_obj)  # Keep reference to avoid garbage collection

if __name__ == "__main__":
    root = tk.Tk()
    app = BasicWindow(root)
    root.mainloop()