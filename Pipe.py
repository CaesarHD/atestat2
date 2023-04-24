import pygame
from pygame import Rect

from Actor import Actor

COLLISION_AREA_HEIGHT = 70


class Pipe(Actor):
    def __init__(self, pos, scale, resource, collisionOffset):
        super().__init__(pos, scale, resource, collisionOffset)
        self.bounds.y = self.bounds.y - 2
        self.animationCooldown = 1000
        self.lastUpdate = pygame.time.get_ticks()
        self.on = False

    def working(self):
        currentTime = pygame.time.get_ticks()
        if currentTime - self.lastUpdate > self.animationCooldown:
            self.on = True
            self.lastUpdate = currentTime

        if self.on:
            self.action = 1
            if self.frame == 4:
                self.on = False

        else:
            self.action = 0

    def collideWith(self, player):
        rect = Rect((self.bounds.x + 40, self.bounds.y + self.bounds.height - COLLISION_AREA_HEIGHT,
                     self.bounds.width - 120, COLLISION_AREA_HEIGHT))
        if player.getCollisionBox().colliderect(rect):
            if self.on:
                player.isShot = True
