from Actor import Actor
import pygame


class Bullet(Actor):
    def __init__(self, pos, scale, resource, isRight):
        super().__init__(pos, scale, resource)
        self.isRight = isRight
        self.out = False

        if self.isRight:
            self.bounds.x += 30
        else:
            self.bounds.x -= 50

    def collideWith(self, screen, actor):
        return (abs(self.bounds.x - actor.bounds.x) < 60 and (self.bounds.top >= actor.bounds.top)) or self.collideWithScreen(screen)

    def collideWithScreen(self, screen):
        return self.bounds.x > screen.screenWidth or self.bounds.x < 0

    def propell(self, screen, actor):
        if not self.collideWith(screen, actor):
            if self.isRight:
                self.moveRight(40)
            else:
                self.moveLeft(40)
        else:
            self.out = True
