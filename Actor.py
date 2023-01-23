from pygame import Rect
import pygame


class Actor:
    def __init__(self, pos, size, spritesheet, animationSteps, frameWidth, frameHeight):
        self.bounds = Rect(pos, size)
        self.velocity = 10
        self.size = size
        self.spritesheet = spritesheet
        self.pos = pos

        self.animationList = []
        self.animationSteps = animationSteps
        self.action = 4
        self.animationCooldown = 120
        self.frame = 0
        self.stepCounter = 0

        black = (0, 0, 0)

        for animation in self.animationSteps:
            tempImageList = []
            for _ in range(animation):
                tempImageList.append(self.spritesheet.getImage(self.stepCounter, frameWidth, frameHeight, self.size[0], black))
                self.stepCounter += 1
            self.animationList.append(tempImageList)

    def tickAnimation(self):
        self.frame += 1
        if self.frame >= len(self.animationList[self.action]):
            self.frame = 0

    def drawActor(self, screen):
        screen.blit(self.animationList[self.action][self.frame], self.bounds)

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
        self.bounds.topleft = (initial[0], initial[1] - (self.velocity))


    def moveDown(self):
        initial = self.bounds.topleft
        self.bounds.topleft = (initial[0], initial[1] + self.velocity)



