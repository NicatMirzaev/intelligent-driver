import pygame
from raycast import RayCast
import math
import random

CAR_STATUS_DRIVE = 1
CAR_STATUS_GO_LEFT = 2
CAR_STATUS_GO_RIGHT = 3

class Car:
    def __init__(self, x, y, angle):
        self.x = x
        self.y = y
        self.status = CAR_STATUS_DRIVE
        self.angle = angle
        self.dist = 70
        self.image = pygame.image.load("car.png");
        self.raycasts = [RayCast(x, y, angle, 100, 1), RayCast(x, y, angle, 100, 2),  RayCast(x, y, angle, 100, 3)]

    def draw(self, screen):
        rotated_image = pygame.transform.rotate(self.image, self.angle)
        screen.blit(rotated_image, rotated_image.get_rect(center=self.image.get_rect(topleft=(self.x, self.y)).center).topleft)

        for raycast in self.raycasts:
            raycast.x = self.x + self.image.get_rect().center[0]
            raycast.y = self.y + self.image.get_rect().center[1]
            raycast.angle = self.angle
            raycast.draw(screen)

    def update(self, board):
        if self.status == CAR_STATUS_DRIVE:
            self.speedUp()
            data = self.raycasts[0].collectData(board)
            left_data = self.raycasts[1].collectData(board)
            right_data = self.raycasts[2].collectData(board)

            if left_data != -1 and (left_data[2] < 50 or left_data[3] == 1):
                self.moveRight()

            if right_data != -1 and (right_data[2] < 50 or right_data[3] == 1):
                self.moveLeft()
            if data != -1 and (data[2] < self.dist or data[3] == 1):
                self.dist = 100
                if left_data == -1 and right_data == -1:
                    rand = random.randint(0, 1)
                    if rand == 0:
                        self.status = CAR_STATUS_GO_LEFT
                    else:
                        self.status = CAR_STATUS_GO_RIGHT

                elif left_data == -1 and right_data != -1:
                    self.status = CAR_STATUS_GO_LEFT

                elif left_data != -1 and right_data == -1:
                    self.status = CAR_STATUS_GO_RIGHT

                elif left_data != -1 and right_data != -1:
                    if left_data[2] > right_data[2]:
                        self.status = CAR_STATUS_GO_LEFT
                    elif left_data[2] < right_data[2]:
                        self.status = CAR_STATUS_GO_RIGHT
                    else:
                        rand = random.randint(0, 1)
                        if rand == 0:
                            self.status = CAR_STATUS_GO_LEFT
                        else:
                            self.status = CAR_STATUS_GO_RIGHT

        elif self.status == CAR_STATUS_GO_LEFT:
            self.moveLeft()
            data = self.raycasts[0].collectData(board)
            right_data = self.raycasts[2].collectData(board)
            if data == -1:
                if right_data != -1 and right_data[2] > 40:
                    self.dist = 70
                    self.status = CAR_STATUS_DRIVE

        elif self.status == CAR_STATUS_GO_RIGHT:
            self.moveRight()
            data = self.raycasts[0].collectData(board)
            left_data = self.raycasts[1].collectData(board)
            if data == -1:
                if left_data != -1 and left_data[2] > 40:
                    self.dist = 70
                    self.status = CAR_STATUS_DRIVE

    def speedUp(self):

        targetX = self.x + math.cos(math.radians(self.angle)) * 2
        targetY = self.y - math.sin(math.radians(self.angle)) * 2

        #if targetX >= 30 and targetX <= 916 and targetY >= 30 and targetY <= 507:
        self.x = targetX
        self.y = targetY

    def speedDown(self):

        targetX = self.x - math.cos(math.radians(self.angle)) * 2
        targetY = self.y + math.sin(math.radians(self.angle)) * 2

        #if targetX >= 30 and targetX <= 950 and targetY >= 30 and targetY <= 935:
        self.x = targetX
        self.y = targetY

    def moveRight(self):
        self.angle -= 2
        if self.angle == -359:
            self.angle = 0

    def moveLeft(self):
        self.angle += 2
        if self.angle == 359:
            self.angle = 0