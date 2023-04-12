from Actor import Actor

SCREEN_BOTTOM = 480 * 1.33
SPEED = 2


class Ground(Actor):
    def __init__(self, pos, scale, resource):
        super().__init__(pos, scale, resource)
        self.pos = pos
        self.bounds.bottom = SCREEN_BOTTOM

    def scrolling(self, screen, scroll):
        for x in range(10):
            speed = SPEED
            screen.blit(self.animationList[0][self.frame],
                        (self.bounds.size[0] * x - scroll * speed, SCREEN_BOTTOM - self.bounds.size[1]))
