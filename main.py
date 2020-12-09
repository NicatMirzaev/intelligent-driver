import sys, pygame
from button import Button

# init pygame
pygame.init()

# Constant Variables
width = 1000 # width of the window
height = 600 # height of the window
GAME_MODE_MENU = 1 # game mode menu
GAME_MODE_DRAW = 2 # game mode draw
GAME_MODE_PLAY = 3 # game mode play

# Variables
buttons = [Button("PLAY", (255, 255, 255), (width / 2) - 70, (height / 2) - 120, 140, 40, (100,100,100), 1), Button("DRAW", (255, 255, 255), (width / 2) - 70, (height / 2) , 140, 40, (100, 100, 100), 2)]
GAME_MODE = GAME_MODE_MENU

screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Intelligent Driver (Coded By Nicat)")

# Game Loop
run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        if event.type == pygame.MOUSEBUTTONDOWN:
            x, y = pygame.mouse.get_pos()
            for button in buttons:
                if button.isClicked(x, y):
                    print("Clicked to: ", button.type)

    screen.fill((255, 255, 255))

    for button in buttons:
        button.draw(screen)

    pygame.display.update()


sys.exit()