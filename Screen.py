import pygame

class Screen:
    def __init__(self, width, height):

        self.screenWidth = width
        self.screenHeight = height

        self.screen = pygame.display.set_mode((self.screenWidth, self.screenHeight))

    def fill(self, color):
        self.screen.fill(color)

    def blit(self, image, dest):
        self.screen.blit(image, dest)
