import pygame

from Resource import Resource
from Spritesheet import Spritesheet


class ResourceProvider:
    def __init__(self):
        self.__cache = {}

    def registerResource(self, name, path, animationFrames, size, actions, bullet, mine):
        imageResource = pygame.image.load(path)
        spriteSheet = Spritesheet(imageResource, size[0], size[1])

        self.__cache[name] = Resource(spriteSheet, animationFrames, size, actions, bullet, mine)

    def getResource(self, name):
        return self.__cache[name]
