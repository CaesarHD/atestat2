from Actor import Actor
import pygame

class Cable(Actor):
    def __init__(self, pos, scale, resource, collisionOffset):
        super().__init__(pos, scale, resource, collisionOffset)

    def working(self, player):
        if player.getCollisionBox().colliderect(self.getCollisionBox()):
                player.isShot = True

