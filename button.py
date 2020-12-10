import pygame

class Button:

    def __init__(self, text, text_color, x, y, width, height, color, type):
        self.x = x
        self.y = y
        self.color = color
        self.width = width
        self.height = height
        self.font = pygame.font.SysFont('Corbel', 35)
        self.text = self.font.render(text, True, text_color)
        self.type = type

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, [self.x, self.y, self.width, self.height])
        screen.blit(self.text, (self.x + 30, self.y))

    def isClicked(self, x, y):
        if x >= self.x and x <= self.x + self.width and y >= self.y and y <= self.y + self.height:
            return True
        return False