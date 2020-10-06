from own_typeracer import whole_text_pyfile
import pygame
import sys
import random
class Settings:
    def __init__(self):
        self.window_width = 1800
        self.window_hight = 700

        self.colors = {"BLACK": (0, 0, 0), "WHITE": (224, 224, 244), "ORANGE": (250, 145, 8), "GREEN": (58, 203, 58),
                       "DARK_GRAY": (89, 101, 139), "LIGHT_GRAY": (202, 205, 216), "GRAY": (64, 64, 64)}
        font_change = 5 / 3
        self.your_text_size = 50
        self.text_size = int(self.your_text_size * font_change)# the font you want * the font_change will give you the right font size
        self.letter_fit_screen = int(self.window_width / self.your_text_size)
        self.center_letter_width = self.letter_fit_screen // 2
        self.text_style = "monospace"

        #self.all_words = WordFile().read_content().split()
        self.all_words = whole_text_pyfile.words
        #print(self.all_words)
        self.amount_words = 100

        self.clock = pygame.time.Clock()
        self.fps = 100

        self.space_ascii = 32
        self.move_back = 0
        self.animation = False

        self.numbers_with_shift = {"1" : "!", "2": "\"", "3": "#", "4": "¤", "5": "%", "6":"&", "7":"/", "8":"(","9":")", "0":"="}
        # uk keyboard to swedish translation
        self.special_character_convergence = {"-": "+", ";":"ö","\'":"ä", "[":"å","\\":"\'","/":"-"}
class TypeRacer(Settings):
    def __init__(self):
        super().__init__()
        self.screen = pygame.display.set_mode((self.window_width, self.window_hight))
        self.running = False
        # text
        pygame.font.init()
        self.myfont = pygame.font.SysFont(self.text_style, self.text_size)
        self.text_position = self.center_letter_width
    def reset(self):

        self.running = True
        self.current_key = " "
        previous_words = " " * self.center_letter_width  # the previous words in the beginning are empty (only spaces)
        self.words = previous_words + " ".join(self.all_words)
    def main(self):
        self.reset()
        while self.running:
            self.handle_event()
            self.display() # last
            self.clock.tick(self.fps)

    def display(self):
        self.screen.fill(self.colors["DARK_GRAY"])
        self.display_text()
        pygame.display.update()

    def display_text(self):
        #display previous words
        previous_textsurface = self.myfont.render(self.words[self.text_position - self.center_letter_width : self.text_position], False, self.colors["GRAY"], self.colors["DARK_GRAY"])

        #display current letter
        self.current_key = self.words[self.text_position]
        current_textsurface = self.myfont.render(self.current_key, False, self.colors["GREEN"], self.colors["WHITE"])

        #display next words
        next_textsurface = self.myfont.render(self.words[self.text_position + 1 : self.text_position + self.center_letter_width], False, self.colors["LIGHT_GRAY"], self.colors["DARK_GRAY"])

        if self.animation:
            self.move_back += int(self.your_text_size / 4)
            if self.move_back >= self.your_text_size:
                self.animation = False

        self.screen.blit(previous_textsurface, (0 - self.move_back, 200))
        self.screen.blit(current_textsurface, (self.center_letter_width * self.your_text_size - self.move_back, 200))
        self.screen.blit(next_textsurface, ((self.center_letter_width + 1) * self.your_text_size - self.move_back, 200))

    def start_typing(self):
        pass

    def handle_event(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.KEYDOWN:
                key = pygame.key.get_pressed()


                if key[ord(self.current_key.lower())] or (event.key == 92):
                    # ascii number for / is 92 but is at the position of '
                    # the postion of ' on a swedish keyboard gives /
                    
                    if (key[303] or key[304]):

                        if self.current_key.islower():
                            break
                    else:
                        # check if upper
                        if self.current_key.isupper():
                            break

                    # right key pressed
                    self.move_back = 0
                    self.animation = True
                    self.text_position += 1

                if event.key == pygame.K_BACKSPACE:
                    self.text_position -= 1

if __name__ == "__main__":
    TypeRacer().main()