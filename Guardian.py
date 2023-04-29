from Character import Character


class Guardian(Character):
    def __init__(self, pos, scale, resource, bulletSize, bulletSpawnLocation, bulletDamage, collisionOffset):
        super().__init__(pos, scale, resource, bulletSize, bulletSpawnLocation, bulletDamage, collisionOffset)
        self.isShooting = True
        self.isJumping = False
        self.isArmed = True
        self.isPreJumping = False
        self.isLanding = False
        self.velocity = 6
        self.isShot = True
        self.isDead = False
        self.isShooting = False
        self.isLeft = True
        self.isRight = False

    def shoot(self):
        if self.isShooting:
            self.action = self.actions["idleShoot"]
            if self.frame == 2:
                self.isShooting = False
                self.bulletReload = False
                self.action = self.actions["idleArmed"]

    def working(self, gate, objects, player):
        self.gravity(objects)
        if gate.isOpening and player.getCollisionBox().x < gate.gateWall.getCollisionBox().x and gate.dinamicGate.getCollisionBox().top > -20:
            self.isShooting = True

        if self.isShooting:
            self.shoot()
        else:
            self.isShooting = False
            self.isIdle = True
            self.inIdle()
