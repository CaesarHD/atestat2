from Actor import Actor


class PressUp(Actor):
    def __init__(self, pos, scale, resource, collisionOffset):
        super().__init__(pos, scale, resource, collisionOffset)
        self.up = True

    def presses(self, pressDown):
        if self.getCollisionBox().bottom >= pressDown.getCollisionBox().top:
            self.up = True
        elif self.getCollisionBox().bottom < 170:
            self.up = False

    def playerPressed(self, player):
        if self.getCollisionBox().bottom >= player.getCollisionBox().top and self.getCollisionBox().topleft < player.getCollisionBox().topleft < self.getCollisionBox().topright:
            player.isShot = True

    def moving(self, pressDown):
        self.presses(pressDown)
        if self.up:
            self.moveUp(5)
        else:
            self.moveDown(7)
