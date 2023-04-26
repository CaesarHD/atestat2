from Actor import Actor


class Gate:
    def __init__(self, gatePosX, resourceProvider):
        self.resourceProvider = resourceProvider
        self.isClose = True
        self.isOpening = False
        self.gatePosX = gatePosX
        self.staticGate = Actor((self.gatePosX, -2),
                                2,
                                resourceProvider.getResource("staticGate"),
                                None)
        self.dinamicGate = Actor((self.gatePosX, -2),
                                 2,
                                 resourceProvider.getResource("dinamicGate"),
                                 None)
        self.gateWall = Actor((self.gatePosX, -2),
                              2,
                              resourceProvider.getResource("gateWall"),
                              None)

    def toggleOpen(self, player):
        if abs(player.getCollisionBox().x - self.gateWall.getCollisionBox().x) < 180:
            if self.isClose:
                self.isOpening = True
            else:
                self.isOpening = False
            self.isClose = False
        else:
            self.isClose = True

    def open(self):
        if not self.isClose:
            if self.dinamicGate.getCollisionBox().bottom > 280:
                self.dinamicGate.moveUp(15)

    def close(self):
        if self.isClose:
            if self.dinamicGate.getCollisionBox().top < -2:
                self.dinamicGate.moveDown(15)

    def working(self, player):
        self.toggleOpen(player)
        self.open()
        self.close()

    def drawGate(self, screen):
        self.gateWall.drawActor(screen)
        self.dinamicGate.drawActor(screen)
        self.staticGate.drawActor(screen)

