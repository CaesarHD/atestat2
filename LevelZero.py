from Actor import Actor
from Background import Background
from Levels import Levels
import pygame

pressKeyLastUpdate = pygame.time.get_ticks()
voyagerLastUpdate = pygame.time.get_ticks()
class LevelZero:
    def __init__(self):
        self.level = Levels()
        self.lvl = 0
        self.resourceProvider = self.level.loadResourcesLevel(self.lvl)
        self.staticBackground = Background((0, 0), 2, self.resourceProvider.getResource("staticBackground"))
        self.vitaexLogo = Actor((0, 0), 2, self.resourceProvider.getResource("vitaexLogo"), None)
        self.pressKey = Actor((0, 0), 2, self.resourceProvider.getResource("pressKey"), None)
        self.voyager = Actor((1500, -100), 2, self.resourceProvider.getResource("voyager"), None)
        self.asteroid = Actor((-200, 400), 0.5, self.resourceProvider.getResource("asteroid"), None)

        self.opacity = 255
        self.pressKey.spritesheet.sheet = pygame.transform.scale2x(self.pressKey.spritesheet.sheet)
        self.pressKeyAnimationCooldown = 50
        self.voyagerAnimationCooldown = 8000
        self.increase = False
        self.decrease = True
        self.startVoyager = False

    def drawLevel(self, screen):
        self.flutterText()
        self.moveVoyager()
        self.moveAsteroid()
        self.staticBackground.drawActor(screen)
        self.asteroid.drawActor(screen)
        self.vitaexLogo.drawActor(screen)
        self.voyager.drawActor(screen)
        screen.blit(self.pressKey.spritesheet.sheet, (0, 0))

    def flutterText(self):
        global pressKeyLastUpdate
        currentTime = pygame.time.get_ticks()
        if currentTime - pressKeyLastUpdate > self.pressKeyAnimationCooldown:
            self.flicker()
            pressKeyLastUpdate = currentTime

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

    def moveVoyager(self):
        global voyagerLastUpdate
        if not self.startVoyager:
            currentTime = pygame.time.get_ticks()
            if currentTime - voyagerLastUpdate > self.voyagerAnimationCooldown:
                self.startVoyager = True
                voyagerLastUpdate = currentTime
        if self.startVoyager:
            if self.voyager.getCollisionBox().y < 2000:
                self.voyager.moveDown(1)
                self.voyager.moveLeft(1.5)
            else:
                self.voyager.bounds.topleft = (2500, -600)

    def moveAsteroid(self):
        if self.asteroid.bounds.x < 3000:
            self.asteroid.moveRight(1)
        else:
            self.asteroid.bounds.topleft = (-2000, 400)

