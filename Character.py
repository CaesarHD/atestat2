import pygame
from pygame import Rect

from Actor import Actor
from Spritesheet import Spritesheet

GROUND = 430
JUMP_HEIGHT = 150
GFORCE = 10

class Character(Actor):


    def __init__(self, pos, size, scale, resource):
        super().__init__(pos, size, scale, resource)
        self.preJumpPosition = GROUND
        self.isShooting = False
        self.isJumping = False
        self.isArmed = False
        self.isPreJumping = False
        self.isLanding = False
        self.velocity = 6

    def fall(self):
        if self.isArmed:
            self.action = 8
            if self.isShooting:
                self.shoot()
        else:
            self.action = 3

        self.gravityForce += 1.5
        self.moveDown()
        self.isLanding = True

    def jump(self):
        if self.isJumping and not self.isFalling:
            self.isIdle = False
            if self.isPreJumping:
                self.preJump()
            else:
                if self.isArmed:
                    self.action = 8
                    if self.isShooting:
                        self.shoot()
                else:
                    self.action = 3

            #TODO: calculate this based on JUMP_HEIGHT
            self.gravityForce -= 0.35
            if self.gravityForce <= 0.1:
                self.gravityForce = 0.1

            self.moveUp()
            currentPos = self.bounds.topleft[1]
            if self.preJumpPosition - currentPos > JUMP_HEIGHT:
                self.isJumping = False

    def preJump(self):
        if self.isPreJumping:
            if self.isArmed:
                self.action = 7
            else:
                self.action = 2
            if self.frame == 2:
                self.isPreJumping = False
    def landing(self):
        if self.isLanding:
            if self.isArmed:
                self.action = 9
            else:
                self.action = 4
            if self.frame == 1:
                self.isLanding = False
    def shoot(self):
        if self.isIdle:
            self.action = 10
            if self.frame == 2:
                self.isShooting = False
        else:
            if self.isJumping or self.isFalling:
                self.action = 13
                if self.frame == 2:
                    self.isShooting = False
            else:
                self.action = 11
                if self.frame == 5:
                    self.isShooting = False

    def moveLeft(self):
        self.isLeft = True
        self.isRight = False
        self.isIdle = False
        if not self.isJumping and not self.isFalling and not self.isShooting:
            if not self.isArmed:
                self.action = 1
            else:
                self.action = 6
        if self.isShooting:
            self.shoot()
        initial = self.bounds.topleft
        self.bounds.topleft = (initial[0] - self.velocity, initial[1])

    def moveRight(self):
        self.isIdle = False
        self.isRight = True
        self.isLeft = False
        if not self.isJumping and not self.isFalling and not self.isShooting:
            if not self.isArmed:
                self.action = 1
            else:
                self.action = 6
        if self.isShooting:
            self.shoot()
        initial = self.bounds.topleft
        self.bounds.topleft = (initial[0] + self.velocity, initial[1])

    def inIdle(self):
        if not self.isFalling and not self.isJumping:
            self.isIdle = True

            if self.isShooting:
                self.shoot()
            else:
                if self.isArmed:
                    self.action = 5
                else:
                    self.action = 0
    def moveUp(self):
        initial = self.bounds.topleft
        self.bounds.topleft = (initial[0], initial[1] - self.gravityForce)

    def moveDown(self):
        initial = self.bounds.topleft
        self.bounds.topleft = (initial[0], initial[1] + self.gravityForce)

    def gravity(self):
        if self.bounds.topleft[1] < GROUND:
            if not self.isJumping:
                self.isFalling = True
                self.isIdle = False
                self.fall()
        else:
            self.isFalling = False
            self.landing()
            self.gravityForce = GFORCE


    def toggleWeapon(self):
        self.isArmed = not self.isArmed

    def toggleJump(self):
        if not self.isFalling and not self.isJumping:
            self.isJumping = True
            self.isPreJumping = True
            self.preJumpPosition = self.bounds.topleft[1]

    def toggleShooting(self):
        if self.isArmed and not self.isShooting:
            self.isShooting = True



