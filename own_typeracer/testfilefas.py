import pygame

screen = pygame.display.set_mode((100, 100))
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            print(event.key)
