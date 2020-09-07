import tkinter as tk
from calculations import Cal


class CalulatorWindow:
    length = 20
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Calculator")
        self.window.geometry("600x600")
        self.operator = ["+", "-", "*", "/", "**", "!", "%"]
        self.text = ""
        self.font_size = (None, 30)

    def keypress(self):
        self.window.bind("<Key>", self.get_number)

    def get_number(self, num):
        # num can be a number or a operator or someother keyboard presses
        is_operator = False
        if num == "EXE":
            pass
        elif str(num).isnumeric():
            self.update_display(num)
        elif num in self.operator:
            is_operator = True
        else:
            key = str(num.char)
            if key.isnumeric():
                self.get_number(key)
            elif key in self.operator:
                is_operator = True
        if is_operator:
            pass
    def reset(self):
        self.text = ""

    def operator_pad(self):
        number_pad_bg_color = "black"
        number_pad_fg_color = "white"
        size_x, size_y = (6, 3)
        buttom_operator = 0.725
        tk.Button(self.window, text="EXE", bg=number_pad_bg_color, fg=number_pad_fg_color, height=size_y,
                  width=int(size_x * 2.5), command=lambda: self.get_number("EXE")).place(relx=0.7, rely=buttom_operator + 0.1)
        tk.Button(self.window, text="+", bg=number_pad_bg_color, fg=number_pad_fg_color, height = size_y,
                  width = size_x, command=lambda: self.get_number("+")).place(relx=0.7, rely = buttom_operator)
        tk.Button(self.window, text="-", bg=number_pad_bg_color, fg=number_pad_fg_color, height=size_y,
                  width=size_x, command=lambda: self.get_number("-")).place(relx=0.8, rely=buttom_operator)
        tk.Button(self.window, text="x", bg=number_pad_bg_color, fg=number_pad_fg_color, height=size_y,
                  width=size_x, command=lambda: self.get_number("x")).place(relx=0.7, rely=buttom_operator - 0.1)
        tk.Button(self.window, text="/", bg=number_pad_bg_color, fg=number_pad_fg_color, height=size_y,
                  width=size_x, command=lambda: self.get_number("/")).place(relx=0.8, rely=buttom_operator - 0.1)
        tk.Button(self.window, text="!", bg=number_pad_bg_color, fg=number_pad_fg_color, height=size_y,
                  width=size_x, command=lambda: self.get_number("!")).place(relx=0.7, rely=buttom_operator - 0.2)
        tk.Button(self.window, text="%", bg=number_pad_bg_color, fg=number_pad_fg_color, height=size_y,
                  width=size_x, command=lambda: self.get_number("%")).place(relx=0.8, rely=buttom_operator - 0.2)

    def number_pad(self):

        number_pad_bg_color = "black"
        number_pad_fg_color = "gray"

        size_x, size_y = (6, 4)
        tk.Button(self.window, text=1, bg=number_pad_bg_color,
                  fg=number_pad_fg_color, height=size_y, width=size_x,
                  command=lambda: self.get_number(1)).place(relx=0.15 * (1 + (7 - 1) % 3 * 0.75),
                                                       rely=0.5 + 0.15 * ((7 - 1) // 3))
        tk.Button(self.window, text=2, bg=number_pad_bg_color,
                  fg=number_pad_fg_color, height=size_y, width=size_x,
                  command=lambda: self.get_number(2)).place(relx=0.15 * (1 + (8 - 1) % 3 * 0.75),
                                                       rely=0.5 + 0.15 * ((8 - 1) // 3))
        tk.Button(self.window, text=3, bg=number_pad_bg_color,
                  fg=number_pad_fg_color, height=size_y, width=size_x,
                  command=lambda: self.get_number(3)).place(relx=0.15 * (1 + (9 - 1) % 3 * 0.75),
                                                       rely=0.5 + 0.15 * ((9 - 1) // 3))
        tk.Button(self.window, text=4, bg=number_pad_bg_color,
                  fg=number_pad_fg_color, height=size_y, width=size_x,
                  command=lambda: self.get_number(4)).place(relx=0.15 * (1 + (4 - 1) % 3 * 0.75),
                                                       rely=0.5 + 0.15 * ((4 - 1) // 3))
        tk.Button(self.window, text=5, bg=number_pad_bg_color,
                  fg=number_pad_fg_color, height=size_y, width=size_x,
                  command=lambda: self.get_number(5)).place(relx=0.15 * (1 + (5 - 1) % 3 * 0.75),
                                                       rely=0.5 + 0.15 * ((5 - 1) // 3))
        tk.Button(self.window, text=6, bg=number_pad_bg_color,
                  fg=number_pad_fg_color, height=size_y, width=size_x,
                  command=lambda: self.get_number(6)).place(relx=0.15 * (1 + (6 - 1) % 3 * 0.75),
                                                       rely=0.5 + 0.15 * ((6 - 1) // 3))
        tk.Button(self.window, text=7, bg=number_pad_bg_color,
                  fg=number_pad_fg_color, height=size_y, width=size_x,
                  command=lambda: self.get_number(7)).place(relx=0.15 * (1 + (1 - 1) % 3 * 0.75),
                                                       rely=0.5 + 0.15 * ((1 - 1) // 3))
        tk.Button(self.window, text=8, bg=number_pad_bg_color,
                  fg=number_pad_fg_color, height=size_y, width=size_x,
                  command=lambda: self.get_number(8)).place(relx=0.15 * (1 + (2 - 1) % 3 * 0.75),
                                                       rely=0.5 + 0.15 * ((2 - 1) // 3))
        tk.Button(self.window, text=9, bg=number_pad_bg_color,
                  fg=number_pad_fg_color, height=size_y, width=size_x,
                  command=lambda: self.get_number(9)).place(relx=0.15 * (1 + (3 - 1) % 3 * 0.75),
                                                       rely=0.5 + 0.15 * ((3 - 1) // 3))

    def main(self):
        self.keypress()
        self.number_pad() # creates number pad with clickable buttons
        self.operator_pad()
        self.window.mainloop()

    def update_display(self, num):
        self.text += str(num)
        tk.Label(self.window, font = self.font_size, text=" " * (self.length - len(self.text)) + self.text, bg="black", fg="white").place(relx=0.2, rely=0.2)


CalulatorWindow().main()