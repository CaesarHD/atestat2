import pygame
from pygame import Rect

from Spritesheet import Spritesheet


class Player:
    def __init__(self, pos, size, spritesheetImg):
        self.bounds = Rect(pos, size)
        self.spritesheetImg = spritesheetImg
        self.spritesheet = Spritesheet(spritesheetImg)
        self.animationList = []
        self.animationSteps = [4, 4, 5, 1, 6]
        self.action = 1
        self.pos = pos
        self.animationCooldown = 120
        self.frame = 0
        self.stepCounter = 0

        black = (0, 0, 0)
        for animation in self.animationSteps:
            tempImageList = []
            for _ in range(animation):
                tempImageList.append(self.spritesheet.getImage(self.stepCounter, 57, 57, 7, black))
                self.stepCounter += 1
            self.animationList.append(tempImageList)

    def tickAnimation(self):
        self.frame += 1
        if self.frame >= len(self.animationList[self.action]):
            self.frame = 0

    def draw(self, screen, coord):
        screen.blit(self.animationList[self.action][self.frame], coord)
