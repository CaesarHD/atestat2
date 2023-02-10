from pygame import Rect
import pygame

from Spritesheet import Spritesheet


class Actor:
    def __init__(self, pos, size, spritesheet, animationSteps, frameWidth, frameHeight):
        self.bounds = Rect(pos, size)
        self.velocity = 7
        self.gravityForce = 10
        self.size = size
        self.frameWidth = frameWidth
        self.frameHeight = frameHeight
        self.spritesheet = spritesheet
        self.pos = pos
        self.isJumping = False
        self.isFalling = False
        self.isArmed = False
        self.isIdle = True
        self.isShooting = False
        self.isRight = True
        self.isLeft = False
        self.animationList = []
        self.animationListFlip = 0
        self.animationSteps = animationSteps
        self.action = 0
        self.animationCooldown = 120
        self.frame = 0
        self.stepCounter = 0


        self.black = (0, 0, 0)

        for animation in self.animationSteps:
            tempImageList = []
            for _ in range(animation):
                tempImageList.append(self.spritesheet.getImage(self.stepCounter, self.frameWidth, self.frameHeight, self.size[0], self.black))
                self.stepCounter += 1
            self.animationList.append(tempImageList)

    def tickAnimation(self):
        self.frame += 1
        if self.frame >= len(self.animationList[self.action]):
            self.frame = 0

    def drawActor(self, screen):
        if self.isRight:
            screen.blit(self.animationList[self.action][self.frame], self.bounds)
        else:
            self.animationListFlip = pygame.transform.flip(self.animationList[self.action][self.frame], True, False)
            self.animationListFlip.set_colorkey(self.black)
            screen.blit(self.animationListFlip, self.bounds)

    def position(self, pos):
        self.bounds.topleft = pos

    def setX(self, x):
        initial = self.bounds.topleft
        self.position((x, initial[1]))

    def setY(self, y):
        initial = self.bounds.topleft
        self.position((initial[0], y))

    def moveRight(self):
        initial = self.bounds.topleft
        self.bounds.topleft = (initial[0] + self.velocity, initial[1])


    def moveLeft(self):
        initial = self.bounds.topleft
        self.bounds.topleft = (initial[0] - self.velocity, initial[1])

    def moveUp(self):
        initial = self.bounds.topleft
        self.bounds.topleft = (initial[0], initial[1] - self.velocity)


    def moveDown(self):
        initial = self.bounds.topleft
        self.bounds.topleft = (initial[0], initial[1] + self.velocity)

    def jump(self, initialPos):
        self.moveUp()
        currentPos = self.bounds.topleft[1]
        if initialPos - currentPos > 150:
            self.isJumping = False

    def fall(self):
        if self.isFalling:
            if self.isArmed:
                self.action = 5
            else:
                self.action = 2
            self.frame = 0
            self.moveDown()
