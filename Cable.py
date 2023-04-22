from Actor import Actor
import pygame
from pygame import Rect

COLLISION_AREA_HEIGHT = 40

class Cable(Actor):
    def __init__(self, pos, scale, resource, collisionOffset):
        super().__init__(pos, scale, resource, collisionOffset)
        self.bounds.y = self.bounds.y - 2

    def working(self, player):
        rect = Rect((self.bounds.x + 60 , self.bounds.y + self.bounds.height - COLLISION_AREA_HEIGHT, self.bounds.width - 120, COLLISION_AREA_HEIGHT))
        if player.getCollisionBox().colliderect(rect):
                player.isShot = True

