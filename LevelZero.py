from Actor import Actor
from Background import Background
from Levels import Levels
import pygame

lastUpdate = pygame.time.get_ticks()
class LevelZero:
    def __init__(self):
        self.level = Levels()
        self.lvl = 0
        self.resourceProvider = self.level.loadResourcesLevel(self.lvl)
        self.staticBackground = Background((0, 0), 2, self.resourceProvider.getResource("staticBackground"))
        self.vitaexLogo = Actor((0, 0), 2, self.resourceProvider.getResource("vitaexLogo"), None)
        self.pressKey = Actor((0, 0), 2, self.resourceProvider.getResource("pressKey"), None)
        self.opacity = 255
        self.pressKey.spritesheet.sheet = pygame.transform.scale2x(self.pressKey.spritesheet.sheet)
        self.animationCooldown = 50
        self.increase = False
        self.decrease = True

    def drawLevel(self, screen):
        self.flutterText()
        self.staticBackground.drawActor(screen)
        self.vitaexLogo.drawActor(screen)
        screen.blit(self.pressKey.spritesheet.sheet, (0, 0))

    def flutterText(self):
        global lastUpdate
        currentTime = pygame.time.get_ticks()
        if currentTime - lastUpdate > self.animationCooldown:
            self.flicker()
            lastUpdate = currentTime

    def flicker(self):
        if self.opacity < 10:
            self.increase = True
        elif self.opacity >= 255:
            self.increase = False
        if self.increase:
            self.opacity += 20
        else:
            self.opacity -= 20
        self.pressKey.spritesheet.sheet.set_alpha(self.opacity)
