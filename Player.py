import pygame
from pygame import Rect

from Actor import Actor
from Spritesheet import Spritesheet


class Player(Actor):
    def __init__(self, pos, size, spritesheet, animationSteps, frameWidth, frameHeight):
        super().__init__(pos, size, spritesheet, animationSteps, frameWidth, frameHeight)



