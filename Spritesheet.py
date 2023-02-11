import pygame


class Spritesheet:
    def __init__(self, sheet, frameWidth, frameHeigh):
        self.sheet = sheet
        self.frameWidth = frameWidth
        self.frameHeigh = frameHeigh

    # def getImage(self, frame, width, height, scale, colour):
    #     image = pygame.Surface((width, height))
    #     image.blit(self.sheet, (0, 0), (frame * width, 0, width, height))
    #     image = pygame.transform.scale(image, (width * scale, height * scale))
    #     # image.set_colorkey(colour)
    #
    #     return image

    def getImageByIndex(self, n, scale):

        x = self.frameWidth * n
        y = 0
        rect = pygame.Rect(x, y, self.frameWidth, self.frameHeigh)
        image = self.sheet.subsurface(rect)
        image = pygame.transform.scale(image, (self.frameWidth * scale, self.frameHeigh * scale))
        return image
