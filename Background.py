import pygame

from Actor import Actor


class Background(Actor):
    def __init__(self, pos, size, scale, resource):
        super().__init__(pos, size, scale, resource)

    def transform(self, size):
        self.spritesheet.sheet = pygame.transform.scale(self.spritesheet.sheet, size)

    def drawActor(self, screen):
        self.spritesheet.sheet = pygame.transform.scale(self.spritesheet.sheet, self.bounds.size)
        screen.blit(self.spritesheet.sheet, self.bounds.topleft)

