import sys, pygame
from button import Button
from car import Car
import json

# init pygame
pygame.init()

# Constant Variables
width = 1000 # width of the window
height = 600 # height of the window
board_width = width-50 # width of the board
board_height = height-65 # height of the board
board_x = 30
board_y = 20
GAME_MODE_MENU = 1 # game mode menu
GAME_MODE_DRAW = 2 # game mode draw
GAME_MODE_PLAY = 3 # game mode play
GAME_MODE_STARTED = 4 # game mode started
clock = pygame.time.Clock()

# Variables
buttons = [Button("PLAY", (255, 255, 255), (width / 2) - 70, (height / 2) - 120, 140, 40, (100,100,100), 1), Button("DRAW", (255, 255, 255), (width / 2) - 70, (height / 2) , 140, 40, (100, 100, 100), 2)]
GAME_MODE = GAME_MODE_MENU
board = []
car = None
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Intelligent Driver (Coded By Nicat)")

# Game Loop
run = True
while run:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        if event.type == pygame.MOUSEBUTTONDOWN:
            x, y = pygame.mouse.get_pos()
            for button in buttons:
                if button.isClicked(x, y):
                    if button.type == 1:
                      GAME_MODE = GAME_MODE_PLAY
                      buttons = [Button("START", (255, 255, 255), (width / 2) - 120, height - 38, 140, 30, (100,100,100), 5)]
                      board = []

                    elif button.type == 2:
                        GAME_MODE = GAME_MODE_DRAW
                        buttons = [Button("SAVE", (255, 255, 255), (width / 2) - 120, height - 38, 140, 30, (100,100,100), 3), Button("LOAD", (255, 255, 255), (width / 2) + 100, height - 38, 140, 30, (100,100,100), 4)]
                        board = []

                    elif button.type == 3:
                        with open("data.json", "w") as f:
                            json.dump(board, f)

                    elif button.type == 4:
                        try:
                            with open("data.json", "r") as f:
                                board = json.load(f)
                        except Exception as e:
                            print(e)

                    elif button.type == 5:
                        with open("data.json", "r") as f:
                            board = json.load(f)

                        if len(board) <= 0:
                            print("You must draw something.")
                        else:
                            car = Car(board_x + 10, board_y + 10, 0)
                            GAME_MODE = GAME_MODE_STARTED
                            


    screen.fill((255, 255, 255))

    if GAME_MODE == GAME_MODE_DRAW:
        pygame.draw.rect(screen, (0, 0, 0), (board_x, board_y, board_width, board_height), 5)
        for i in board:
            pygame.draw.rect(screen, (0, 0, 0), (i[0], i[1], 25, 25), 0)

        click = pygame.mouse.get_pressed()
        if click[0]:
            x, y = pygame.mouse.get_pos()
            if x >= board_x and x <= board_width and y >= board_y and y <= board_height:
                if [x, y] not in board:
                    board.append([x, y])
        elif click[2]:
            x, y = pygame.mouse.get_pos()
            for rect in board:
                if x >= rect[0] and x <= rect[0] + 25 and y >= rect[1] and y <= rect[1] + 25:
                    board.remove(rect)

    elif GAME_MODE == GAME_MODE_PLAY or GAME_MODE_STARTED:
        pygame.draw.rect(screen, (0, 0, 0), (board_x, board_y, board_width, board_height), 5)
        if GAME_MODE == GAME_MODE_STARTED:

            keys = pygame.key.get_pressed()

            if keys[pygame.K_w]:
                car.speedUp()
            if keys[pygame.K_s]:
                car.speedDown()
            if keys[pygame.K_d]:
                car.moveRight()
            if keys[pygame.K_a]:
                car.moveLeft()

            for i in board:
                pygame.draw.rect(screen, (0, 0, 0), (i[0], i[1], 25, 25), 0)

            car.draw(screen)


    for button in buttons:
        button.draw(screen)

    pygame.display.update()


sys.exit()
