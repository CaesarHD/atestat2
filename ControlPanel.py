from Actor import Actor
import pygame


class ControlPanel(Actor):
    def __init__(self, pos, scale, resource, collisionOffset):
        super().__init__(pos, scale, resource, collisionOffset)
        self.animationCooldown = 100
        self.lastUpdate = pygame.time.get_ticks()
        self.on = False
        self.pause = False

    def working(self, player):
        if abs(player.getCollisionBox().x - self.getCollisionBox().x) < 100:
            self.on = True
            if not self.pause:
                self.action = 0
            if self.frame == 4:
                self.pause = True
            if self.pause:
                self.action = 1
        else:
            self.pause = False
            self.action = 2
            if self.frame == 5:
                self.on = False

    def drawActor(self, screen):
        if self.on:
            self.resetAnimation()
            if self.isRight:
                screen.blit(self.animationList[self.action][self.frame], self.bounds)
            else:
                self.animationListFlip = pygame.transform.flip(self.animationList[self.action][self.frame], True, False)
                screen.blit(self.animationListFlip, self.bounds)
