class Abilities:
    def __init__(self, actor):
        self.getPotion = actor.getPotion
        self.placingMine = actor.placingMine
        self.actor = actor

    def setStatus(self):
        self.getPotion = self.actor.getPotion
        self.placingMine = self.actor.placingMine

    def useAbility(self):
        return  self.getPotion or self.placingMine