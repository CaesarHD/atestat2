import pygame
from pygame import Rect

from Actor import Actor

COLLISION_SLAB_HEIGHT = 50
LASER_HEIGHT = 80


class Laser:
    def __init__(self, posX, resource):
        self.pos = posX
        self.resource = resource
        self.laserTop = Actor((posX, 0), 2, self.resource.getResource("laserTop"), (65, 0))
        self.laserSlab = Actor((posX, 265 * 2 - 6), 2, self.resource.getResource("laserSlab"), None)
        self.laserSlab.topOffset = 4
        self.collisionHeight = self.laserSlab.bounds.height - LASER_HEIGHT
        self.collisionArea = Rect(self.laserTop.getCollisionBox().x, self.laserTop.bounds.bottom,
                                  self.laserTop.bounds.width,
                                  self.collisionHeight)
        self.lastUpdate = pygame.time.get_ticks()
        self.animationCooldown = 4000
        self.on = False

    def playerBurned(self, player):
        if (player.getCollisionBox().colliderect(
                self.laserTop.getCollisionBox())):
            if self.laserTop.action == 0:
                player.isShot = True
            else:
                if self.laserTop.frame > 8:
                    player.isShot = True

    def working(self):
        currentTime = pygame.time.get_ticks()
        if currentTime - self.lastUpdate > self.animationCooldown:
            self.on = True
            self.lastUpdate = currentTime

        if self.on:
            self.laserTop.action = 1
            self.laserSlab.action = 1

            if self.laserTop.frame == 8:
                self.on = False
        else:
            self.laserTop.action = 0
            self.laserSlab.action = 0

    def drawActor(self, screen):
        self.laserTop.drawActor(screen)
        self.laserSlab.drawActor(screen)
        # pygame.draw.rect(screen.screen, 'green', self.laserTop.getCollisionBox())
