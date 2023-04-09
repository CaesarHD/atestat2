from Levels import Levels
from Mine import Mine


class Abilities:
    def __init__(self, actor):
        self.getPotion = actor.getPotion
        self.actor = actor
        self.mines = []
        self.level = Levels()
        self.resourceProvider = self.level.loadResourcesLevel(1)

    def setStatus(self):
        self.getPotion = self.actor.getPotion
        self.placingMine = self.actor.placingMine

    def useAbility(self):
        return  self.getPotion or self.placingMine