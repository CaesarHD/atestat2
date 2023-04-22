import pygame

from Actor import Actor
from pygame import Rect


class Press:
    def __init__(self, pressPosX, pressPosYOffset, resourceProvider):
        self.up = True
        self.offset = pressPosYOffset

        self.pressUp = Actor((pressPosX, -1 - pressPosYOffset),
                             2,
                             resourceProvider.getResource("pressUp"),
                             None)

        self.pressDown = Actor((pressPosX, (272 * 2) - 1),
                               2,
                               resourceProvider.getResource("pressDown"),
                               None)

    def drawActor(self, screen):
        self.pressUp.drawActor(screen)
        self.pressDown.drawActor(screen)

    def pressPlayer(self, player):
        return abs(player.getCollisionBox().top - self.pressUp.getCollisionBox().bottom) > 5

    def presses(self):
        if self.pressUp.getCollisionBox().bottom >= self.pressDown.getCollisionBox().top:
            self.up = True
        elif self.pressUp.getCollisionBox().bottom < 170:
            self.up = False

    def playerPressed(self, player):
        collisionHeight = self.pressDown.bounds.top - self.pressUp.bounds.bottom
        collisionArea = Rect(self.pressUp.bounds.x + 10, self.pressUp.bounds.bottom, self.pressUp.bounds.width - 20,
                             collisionHeight)

        if (player.getCollisionBox().colliderect(
                collisionArea)) and player.bounds.height > collisionArea.height and not self.up:
            player.isShot = True

    def moving(self):
        self.presses()
        if self.up:
            self.pressUp.moveUp(5)
        else:
            self.pressUp.moveDown(7)
