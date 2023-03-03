import pygame

from Actor import Actor


class Background(Actor):
    def __init__(self, pos, scale, resource):
        super().__init__(pos, scale, resource)
        self.backgrounds = []
        animation = 0
        for _ in self.animationSteps:
            self.backgrounds.append(self.animationList[animation][self.frame])
            animation += 1

    def transform(self, size):
        self.spritesheet.sheet = pygame.transform.scale(self.spritesheet.sheet, size)

    def drawActor(self, screen):
        action = 0
        for i in self.animationSteps:
            screen.blit(self.animationList[action][self.frame], self.bounds)
            action = action + 1

    def scrolling(self, screen, scroll):
        for x in range(10):
            speed = 1
            for i in self.backgrounds:
                screen.blit(i, (self.bounds.size[0] * x - scroll * speed, 0))
                speed += 0.5

