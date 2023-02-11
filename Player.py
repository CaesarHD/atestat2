import pygame
from pygame import Rect

from Actor import Actor
from Spritesheet import Spritesheet


class Player(Actor):
    def __init__(self, pos, size, spritesheet, animationSteps, scale):
        super().__init__(pos, size, spritesheet, animationSteps, scale)

    def fall(self):

        self.isIdle = False

        if self.isFalling:
            if self.isArmed:
                self.action = 5
                if self.isShooting:
                    self.shoot()
            else:
                self.action = 2
            self.gravityForce += 1
            self.moveDown()

    def jump(self, initialPos):

        if self.isJumping and not self.isFalling:
            self.isIdle = False

            if self.isArmed:
                self.action = 5
                if self.isShooting:
                    self.shoot()
            else:
                self.action = 2

            self.gravityForce -= 1.6
            self.moveUp()
            currentPos = self.bounds.topleft[1]
            if initialPos - currentPos > 150:
                self.isJumping = False

    def shoot(self):

        if self.isIdle:
            self.action = 6
            if self.frame == 2:
                self.isShooting = False
        else:
            if self.isJumping or self.isFalling:
                self.action = 8
                if self.frame == 2:
                    self.isShooting = False
            else:
                self.action = 7
                if self.frame == 5:
                    self.isShooting = False

    def moveLeft(self):
        self.isLeft = True
        self.isRight = False
        self.isIdle = False
        if not self.isJumping and not self.isFalling and not self.isShooting:
            if (not self.isArmed):
                self.action = 1
            else:
                self.action = 4
        initial = self.bounds.topleft
        self.bounds.topleft = (initial[0] - self.velocity, initial[1])

    def moveRight(self):

        self.isIdle = False
        self.isRight = True
        self.isLeft = False
        if not self.isJumping and not self.isFalling and not self.isShooting:
            if (not self.isArmed):
                self.action = 1
            else:
                self.action = 4
        initial = self.bounds.topleft
        self.bounds.topleft = (initial[0] + self.velocity, initial[1])

    def inIdle(self):

        if self.isShooting:
            self.shoot()
        else:
            if self.isArmed:
                self.action = 3
            else:
                self.action = 0
        self.gravityForce = 10

    def moveUp(self):
        initial = self.bounds.topleft
        self.bounds.topleft = (initial[0], initial[1] - self.gravityForce)

    def moveDown(self):
        initial = self.bounds.topleft
        self.bounds.topleft = (initial[0], initial[1] + self.gravityForce)
    def gravity(self):

        if self.bounds.topleft[1] < 430 and not self.isJumping:
            self.isFalling = True
        else:
            self.isFalling = False
            self.inIdle()

        self.fall()




