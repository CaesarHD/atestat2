import pygame

from Actor import Actor


class Background(Actor):
    def __init__(self, pos, size, spritesheet, animationSteps, scale):
        super().__init__(pos, size, spritesheet, animationSteps, scale)
        self.pos = pos

    def transform(self, size):
        self.spritesheet.sheet = pygame.transform.scale(self.spritesheet.sheet, size)

    def drawActor(self, screen):
        self.spritesheet.sheet = pygame.transform.scale(self.spritesheet.sheet, self.size)
        screen.blit(self.spritesheet.sheet, self.pos)

