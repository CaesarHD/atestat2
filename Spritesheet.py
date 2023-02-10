import pygame


class Spritesheet:
    def __init__(self, image):
        self.sheet = image

    def getImage(self, frame, width, height, scale, colour):
        image = pygame.Surface((width, height)).convert_alpha()
        image.blit(self.sheet, (0, 0), (frame * width, 0, width, height))
        image = pygame.transform.scale(image, (width * scale, height * scale))

        return image
