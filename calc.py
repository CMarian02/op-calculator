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
        self.geometry(f'550x550+{int(x)}+{int(y)}')
    
class MainPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        self.controller = controller
        main_frame = tk.Frame(self, width = 520, height = 520, bg = "white")
        main_frame.pack(fill = "both", expand = True)
        display_frame = tk.Frame(main_frame, width = 520, height = 120, bg = "red")
        display_frame.pack(fill = "x")
        button_frame = tk.Frame(main_frame, width = 520, height = 400, bg = "#0F4C75")
        button_frame.pack(fill = 'both', expand = True)
        NonePhoto = tk.PhotoImage(width = 1, height = 1)
        #color #1B262C
        button_clearall = tk.Button(button_frame, text = "AC", font = ('Bebas Neue', 20), image = NonePhoto, compound = "c", width =140, height = 80, cursor = "hand2", command = lambda:self.check_btn())
        button_clearall.grid(row = 0, column = 0, sticky = tk.W)
        button_clearone = tk.Button(button_frame, text = "CC", font = ('Bebas Neue', 20), image = NonePhoto, compound = "c", width =140, height = 80, cursor = "hand2", command = lambda:self.check_btn())
        button_clearone.grid(row = 0, column = 1, stick = tk.W)
        button_mod = tk.Button(button_frame, text = "%", font = ('Bebas Neue', 20), image = NonePhoto, compound = "c", width =140, height = 80, cursor = "hand2", command = lambda:self.check_btn())
        button_mod.grid(row = 0, column = 2, sticky = tk.W)
        button_div = tk.Button(button_frame, text = "/", font = ('Bebas Neue', 20), image = NonePhoto, compound = "c", width =100, height = 80, cursor = "hand2", command = lambda:self.check_btn())
        button_div.grid(row = 0, column = 3, sticky = tk.W)
        button_sev = tk.Button(button_frame, text = "7", font = ('Bebas Neue', 20), image = NonePhoto, compound = "c", width =140, height = 80, cursor = "hand2", command = lambda:self.check_btn())
        button_sev.image = NonePhoto
        button_sev.grid(row = 1, column = 0)
        button_eig = tk.Button(button_frame, text = "8", font = ('Bebas Neue', 20), image = NonePhoto, compound = "c", width =140, height = 80, cursor = "hand2", command = lambda:self.check_btn())
        button_eig.grid(row = 1, column = 1)
        button_nin = tk.Button(button_frame, text = "9", font = ('Bebas Neue', 20), image = NonePhoto, compound = "c", width =140, height = 80, cursor = "hand2", command = lambda:self.check_btn())
        button_nin.grid(row = 1, column = 2)
        button_mul = tk.Button(button_frame, text = "X", font = ('Bebas Neue', 20), image = NonePhoto, compound = "c", width =100, height = 80, cursor = "hand2", command = lambda:self.check_btn())
        button_mul.grid(row = 1, column = 3)
        button_fou = tk.Button(button_frame, text = "4", font = ('Bebas Neue', 20), image = NonePhoto, compound = "c", width =140, height = 80, cursor = "hand2", command = lambda:self.check_btn())
        button_fou.grid(row = 2, column = 0)
        button_fiv = tk.Button(button_frame, text = "5", font = ('Bebas Neue', 20), image = NonePhoto, compound = "c", width =140, height = 80, cursor = "hand2", command = lambda:self.check_btn())
        button_fiv.grid(row = 2, column = 1)
        button_six = tk.Button(button_frame, text = "6", font = ('Bebas Neue', 20), image = NonePhoto, compound = "c", width =140, height = 80, cursor = "hand2", command = lambda:self.check_btn())
        button_six.grid(row = 2, column = 2)
        button_min = tk.Button(button_frame, text = "-", font = ('Bebas Neue', 20), image = NonePhoto, compound = "c", width =100, height = 80, cursor = "hand2", command = lambda:self.check_btn())
        button_min.grid(row = 2, column = 3)
        button_one = tk.Button(button_frame, text = "1", font = ('Bebas Neue', 20), image = NonePhoto, compound = "c", width =140, height = 80, cursor = "hand2", command = lambda:self.button_pressed("Number", 1))
        button_one.grid(row = 3, column = 0)
        button_two = tk.Button(button_frame, text = "2", font = ('Bebas Neue', 20), image = NonePhoto, compound = "c", width =140, height = 80, cursor = "hand2", command = lambda:self.button_pressed("Number",2))
        button_two.grid(row = 3, column = 1)
        button_thr = tk.Button(button_frame, text = "3", font = ('Bebas Neue', 20), image = NonePhoto, compound = "c", width =140, height = 80, cursor = "hand2", command = lambda:self.check_btn())
        button_thr.grid(row = 3, column = 2)
        button_plu = tk.Button(button_frame, text = "+", font = ('Bebas Neue', 20), image = NonePhoto, compound = "c", width =100, height = 80, cursor = "hand2", command = lambda:self.button_pressed("+", 0))
        button_plu.grid(row = 3, column = 3)
        button_next_pag = tk.Button(button_frame, text = ">>", font = ('Bebas Neue', 20), image = NonePhoto, compound = "c", width =140, height = 80, cursor = "hand2", command = lambda:self.check_btn())
        button_next_pag.grid(row = 4, column = 0)
        button_zer = tk.Button(button_frame, text = "0", font = ('Bebas Neue', 20), image = NonePhoto, compound = "c", width =140, height = 80, cursor = "hand2", command = lambda:self.check_btn())
        button_zer.grid(row = 4, column = 1)
        button_dig = tk.Button(button_frame, text = ",", font = ('Bebas Neue', 20), image = NonePhoto, compound = "c", width =140, height = 80, cursor = "hand2", command = lambda:self.check_btn())
        button_dig.grid(row = 4, column = 2)
        button_ans = tk.Button(button_frame, text = "=", font = ('bebas Neue', 20), image = NonePhoto, compound = "c", width =100, height = 80, cursor = "hand2", command = lambda:self.check_btn())
        button_ans.grid(row = 4, column = 3)
        global times
        global number_one
        global number_two
        global operator
        global nr
        nr = 0
        times = 0
    def check_btn(self):
        print('Checked')

    def button_pressed(self, button_type, number):
        global number_one
        global number_two
        global operator
        global times
        global nr
        
        print('test confirmed')
        while button_type == "Number":
            if times == 0:
                number_one = number
                times += 1
            number_one = number_one * 10 + number
            button_type = None
            print(f'number one is: {number_one}')
        if button_type == "+" and times != 0:
            operator = 1
            nr = 2
            times = 0
        while button_type == "Number" and nr == 2:
            if times == 0:
                number_two = number
                times += 1
            number_two = number_two * 10 + number
            button_type = None
            print(f"number two is:{number_two}")
        
if __name__ == "__main__":
    app = MainApp()
    app.mainloop()