from Character import Character

GROUND = 430
GFORCE = 10


class Enemy(Character):
    def __init__(self, pos, scale, resource):
        super().__init__(pos, scale, resource)
        self.isShooting = False
        self.isJumping = False
        self.isArmed = True
        self.isPreJumping = False
        self.isLanding = False
        self.velocity = 7
        self.right = True


    def fall(self):
        self.gravityForce += 1.5
        self.moveDown()

    def moving(self):

        if self.right:
            if self.bounds.topleft[0] < 700:
                self.moveRight()
            else:
                self.right = False
        if not self.right:
            if self.bounds.topleft[0] > 20:
                self.moveLeft()
            else:
                self.right = True
