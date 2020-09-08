import tkinter as tk
from time import time
from math import floor
class Settings:
    def __init__(self):
        self.screen_width = 800
        self.screen_height = 600

        # self.time_width = round(150 * self.px_to_text_unit_x)
        # self.time_height = round(120 * self.px_to_text_unit_y / 2)

        self.time_font = 30
        self.button_font = 10
        self.button_width = 000 #TODO Come up with width
        self.button_height = 60


        self.space_width = 30 #* self.px_to_text_unit_x
        self.space_height = 100 #* self.px_to_text_unit_y

        self.title_font = 20
        self.title_height = round(self.space_height / 2)

        self.colors = {"BLACK": (0, 0, 0), "WHITE": (255, 255, 255)}

class HandleTime:

    def __init__(self):
        # create variables accessble to all methods
        self.initial_time = time()
        # the timer will always be stopped at first
        self.stop = True
        self.text_stop_start = " Start "
        self.display_time = "00:00:00"
        self.show_seconds = 0
        self.stop_seconds = 0

    def start_stop_time(self):
        if self.stop:
            self.initial_time = time()
        else: # the timer was on
            self.stop_seconds = self.show_seconds
        # create a switch each time this method is used
        self.stop = not self.stop
        if self.stop:
            self.text_stop_start = " Start "
        else:
            self.text_stop_start = "Stop"

    def time_tracker(self):
        if not self.stop:
            # the timer is on
            self.show_seconds = floor(time() - self.initial_time) + self.stop_seconds
            self.display_time = f"00:00:{self.show_seconds}"

    def reset_time(self):
        self.stop = True

    @staticmethod
    def reset_all():
        # This method will the time of all objects assosiabed with the time class
        pass

