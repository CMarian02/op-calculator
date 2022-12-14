# Main App
import tkinter as tk
from decimal import *
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

    #Move window on middle screen
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
        display_frame.pack(fill = "both", expand = True)
        self.eq_label = tk.Label(display_frame,text = "", font = ("Bebas Neue", 20), bg = "green", fg = "white")
        self.eq_label.place(relx = 1, x = 0, y = 0, anchor = "ne")
        self.eq2_label = tk.Label(display_frame, text ="", font = ('Bebas Neue', 35), bg = "yellow", fg = "black")
        self.eq2_label.place(relx = 0, x = 550, y = 120, anchor = "se")
        button_frame = tk.Frame(main_frame, width = 520, height = 400, bg = "#0F4C75")
        button_frame.pack(fill = 'both', expand = True)
        NonePhoto = tk.PhotoImage(width = 1, height = 1)
        #color #1B262C
        button_clearall = tk.Button(button_frame, text = "AC", font = ('Bebas Neue', 20), image = NonePhoto, compound = "c", width =140, height = 80, cursor = "hand2", command = lambda:self.button_pressed("AC", 0))
        button_clearall.grid(row = 0, column = 0, sticky = tk.W)
        self.controller.bind("<Shift_L> <BackSpace>", lambda event:self.button_pressed("AC", 0))
        button_clearone = tk.Button(button_frame, text = "CC", font = ('Bebas Neue', 20), image = NonePhoto, compound = "c", width =140, height = 80, cursor = "hand2", command = lambda:self.button_pressed("CC", 0))
        button_clearone.grid(row = 0, column = 1, stick = tk.W)
        self.controller.bind("<BackSpace>", lambda event: self.button_pressed("CC", 0))
        button_mod = tk.Button(button_frame, text = "%", font = ('Bebas Neue', 20), image = NonePhoto, compound = "c", width =140, height = 80, cursor = "hand2", command = lambda:self.button_pressed("%", 0))
        button_mod.grid(row = 0, column = 2, sticky = tk.W)
        self.controller.bind("%", lambda event: self.button_pressed("%", 0))
        button_div = tk.Button(button_frame, text = "/", font = ('Bebas Neue', 20), image = NonePhoto, compound = "c", width =100, height = 80, cursor = "hand2", command = lambda:self.button_pressed("/", 0))
        button_div.grid(row = 0, column = 3, sticky = tk.W)
        self.controller.bind("/", lambda event: self.button_pressed("/", 0))
        button_sev = tk.Button(button_frame, text = "7", font = ('Bebas Neue', 20), image = NonePhoto, compound = "c", width =140, height = 80, cursor = "hand2", command = lambda:self.button_pressed("Number", 7))
        button_sev.image = NonePhoto
        button_sev.grid(row = 1, column = 0)
        self.controller.bind("7", lambda event: self.button_pressed("Number", 7))
        button_eig = tk.Button(button_frame, text = "8", font = ('Bebas Neue', 20), image = NonePhoto, compound = "c", width =140, height = 80, cursor = "hand2", command = lambda:self.button_pressed("Number", 8))
        button_eig.grid(row = 1, column = 1)
        self.controller.bind("8", lambda event: self.button_pressed("Number", 6))
        button_nin = tk.Button(button_frame, text = "9", font = ('Bebas Neue', 20), image = NonePhoto, compound = "c", width =140, height = 80, cursor = "hand2", command = lambda:self.button_pressed("Number", 9))
        button_nin.grid(row = 1, column = 2)
        self.controller.bind("9", lambda event: self.button_pressed("Number", 9))
        button_mul = tk.Button(button_frame, text = "X", font = ('Bebas Neue', 20), image = NonePhoto, compound = "c", width =100, height = 80, cursor = "hand2", command = lambda:self.button_pressed("X", 0))
        button_mul.grid(row = 1, column = 3)
        self.controller.bind("*", lambda event: self.button_pressed("X", 0))
        button_fou = tk.Button(button_frame, text = "4", font = ('Bebas Neue', 20), image = NonePhoto, compound = "c", width =140, height = 80, cursor = "hand2", command = lambda:self.button_pressed("Number", 4))
        button_fou.grid(row = 2, column = 0)
        self.controller.bind("4", lambda event: self.button_pressed("Number", 4))
        button_fiv = tk.Button(button_frame, text = "5", font = ('Bebas Neue', 20), image = NonePhoto, compound = "c", width =140, height = 80, cursor = "hand2", command = lambda:self.button_pressed("Number", 5))
        button_fiv.grid(row = 2, column = 1)
        self.controller.bind("5", lambda event: self.button_pressed("Number", 5))
        button_six = tk.Button(button_frame, text = "6", font = ('Bebas Neue', 20), image = NonePhoto, compound = "c", width =140, height = 80, cursor = "hand2", command = lambda:self.button_pressed("Number", 6))
        button_six.grid(row = 2, column = 2)
        self.controller.bind("6", lambda event: self.button_pressed("Number", 6))
        button_min = tk.Button(button_frame, text = "-", font = ('Bebas Neue', 20), image = NonePhoto, compound = "c", width =100, height = 80, cursor = "hand2", command = lambda:self.button_pressed("-", -1))
        button_min.grid(row = 2, column = 3)
        self.controller.bind("-", lambda event: self.button_pressed("-", -1))
        button_one = tk.Button(button_frame, text = "1", font = ('Bebas Neue', 20), image = NonePhoto, compound = "c", width =140, height = 80, cursor = "hand2", command = lambda:self.button_pressed("Number", 1))
        button_one.grid(row = 3, column = 0)
        self.controller.bind("1", lambda event: self.button_pressed("Number", 1))
        button_two = tk.Button(button_frame, text = "2", font = ('Bebas Neue', 20), image = NonePhoto, compound = "c", width =140, height = 80, cursor = "hand2", command = lambda:self.button_pressed("Number", 2))
        button_two.grid(row = 3, column = 1)
        self.controller.bind("2", lambda event: self.button_pressed("Number", 2))
        button_thr = tk.Button(button_frame, text = "3", font = ('Bebas Neue', 20), image = NonePhoto, compound = "c", width =140, height = 80, cursor = "hand2", command = lambda:self.button_pressed("Number", 3))
        button_thr.grid(row = 3, column = 2)
        self.controller.bind("3", lambda event: self.button_pressed("Number", 3))
        button_plu = tk.Button(button_frame, text = "+", font = ('Bebas Neue', 20), image = NonePhoto, compound = "c", width =100, height = 80, cursor = "hand2", command = lambda:self.button_pressed("+", 0))
        button_plu.grid(row = 3, column = 3)
        self.controller.bind("+", lambda event: self.button_pressed("+", 0))
        button_next_pag = tk.Button(button_frame, text = ">>", font = ('Bebas Neue', 20), image = NonePhoto, compound = "c", width =140, height = 80, cursor = "hand2", command = lambda:self.button_pressed(">>", 0))
        button_next_pag.grid(row = 4, column = 0)
        button_zer = tk.Button(button_frame, text = "0", font = ('Bebas Neue', 20), image = NonePhoto, compound = "c", width =140, height = 80, cursor = "hand2", command = lambda:self.button_pressed("Number", 0))
        button_zer.grid(row = 4, column = 1)
        self.controller.bind("0", lambda event: self.button_pressed("Number", 0))
        button_dig = tk.Button(button_frame, text = ",", font = ('Bebas Neue', 20), image = NonePhoto, compound = "c", width =140, height = 80, cursor = "hand2", command = lambda:self.button_pressed(",", 0))
        button_dig.grid(row = 4, column = 2)
        self.controller.bind(",", lambda event: self.button_pressed(",", 0))
        button_ans = tk.Button(button_frame, text = "=", font = ('bebas Neue', 20), image = NonePhoto, compound = "c", width =100, height = 80, cursor = "hand2", command = lambda:self.button_pressed("=", 0))
        button_ans.grid(row = 4, column = 3)
        self.controller.bind("<Return>", lambda event: self.button_pressed("=", 0))
        
        #Global Variables
        global number_is, z , round_factor, second_operator, operator, number_two, number_one, btn_press, high_round_n1, high_round_n2
        second_operator = 0
        z = 1
        operator = 0 
        round_factor = 0
        number_is = 0
        high_round_n1 = 0
        high_round_n2 = 0
        btn_press = 0
        
        
    def button_pressed(self, button_type, number):
        #Global Variables
        global number_one, number_two, operator, btn_press, number_is, z, round_factor, second_operator, high_round_n1, high_round_n2
        
        #Create Number One
        if button_type == "Number" and number_is == 0:
            if btn_press == 0:
                number_one = number
                self.eq2_label.config(text = number_one)
                btn_press += 1
            elif btn_press == -1:
                z *= 10
                if len(str(number_one)) <=12:
                    round_factor += 1
                    high_round_n1 = round_factor
                    number_one = (number_one * z + number)/z
                    number_one = round(number_one, round_factor)
                    self.eq2_label.config(text = number_one)
                    print(f"Number one: {number_one}")

                else:
                    print("You cannot enter more than 15 characters!")
            else:
                if len(str(number_one)) <= 12:
                    number_one = number_one * 10 + number
                    self.eq2_label.config(text = number_one)
                else:
                    print("You cannot enter more than 15 characters!")
        
        #Verify operators when you press
        if button_type == "+" and btn_press != 0:
            operator = "+"
            number_is = 2
            self.eq2_label.config(text = str(number_one) +" "+ str(operator))
            second_operator = "+"
            btn_press = 0
            z = 1
            round_factor = 1
        if button_type == "-" and btn_press != 0:
            operator = "-"
            number_is = 2
            self.eq2_label.config(text = str(number_one) +" "+ str(operator))
            btn_press = 0
            second_operator = "-"
            z = 1
            round_factor = 1
        if button_type == "X" and btn_press != 0:
            operator = "X"
            number_is = 2
            self.eq2_label.config(text = str(number_one) +" "+ str(operator))
            btn_press = 0
            second_operator = "X"
            z = 1
            round_factor = 1
        if button_type == "/" and btn_press != 0:
            operator = "/"
            number_is = 2
            self.eq2_label.config(text = str(number_one) +" "+ str(operator))
            btn_press = 0 
            second_operator = "/"
            round_factor = 1
            z = 1
        if button_type == "%" and btn_press != 0:
            operator = "%"
            number_is = 2
            self.eq2_label.config(text = str(number_one) +" "+ str(operator))
            btn_press = 0
            second_operator = "%"
            round_factor = 1
            z = 1
        
        #Verify if you pres ','
        if button_type == "," and btn_press != 0:
            btn_press = -1
            operator = ","
        
        # Create Number Two
        if button_type == "Number" and number_is == 2:
            if btn_press == 0:
                number_two = number
                self.eq2_label.config(text = str(number_one) +" "+ str(second_operator) +" "+ str(number_two))
                btn_press += 1
            elif btn_press == -1:
                z *= 10
                if len(str(number_two)) <= 12:
                    round_factor +=1
                    high_round_n2 = round_factor
                    number_two = (number_two * z + number)/z
                    number_two = round(number_two, round_factor)
                    self.eq2_label.config(text = str(number_one) +" "+ str(second_operator) +" "+ str(number_two))
                    print(f"Number two: {number_two}")
                else:
                    print("You cannot enter more than 15 characters!")
            else:
                if len(str(number_two)) <= 12:
                    number_two = number_two * 10 + number
                    self.eq2_label.config(text = str(number_one) +" "+ str(operator) +" "+ str(number_two))
                else:
                    print("You cannot enter more than 15 characters!")
        
        
        # Buttons for Clear Character and Clear All
        if button_type == "AC":
            number_one = 0
            number_two = 0 
            btn_press = 0
            operator = ""
            number_is = 0
            z = 1
            self.eq2_label.config(text = "")
            second_operator = 0
        
        # Use 2 methods to remove a character from the number, first - when is int with // ;
        # second - when is float with a combination float(str()[:-1])

        if button_type == "CC":
            if number_is != 2:
                if operator == ',':
                    number_one = float(str(number_one)[:-1])
                    z = z/10
                    self.eq2_label.config(text = number_one)
                else:
                    number_one = number_one // 10
                    self.eq2_label.config(text = number_one)
                print(number_one)
            else:
                if operator == ',':
                    number_two = float(str(number_two)[:-1])
                    self.eq2_label.config(text = str(number_one) +" "+ str(second_operator) +" "+ str(number_two))
                    z = z/10
                else:
                    number_two = number_two // 10
                    self.eq2_label.config(text = str(number_one) +" "+ str(second_operator) +" "+ str(number_two))

        #Verify conditions for equal
        if button_type == "=" and btn_press != 0:
            if operator == "+":
                display = number_one + number_two
                final_ec = str(number_one)+" "+str(operator)+" "+str(number_two)+" "+"="+" "+ str(display)
                self.eq2_label.config(text = display)
            if operator == "-":
                display = number_one - number_two
                final_ec = str(number_one)+" "+str(operator)+" "+str(number_two)+" "+"="+" "+ str(display)
                self.eq2_label.config(text = display)
            if operator == "X":
                display = number_one * number_two
                final_ec = str(number_one)+" "+str(operator)+" "+str(number_two)+" "+"="+" "+ str(display)
                self.eq2_label.config(text = display)
            if operator == "/":
                display = number_one / number_two
                final_ec = str(number_one)+" "+str(operator)+" "+str(number_two)+" "+"="+" "+ str(display)
                self.eq2_label.config(text = display)
            if operator == "%":
                display = number_one % number_two
                final_ec = str(number_one)+" "+str(operator)+" "+str(number_two)+" "+"="+" "+ str(display)
                self.eq2_label.config(text = display)
            
            #Verify equal when a number is float, and round up after the longest
            if operator == ',' and second_operator == "+":
                display = number_one + number_two
                if high_round_n1 > high_round_n2:
                  display = round(display, high_round_n1)
                  final_ec = str(number_one)+" "+str(second_operator)+" "+str(number_two)+" "+"="+" "+ str(display)
                  self.eq2_label.config(text = display)
                else:
                    display = round(display, high_round_n2)
                    final_ec = str(number_one)+" "+str(second_operator)+" "+str(number_two)+" "+"="+" "+ str(display)
                    self.eq2_label.config(text = display)
            if operator == ',' and second_operator == "-":
                display = number_one - number_two
                if high_round_n1 > high_round_n2:
                  display = round(display, high_round_n1)
                  final_ec = str(number_one)+" "+str(second_operator)+" "+str(number_two)+" "+"="+" "+ str(display)
                  self.eq2_label.config(text = display)
                else:
                    display = round(display, high_round_n2)
                    final_ec = str(number_one)+" "+str(second_operator)+" "+str(number_two)+" "+"="+" "+ str(display)
                    self.eq2_label.config(text = display)
            if operator == ',' and second_operator == "X":
                display = number_one * number_two
                if high_round_n1 > high_round_n2:
                  display = round(display, high_round_n1)
                  final_ec = str(number_one)+" "+str(second_operator)+" "+str(number_two)+" "+"="+" "+ str(display)
                  self.eq2_label.config(text = display)
                else:
                    display = round(display, high_round_n2)
                    final_ec = str(number_one)+" "+str(second_operator)+" "+str(number_two)+" "+"="+" "+ str(display)
                    self.eq2_label.config(text = display)
            if operator == ',' and second_operator == "/":
                display = number_one / number_two
                if high_round_n1 > high_round_n2:
                  display = round(display, high_round_n1)
                  final_ec = str(number_one)+" "+str(second_operator)+" "+str(number_two)+" "+"="+" "+ str(display)
                  self.eq2_label.config(text = display)
                else:
                    display = round(display, high_round_n2)
                    final_ec = str(number_one)+" "+str(second_operator)+" "+str(number_two)+" "+"="+" "+ str(display)
                    self.eq2_label.config(text = display)
            if operator == ',' and second_operator == "%":
                display = number_one % number_two
                if high_round_n1 > high_round_n2:
                  display = round(display, high_round_n1)
                  final_ec = str(number_one)+" "+str(second_operator)+" "+str(number_two)+" "+"="+" "+ str(display)
                  self.eq2_label.config(text = display)
                else:
                    display = round(display, high_round_n2)
                    final_ec = str(number_one)+" "+str(second_operator)+" "+str(number_two)+" "+"="+" "+ str(display)
                    self.eq2_label.config(text = display)
            
            #Reset Variables
            btn_press = 0
            number_one = 0
            number_two = 0
            number_is = 0
            z = 1 
            second_operator = 0
            self.eq_label.config(text = final_ec)

            #Check if variables is fine.
            print(display)
            print(final_ec)

if __name__ == "__main__":
    app = MainApp()
    app.mainloop()