import pygame
import math

class RayCast:

    def __init__(self, x, y, angle, length, direction):
        self.x = x
        self.y = y
        self.angle = angle
        self.length = length
        self.direction = direction

    def draw(self, screen):
        if self.direction == 1:
            endX = self.x + (self.length * math.cos(math.radians(self.angle)))
            endY = self.y - (self.length * math.sin(math.radians(self.angle)))
            pygame.draw.line(screen, pygame.Color("red"), (self.x, self.y), (endX, endY), 2)

        elif self.direction == 2:
            endX = self.x + (self.length * math.cos(math.radians(self.angle + 90)))
            endY = self.y - (self.length * math.sin(math.radians(self.angle + 90)))

            pygame.draw.line(screen, pygame.Color("red"), (self.x, self.y), (endX, endY), 2)

        elif self.direction == 3:
            endX = self.x + (self.length * math.cos(math.radians(self.angle - 90)))
            endY = self.y - (self.length * math.sin(math.radians(self.angle - 90)))

            pygame.draw.line(screen, pygame.Color("red"), (self.x, self.y), (endX, endY), 2)

    def collectData(self, barriers):
        if self.direction == 1:
            for i in range(1, self.length):
                x = self.x + (i * math.cos(math.radians(self.angle)))
                y = self.y - (i * math.sin(math.radians(self.angle)))
                for barrier in barriers:
                    if x >= barrier[0] and x <= barrier[0] + 25 and y >= barrier[1] and y <= barrier[1] + 25:
                        dist = math.sqrt((x - self.x) ** 2 + (y - self.y) ** 2)
                        return (x, y, dist, 0)

                if x <= 30 or x >= 916 or y <= 20 or y >= 540:
                    dist = math.sqrt((x - self.x) ** 2 + (y - self.y) ** 2)
                    return (x, y, dist, 1)

            return -1

        elif self.direction == 2:
            for i in range(0, self.length):
                x = self.x + (i * math.cos(math.radians(self.angle + 90)))
                y = self.y - (i * math.sin(math.radians(self.angle + 90)))
                for barrier in barriers:
                    if x >= barrier[0] and x <= barrier[0] + 25 and y >= barrier[1] and y <= barrier[1] + 25:
                        dist = math.sqrt((x - self.x) ** 2 + (y - self.y) ** 2)
                        return (x, y, dist, 0)

                if x <= 30 or x >= 916 or y <= 20 or y >= 540:
                    dist = math.sqrt((x - self.x) ** 2 + (y - self.y) ** 2)
                    return (x, y, dist, 1)
            return -1

        elif self.direction == 3:
            for i in range(0, self.length):
                x = self.x + (i * math.cos(math.radians(self.angle - 90)))
                y = self.y - (i * math.sin(math.radians(self.angle - 90)))
                for barrier in barriers:
                    if x >= barrier[0] and x <= barrier[0] + 25 and y >= barrier[1] and y <= barrier[1] + 25:
                        dist = math.sqrt((x - self.x) ** 2 + (y - self.y) ** 2)
                        return (x, y, dist, 0)

                if x <= 30 or x >= 916 or y <= 20 or y >= 540:
                    dist = math.sqrt((x - self.x) ** 2 + (y - self.y) ** 2)
                    return (x, y, dist, 1)
            return -1

