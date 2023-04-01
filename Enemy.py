from Character import Character

GROUND = 420
GFORCE = 10
PLAYER_DISTANCE = 200


class Enemy(Character):
    def __init__(self, pos, scale, resource, bulletSize, bulletSpawnLocation):
        super().__init__(pos, scale, resource, bulletSize, bulletSpawnLocation)
        self.isShooting = False
        self.isJumping = False
        self.isArmed = True
        self.isPreJumping = False
        self.isLanding = False
        self.velocity = 6
        self.isShot = False
        self.isDead = False
        self.bulletsReceived = 2

    def fall(self):
        self.gravityForce += 1.5
        self.moveDown()

    def getDistance(self, actor):
        return self.bounds.topleft[0] - actor.bounds.topleft[0]

    def changeOrientation(self, actor):
        distance = self.getDistance(actor)
        if distance < 0:
            self.isRight = True
        else:
            self.isRight = False

    def moving(self, player):
        if self.isCloseTo(player):
            self.isIdle = True
            self.action = self.actions["idleShoot"]
            self.isShooting = True
            self.shoot()
            self.changeOrientation(player)
        else:
            self.isShooting = False
            if self.isRight:
                if self.bounds.topleft[0] < 700:
                    self.moveRight()
                else:
                    self.isRight = False
            if not self.isRight:
                if self.bounds.topleft[0] > 20:
                    self.moveLeft()
                else:
                    self.isRight = True
