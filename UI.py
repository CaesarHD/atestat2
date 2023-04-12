from Icons import Icons
from Levels import Levels


class UI:
    def __init__(self):
        self.lifeBarPos = (20, 20)
        self.gunIconPos = (87, 112)
        self.mineIconPos = (140, 112)

        self.level = Levels()
        self.resourceProvider = self.level.loadResourcesLevel(1)

        self.lifeBar = Icons(self.lifeBarPos, 1.5, self.resourceProvider.getResource('lifeBar'))
        self.mineIcon = Icons(self.mineIconPos, 1.5, self.resourceProvider.getResource('mineIcon'))
        self.gunIcon = Icons(self.gunIconPos, 1.5, self.resourceProvider.getResource('gunIcon'))

    def drawUI(self, screen):
        self.lifeBar.drawActor(screen)
        self.mineIcon.drawActor(screen)
        self.gunIcon.drawActor(screen)

    def setStatus(self, ability, player):
        ability.abilityChangeState(player)

    def renderUI(self, player, screen):
        self.setStatus(self.mineIcon, player)
        self.gunIcon.gunIconStatus(player)
        self.lifeBar.lifeBarStages(player)
        self.drawUI(screen)
