from Actor import Actor


class Press:
    def __init__(self, pressUp, pressDown):
        self.pressUp = pressUp
        self.pressDown = pressDown

    def drawActor(self, screen):
        self.pressUp.moving(self.pressDown)
        self.pressUp.drawActor(screen)
        self.pressDown.drawActor(screen)

    def pressPlayer(self, player):
        return abs(player.getCollisionBox().top - self.pressUp.getCollisionBox().bottom) > 5




