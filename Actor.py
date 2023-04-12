import pygame
from pygame import Rect

GFORCE = 2
SPEED = 2


class Actor:

    def __init__(self, pos, scale, resource, collisionBox):
        self.scale = scale
        self.bounds = Rect(pos, (resource.size[0] * self.scale, resource.size[1] * self.scale))

        if collisionBox is None:
            self.collisionOffset = (0, 0)
        else:
            self.collisionOffset = (collisionBox[0] * self.scale, collisionBox[1] * self.scale)

        self.velocity = 7
        self.gravityForce = GFORCE
        self.spritesheet = resource.spritesheet
        self.isFalling = False
        self.isIdle = True
        self.isRight = True
        self.isLeft = False
        self.animationList = []
        self.animationListFlip = 0
        self.animationSteps = resource.animationFrames
        self.action = 0
        self.animationCooldown = 500
        self.frame = 0
        self.stepCounter = 0
        self.scroll = 0
        self.actionChanged = False

        for animation in self.animationSteps:
            tempImageList = []
            for _ in range(animation):
                tempImageList.append(self.spritesheet.getImageByIndex(self.stepCounter, self.scale))
                self.stepCounter += 1
            self.animationList.append(tempImageList)

    def tickAnimation(self):
        self.frame += 1
        # self.resetAnimation()

    def resetAnimation(self):
        if self.frame >= len(self.animationList[self.action]):
            print(self.frame)

            print("=======")

            self.frame = 0

    def drawActor(self, screen):
        self.resetAnimation()

        if self.isRight:
            screen.blit(self.animationList[self.action][self.frame], self.bounds)
        else:
            self.animationListFlip = pygame.transform.flip(self.animationList[self.action][self.frame], True, False)
            screen.blit(self.animationListFlip, self.bounds)

    def scrolling(self, speed):
        self.bounds.x += speed

    def position(self, pos):
        self.bounds.topleft = pos

    def setX(self, x):
        initial = self.bounds.topleft
        self.position((x, initial[1]))

    def setY(self, y):
        initial = self.bounds.topleft
        self.position((initial[0], y))

    def moveRight(self, velocity):
        initial = self.bounds.topleft
        self.bounds.topleft = (initial[0] + velocity, initial[1])

    def moveLeft(self, velocity):
        initial = self.bounds.topleft
        self.bounds.topleft = (initial[0] - velocity, initial[1])

    def moveUp(self, velocity):
        initial = self.bounds.topleft
        self.bounds.topleft = (initial[0], initial[1] - velocity)

    def moveDown(self, velocity):
        initial = self.bounds.topleft
        self.bounds.topleft = (initial[0], initial[1] + velocity)

    def isCloseTo(self, actor, distance):
        return abs(self.bounds.topleft[0] - actor.bounds.topleft[0]) < distance

    def getCollisionBox(self):
        collisionBoxWidth = self.bounds.width - self.collisionOffset[0]
        collisionBoxHeight = self.bounds.height - self.collisionOffset[1]
        collisionBoxX = self.bounds.x + (self.bounds.width / 2) - (collisionBoxWidth / 2)
        collisionBoxY = self.bounds.y + (self.bounds.height / 2) - (collisionBoxHeight / 2)

        return Rect(collisionBoxX, collisionBoxY, collisionBoxWidth, collisionBoxHeight)
