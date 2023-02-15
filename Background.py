import pygame

from Actor import Actor


class Background(Actor):
    def __init__(self, pos, scale, resource):
        super().__init__(pos, scale, resource)

    def transform(self, size):
        self.spritesheet.sheet = pygame.transform.scale(self.spritesheet.sheet, size)

    def drawActor(self, screen):
        self.spritesheet.sheet = pygame.transform.scale(self.spritesheet.sheet, (self.bounds.size[0] * self.scale, self.bounds.size[1] * self.scale))
        screen.blit(self.spritesheet.sheet, self.bounds.topleft)

