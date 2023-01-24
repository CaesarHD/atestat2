import pygame
from pygame import Rect

from Actor import Actor
from Spritesheet import Spritesheet


class Player(Actor):
    def __init__(self, pos, size, spritesheet, animationSteps, frameWidth, frameHeight):
        super().__init__(pos, size, spritesheet, animationSteps, frameWidth, frameHeight)

    def fall(self):
        if self.isFalling:
            self.action = 3
            self.frame = 0
            self.moveDown()

    def jump(self, initialPos):
        if self.isJumping and not self.isFalling:
            self.action = 3
            self.frame = 0
            self.moveUp()
            currentPos = self.bounds.topleft[1]
            print(currentPos)
            if initialPos - currentPos > 150:
                self.isJumping = False


