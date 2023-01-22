import pygame

from Actor import Actor


class Background(Actor):
    def __init__(self, pos, size, spritesheet):
        super().__init__(pos, size, spritesheet)

    def transform(self, size):
        self.spritesheet.sheet = pygame.transform.scale(self.spritesheet.sheet, size)

    def drawActor(self, screen, coord):
        self.spritesheet.sheet = pygame.transform.scale(self.spritesheet.sheet, self.size)
        screen.blit(self.spritesheet.sheet, coord)

