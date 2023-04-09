from Actor import Actor

MIDDLE_MINE_COORD = 10.5

class Mine(Actor):
    def __init__(self, pos, scale, resource):
        super().__init__(pos, scale, resource)
        self.isActive = False
        self.isTriggered = False
        self.resource = resource

    def active(self, player):
        if not self.isActive:
            if not player.isCollideWith(self):
                self.isActive = True
                
    def trigger(self, player, actors):
        if self.isActive:
            for actor in actors:
                if actor.isCollideWith(self):
                    self.isTriggered = True
                    actor.isShot = True
            if player.isCollideWith(self):
                self.isTriggered = True
                player.isShot = True

    def getExplosionCoord(self):
        return (self.bounds.x - 70, self.bounds.y - 92*2)