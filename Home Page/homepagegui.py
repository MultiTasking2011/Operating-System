import tkinter as tk
from PIL import Image, ImageTk

class BasicWindow:
    def __init__(self, root):
        self.root = root
        self.root.title("Home")
        self.homepage()
    
    def homepage(self):
        # Calculator Image
        image_calc = Image.open("Home Page/download.png")
        resized_image_calc = image_calc.resize((40, 40), Image.ANTIALIAS)
        self.calcimage = ImageTk.PhotoImage(resized_image_calc)
        self.calculator = tk.Button(self.root, image=self.calcimage)
        self.calculator.pack()

        # Clock Image
        image_clock = Image.open("Home Page/clock.png")
        resized_image_clock = image_clock.resize((40, 40), Image.ANTIALIAS)
        self.clockimage = ImageTk.PhotoImage(resized_image_clock)
        self.clock = tk.Button(self.root, image=self.clockimage)
        self.clock.pack()

        # Chess Image
        image_chess = Image.open("Home Page/chess.png")
        resized_image_chess = image_chess.resize((40, 40), Image.ANTIALIAS)
        self.chessimage = ImageTk.PhotoImage(resized_image_chess)
        self.chess = tk.Button(self.root, image=self.chessimage)
        self.chess.pack()

        # Paint Image (corrected to use the paint image instead of clock)
        image_paint = Image.open("Home Page/paint.png")
        resized_image_paint = image_paint.resize((40, 40), Image.ANTIALIAS)
        self.paintimage = ImageTk.PhotoImage(resized_image_paint)
        self.paint = tk.Button(self.root, image=self.paintimage)
        self.paint.pack()

        # # Video Games Image
        # image_video_games = Image.open("Home Page/videogames.jpg")
        # resized_image_video_games = image_video_games.resize((40, 40), Image.ANTIALIAS)
        # self.videogamesimage = ImageTk.PhotoImage(resized_image_video_games)
        # self.videogames = tk.Button(self.root, image=self.videogamesimage)
        # self.videogames.pack()

        # Textedit Image
        image_textedit = Image.open("Home Page/textedit.png")
        resized_image_textedit = image_textedit.resize((40, 40), Image.ANTIALIAS)
        self.texteditimage = ImageTk.PhotoImage(resized_image_textedit)
        self.textedit = tk.Button(self.root, image=self.texteditimage)
        self.textedit.pack()

        # Terminal Image
        image_terminal = Image.open("Home Page/terminal.png")
        resized_image_terminal = image_terminal.resize((40, 40), Image.ANTIALIAS)
        self.terminalimage = ImageTk.PhotoImage(resized_image_terminal)
        self.terminal = tk.Button(self.root, image=self.terminalimage)
        self.terminal.pack()

        # Search Image
        image_search = Image.open("Home Page/search.png")
        resized_image_search = image_search.resize((40, 40), Image.ANTIALIAS)
        self.searchimage = ImageTk.PhotoImage(resized_image_search)
        self.search = tk.Button(self.root, image=self.searchimage)
        self.search.pack()

        # Quiverr Image
        image_quiverr = Image.open("Home Page/quiverr.png")
        resized_image_quiverr = image_quiverr.resize((40, 40), Image.ANTIALIAS)
        self.quiverrimage = ImageTk.PhotoImage(resized_image_quiverr)
        self.quiverr = tk.Button(self.root, image=self.quiverrimage)
        self.quiverr.pack()

        # Files Image
        image_files = Image.open("Home Page/files.png")
        resized_image_files = image_files.resize((40, 40), Image.ANTIALIAS)
        self.filesimage = ImageTk.PhotoImage(resized_image_files)
        self.files = tk.Button(self.root, image=self.filesimage)
        self.files.pack()

        # Data Image
        image_data = Image.open("Home Page/data.jpg")
        resized_image_data = image_data.resize((40, 40), Image.ANTIALIAS)
        self.dataimage = ImageTk.PhotoImage(resized_image_data)
        self.data = tk.Button(self.root, image=self.dataimage)
        self.data.pack()

        # Calendar Image
        image_calendar = Image.open("Home Page/calender.png")
        resized_image_calendar = image_calendar.resize((40, 40), Image.ANTIALIAS)
        self.calendarimage = ImageTk.PhotoImage(resized_image_calendar)
        self.calendar = tk.Button(self.root, image=self.calendarimage)
        self.calendar.pack()

if __name__ == "__main__":
    root = tk.Tk()
    app = BasicWindow(root)
    root.mainloop()