class Timer(Settings):

    def __init__(self):
        super().__init__()

        self.screen = tk.Tk()
        self.screen.configure(background="lightblue")
        self.screen.geometry(f"{self.screen_width}x{self.screen_height}")
        self.seconds = 0
        self.minutes = 0

        #   1   2   3
        #   4   5   6
        # create 6 objects of the class HandleTime
        self.handle_time1 = HandleTime()
        self.handle_time2 = HandleTime()
        self.handle_time3 = HandleTime()
        self.handle_time4 = HandleTime()
        self.handle_time5 = HandleTime()
        self.handle_time6 = HandleTime()

        self.display_time = "00:00:00"

    def update(self):

        self.manage()
        self.configure_display()
        self.screen.after(500, self.update)

    def main(self):
        self.display()
        self.update()
        #tk.Label(self.screen, text="adfsd").place(relx = 0.1, rely= 0.1)
        self.screen.mainloop()

    def manage(self):
        self.handle_time1.time_tracker()
        self.handle_time2.time_tracker()
        self.handle_time3.time_tracker()
        self.handle_time4.time_tracker()
        self.handle_time5.time_tracker()
        self.handle_time6.time_tracker()

    def configure_display(self):
        self.b1_start_stop.config(text=self.handle_time1.text_stop_start)
        self.l1_timer.config(text=self.handle_time1.display_time)

    def display(self):
        # time box and button box for upper row
        each_cell_width = self.screen_width // 3
        each_cell_height = self.screen_height // 2
        font_multiplier = 2.5
        # 1.
        self.b1_start_stop = tk.Button(self.screen, bg="lightgreen", fg="white", text=self.handle_time1.text_stop_start,
                  font=(None, self.button_font),
                  command=self.handle_time1.start_stop_time)
        self.b1_start_stop.place(x=self.space_width, y=self.space_height + round(
            self.time_font * font_multiplier))
        self.b1_reset = tk.Button(self.screen, bg="lightgreen", fg="white", text="Reset", font=(None, self.button_font))
        self.b1_reset.place(x=self.space_width + self.time_font * 3,
                            y=self.space_height + round(self.time_font * font_multiplier))
        self.l1_timer = tk.Label(self.screen, bg="lightgreen", fg="white",
                                text=self.handle_time1.display_time, font=(None, self.time_font))
        self.l1_timer.place(x=self.space_width, y=self.space_height)

        tk.Label(self.screen, bg="lightgreen", fg="white",
                 text="Communication", font=(None, self.title_font)).place(x=self.space_width, y=self.title_height)

        # 2.
        tk.Label(self.screen, bg="lightgreen", fg="white",
                 text="Homework", font=(None, self.title_font)).place(x=self.space_width + each_cell_width, y=self.title_height)
        tk.Label(self.screen, bg="lightgreen", fg="white",
                 text=self.display_time, font=(None, self.time_font)).place(x=self.space_width + each_cell_width, y=self.space_height)
        tk.Button(self.screen, bg="lightgreen", fg="white", text=" Start "
                  , font=(None, self.button_font)).place(x=self.space_width + each_cell_width, y=self.space_height + round(self.time_font * font_multiplier))
        tk.Button(self.screen, bg="lightgreen", fg="white", text="Reset",
                  font=(None, self.button_font)).place(x=self.space_width + self.time_font * 3 + each_cell_width,
                                                       y=self.space_height + round(self.time_font * font_multiplier))
        # 3.
        tk.Label(self.screen, bg="lightgreen", fg="white",
                 text="Chinese", font=(None, self.title_font)).place(x=self.space_width + each_cell_width * 2, y=self.title_height)
        tk.Label(self.screen, bg="lightgreen", fg="white",
                 text=self.display_time, font=(None, self.time_font)).place(x=self.space_width + each_cell_width * 2, y=self.space_height)
        tk.Button(self.screen, bg="lightgreen", fg="white", text=" Start "
                  , font=(None, self.button_font)).place(x=self.space_width + each_cell_width * 2, y=self.space_height + round(self.time_font * font_multiplier))
        tk.Button(self.screen, bg="lightgreen", fg="white", text="Reset",
                  font=(None, self.button_font)).place(x=self.space_width + self.time_font * 3 + each_cell_width * 2,
                                                       y=self.space_height + round(self.time_font * font_multiplier))

        # bottom row
        # 4.
        tk.Label(self.screen, bg="lightgreen", fg="white",
                 text="LearnC++", font=(None, self.title_font)).place(x=self.space_width, y=self.title_height + each_cell_height)
        tk.Label(self.screen, bg="lightgreen", fg="white",
                 text=self.display_time, font=(None, self.time_font)).place(x=self.space_width, y=self.space_height + each_cell_height)
        tk.Button(self.screen, bg="lightgreen", fg="white", text=" Start "
                  , font=(None, self.button_font)).place(x=self.space_width, y=self.space_height + round(self.time_font * font_multiplier) + each_cell_height)
        tk.Button(self.screen, bg="lightgreen", fg="white", text="Reset",
                  font=(None, self.button_font)).place(x=self.space_width + self.time_font * 3,
                                                       y=self.space_height + round(self.time_font * font_multiplier) + each_cell_height)
        # 5.
        tk.Label(self.screen, bg="lightgreen", fg="white",
                 text="Programming", font=(None, self.title_font)).place(x=self.space_width + each_cell_width, y=self.title_height + each_cell_height)
        tk.Label(self.screen, bg="lightgreen", fg="white",
                 text=self.display_time, font=(None, self.time_font)).place(x=self.space_width + each_cell_width, y=self.space_height + each_cell_height)
        tk.Button(self.screen, bg="lightgreen", fg="white", text=" Start "
                  , font=(None, self.button_font)).place(x=self.space_width + each_cell_width,
                                                         y=self.space_height + round(self.time_font * font_multiplier) + each_cell_height)
        tk.Button(self.screen, bg="lightgreen", fg="white", text="Reset",
                  font=(None, self.button_font)).place(x=self.space_width + self.time_font * 3 + each_cell_width,
                                                       y=self.space_height + round(self.time_font * font_multiplier) + each_cell_height)
        # 6.
        tk.Label(self.screen, bg="lightgreen", fg="white",
                 text="Other", font=(None, self.title_font)).place(x=self.space_width + each_cell_width * 2, y=self.title_height + each_cell_height)
        tk.Label(self.screen, bg="lightgreen", fg="white",
                 text=self.display_time, font=(None, self.time_font)).place(x=self.space_width + each_cell_width * 2, y=self.space_height + each_cell_height)
        tk.Button(self.screen, bg="lightgreen", fg="white", text=" Start "
                  , font=(None, self.button_font)).place(x=self.space_width + each_cell_width * 2,
                                                         y=self.space_height + round(self.time_font * font_multiplier) + each_cell_height)
        tk.Button(self.screen, bg="lightgreen", fg="white", text="Reset",
                  font=(None, self.button_font)).place(x=self.space_width + self.time_font * 3 + each_cell_width * 2,
                                                       y=self.space_height + round(self.time_font * font_multiplier) + each_cell_height)

        # all reset
        tk.Button(self.screen, bg="lightgreen", fg="white", text="Reset All", font=(None, self.button_font * 2)).place(relx=0.4, rely=0.4)

if __name__ == "__main__":
    Timer().main()