# Main App
import tkinter as tk
from screeninfo import get_monitors

class MainApp(tk.Tk):

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, *kwargs)
        

        self.verify_resolution()
        self.title('OPCalculator')
        self.resizable(False,False)
        self.container = tk.Frame(self)
        self.container.pack(side = 'top', fill = 'both', expand = True)
        self.container.grid_rowconfigure(0, weight = 1)
        self.container.grid_columnconfigure(0, weight = 1)
        self.frames = {}
        self.frames["MainPage"] = MainPage(parent = self.container, controller = self)
        self.frames["MainPage"].grid(row = 0, column = 0, sticky = 'nsew')
        self.show_frame("MainPage")

    def show_frame(self, page):
        frame = self.frames[page]
        frame.tkraise()
    
    def verify_resolution(self):
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()
        x = (screen_width/2) - 260
        y = (screen_height/2) - 270
        self.geometry(f'520x520+{int(x)}+{int(y)}')
    
class MainPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        self.controller = controller
        main_frame = tk.Frame(self, width = 520, height = 520, bg = "#1B262C")
        main_frame.pack(fill = "both", expand = True)
        display_frame = tk.Frame(main_frame, width = 480, height = 70, bg = "#0F4C75")
        display_frame.pack(fill = "both")
        button_frame = tk.Frame(main_frame, width = 500, height = 450, bg = "#0F4C75")
        button_frame.pack(fill = "both")
        button_clearall = tk.Button(button_frame, text = "CLEAR", font = ('Bebas Neue', 20), width = 10, height = 1, cursor = "hand2")
        button_clearall.grid(row = 0, column = 0)


if __name__ == "__main__":
    app = MainApp()
    app.mainloop()