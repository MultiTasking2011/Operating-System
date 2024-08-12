import tkinter as tk
from tkinter import filedialog

class TextSaverApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Code Editor")  # Updated title

        # Create a textbox
        self.text_box = tk.Text(root, wrap='word', height=10, width=40)
        self.text_box.pack(pady=10)

        # Create a frame for buttons
        button_frame = tk.Frame(root)
        button_frame.pack(pady=10)

        # Create a save button
        self.save_button = tk.Button(button_frame, text="Save", command=self.save_to_file)
        self.save_button.pack(side=tk.LEFT, padx=5)

        # Create a run button
        self.run_button = tk.Button(button_frame, text="Run", command=self.run_code)
        self.run_button.pack(side=tk.LEFT, padx=5)

    def save_to_file(self):
        # Get the content from the textbox
        content = self.text_box.get("1.0", tk.END)
        with open("Code editor for coding language/language.txt", 'w') as file:
            file.write(content)

    def run_code(self):
        # This method is currently empty
        pass

if __name__ == "__main__":
    root = tk.Tk()
    app = TextSaverApp(root)
    root.mainloop()