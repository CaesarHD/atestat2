from pygame import Rect
import pygame


class Actor:
    def __init__(self, pos, size):
        self.bounds = Rect(pos, size)
        self.velocity = 10
        self.size = size

    def drawActor(self, image, screen, coord):
        screen.blit(image, coord)

    def transform(self, image, width, height):  # nu mergeee!!!
        pygame.transform.scale(image, (width, height))
        return image


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
        self.bounds.topleft = (initial[0], initial[1] - self.velocity)

    def moveDown(self):
        initial = self.bounds.topleft
        self.bounds.topleft = (initial[0], initial[1] + self.velocity)