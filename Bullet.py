from Actor import Actor
import pygame

class Bullet(Actor):
    def __init__(self, pos, scale, resource):
        super().__init__(pos, scale, resource)
        self.direction = 0
        self.radius = 2000
        self.release = False
        
    def getDirection(self, player):
        self.isRight = player.isRight
        self.isLeft = player.isLeft
        if self.isRight:
            return 1
        if self.isLeft:
            return -1

    def drawActor(self, screen):
        if self.radius > 0:
            if self.isRight:
                screen.blit(self.animationList[self.action][self.frame], self.bounds)
            else:
                self.animationListFlip = pygame.transform.flip(self.animationList[self.action][self.frame], True, False)
                screen.blit(self.animationListFlip, self.bounds)
            self.radius -= 1
            if self.direction > 0:
                self.moveRight(20)
            if self.direction < 0:
                self.moveLeft(20)
        if self.radius == 0:
            self.release = False
            self.radius = 2000
            self.direction = 0
    