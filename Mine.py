from Actor import Actor


class Mine(Actor):
    def __init__(self, pos, scale, resource):
        super().__init__(pos, scale, resource)
        self.isActive = False
        self.isTriggered = False

def trigger(self, actor):
    if self.isActive:
        if actor.bounds.x > self.boumds.x and actor.bounds.x < self.bounds.x:
            self.isTriggered = True

def exploding(self):
    if self.isTriggered:
        pass