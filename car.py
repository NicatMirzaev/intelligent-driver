import pygame
import math

class Car:
    def __init__(self, x, y, angle):
        self.x = x
        self.y = y
        self.angle = angle
        self.image = pygame.image.load("car.png");

    def draw(self, screen):
        rotated_image = pygame.transform.rotate(self.image, self.angle)
        screen.blit(rotated_image, rotated_image.get_rect(center=self.image.get_rect(topleft=(self.x, self.y)).center).topleft)

    def speedUp(self):

        targetX = self.x + math.cos(math.radians(self.angle))
        targetY = self.y - math.sin(math.radians(self.angle))

        if targetX >= 30 and targetX <= 916 and targetY >= 30 and targetY <= 507:
            self.x = targetX
            self.y = targetY

    def speedDown(self):

        targetX = self.x - math.cos(math.radians(self.angle))
        targetY = self.y + math.sin(math.radians(self.angle))

        if targetX >= 30 and targetX <= 950 and targetY >= 30 and targetY <= 935:
            self.x = targetX
            self.y = targetY

    def moveRight(self):
        self.angle -= 1
        if self.angle == -359:
            self.angle = 0

    def moveLeft(self):
        self.angle += 1
        if self.angle == 359:
            self.angle = 0