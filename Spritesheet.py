import pygame


class Spritesheet:
    def __init__(self, sheet, frameWidth, frameHeigh):
        self.sheet = sheet
        self.frameWidth = frameWidth
        self.frameHeigh = frameHeigh

    def getImageByIndex(self, n, scale):

        x = self.frameWidth * n
        y = 0
        rect = pygame.Rect(x, y, self.frameWidth, self.frameHeigh)
        image = self.sheet.subsurface(rect)
        image = pygame.transform.scale(image, (self.frameWidth * scale, self.frameHeigh * scale)).convert_alpha()
        return image
