from pygame import Rect

from Actor import Actor

COLLISION_SLAB_HEIGHT = 50


class Laser(Actor):
    def __init__(self, pos, scale, resource, collisionOffset):
        super().__init__(pos, scale, resource, collisionOffset)
        self.bounds.y = self.bounds.y - 2
        self.pos = pos
        self.resource = resource
        self.slabRect = Rect(
            (self.bounds.x + self.resource.size[0], self.bounds.y + self.bounds.height - COLLISION_SLAB_HEIGHT,
             self.bounds.width, COLLISION_SLAB_HEIGHT))
