from Character import Character


class Guardian(Character):
    def __init__(self, pos, scale, resource, bulletSize, bulletSpawnLocation, collisionOffset):
        super().__init__(pos, scale, resource, bulletSize, bulletSpawnLocation, collisionOffset)
        self.isShooting = True
        self.isJumping = False
        self.isArmed = True
        self.isPreJumping = False
        self.isLanding = False
        self.velocity = 6
        self.isShot = True
        self.isDead = False

    def shoot(self):
        if self.isShooting:
            self.action = self.actions["idleShoot"]
            if self.frame == 2:
                self.isShooting = False
                self.bulletReload = False
                self.action = self.actions["idleArmed"]

    def AI(self, player):
        if abs(player.bounds.x - self.bounds.x) < 200:
            self.isShooting = True
            self.shoot()
        else:
            self.isShooting = False
            self.isIdle = True
            self.inIdle()

