from words_file import WordFile
import pygame
import sys
import random
class Settings:
    def __init__(self):
        self.window_width = 800
        self.window_hight = 600

        self.colors = {"BLACK": (0, 0, 0), "WHITE": (224, 224, 244), "ORANGE": (250, 145, 8), "GREEN": (58, 203, 58)}
        self.text_size = 40
        self.text_style = "Calibri"

        self.all_words = WordFile().read_content().split()
        #print(self.all_words)
        self.amount_words = 100

        self.clock = pygame.time.Clock()
        self.fps = 100

class TypeRacer(Settings):
    def __init__(self):
        super().__init__()
        self.screen = pygame.display.set_mode((self.window_width, self.window_hight))
        self.running = False
        # text
        pygame.font.init()
        self.myfont = pygame.font.SysFont(self.text_style, self.text_size)
        self.text_position = 0

    def reset(self):
        list_words = self.get_random_words() # length of words = self.amount_words


        self.fit = (self.window_width // self.text_size) * 2
        self.words = " " * (self.fit // 2) +  " ".join(list_words) # have space in the begginning
        self.length_words = len(self.words)
        self.running = True
        self.current_key = " "


    def main(self):

        self.reset()
        while self.running:
            self.handle_event()
            self.display() # last
            self.clock.tick(self.fps)
    def display(self):
        self.screen.fill(self.colors["BLACK"])
        self.display_text()

        pygame.display.update()

    def display_text(self):
        end_pos = self.text_position + self.fit + 15

        if end_pos > self.length_words:
            end_pos = self.length_words
        if self.text_position == end_pos:
            self.running = False
        text = self.words[self.text_position:end_pos]

        self.current_key = text[self.fit // 2]
        textsurface = self.myfont.render(text, False, self.colors["WHITE"], self.colors["BLACK"])
        self.screen.blit(textsurface, (50, 200))

    def start_typing(self):
        pass

    def handle_event(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == ord(self.current_key):
                    self.text_position += 1
        # key = pygame.key.get_pressed()
        # if key[pygame.K_SPACE]:
        #     self.text_position += 1

    def get_random_words(self):
        return random.choices(self.all_words, k = self.amount_words)



if __name__ == "__main__":
    TypeRacer().main()