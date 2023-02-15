from Character import Character

GROUND = 430
GFORCE = 10


class Enemy(Character):
    def __init__(self, pos, scale, resource):
        super().__init__(pos, scale, resource)
        self.isShooting = False
        self.isJumping = False
        self.isArmed = False
        self.isPreJumping = False
        self.isLanding = False
        self.velocity = 7
        self.right = True

    def fall(self):

        # self.action = 0
        self.gravityForce += 1.5
        self.moveDown()

    def inIdle(self):
        if not self.isFalling and not self.isJumping:
            self.isIdle = True
            self.action = 0

    def gravity(self):
        if self.bounds.topleft[1] < GROUND:
            self.isFalling = True
            self.isIdle = False
            self.fall()
        else:
            self.isFalling = False
            self.gravityForce = GFORCE

    def moveLeft(self):
        self.isLeft = True
        self.isRight = False
        self.isIdle = False
        if not self.isFalling and not self.isShooting:
            self.action = 3
        if self.isShooting:
            self.shoot()
        initial = self.bounds.topleft
        self.bounds.topleft = (initial[0] - self.velocity, initial[1])

    def moveRight(self):
        self.isIdle = False
        self.isRight = True
        self.isLeft = False
        if not self.isFalling and not self.isShooting:
            self.action = 3
        if self.isShooting:
            self.shoot()
        initial = self.bounds.topleft
        self.bounds.topleft = (initial[0] + self.velocity, initial[1])

    def shoot(self):
        if self.isIdle:
            self.action = 2
            if self.frame == 2:
                self.isShooting = False
        else:
            self.action = 3
            if self.frame == 3:
                self.isShooting = False

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
