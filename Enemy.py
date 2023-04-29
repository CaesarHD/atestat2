import random

import pygame

from Character import Character

GROUND = 420
GFORCE = 10
IDLE_ACTOR_DISTANCE = 200
WALK_PLAYER_DISTANCE = 1000
PLAYER_DISTANCE = 1200
lastUpdate = 0

class Enemy(Character):
    def __init__(self, pos, scale, resource, bulletSize, bulletSpawnLocation, bulletDamage, collisionOffset):
        super().__init__(pos, scale, resource, bulletSize, bulletSpawnLocation, bulletDamage, collisionOffset)
        self.isShooting = False
        self.isJumping = False
        self.isArmed = True
        self.isPreJumping = False
        self.isLanding = False
        self.velocity = 6
        self.isShot = False
        self.isDead = False
        self.bulletsReceived = 4
        self.idleShootTiming = 500
        self.movingShootTiming = 0
        self.lastUpdate = 0
        self.startGoing = False

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

    def moveLeft(self):
        self.isLeft = True
        self.isRight = False
        self.isIdle = False
        if not self.useAbility:
            if not self.isJumping and not self.isFalling and not self.isShooting:
                if not self.isArmed:
                    self.changeAction("walk")
                else:
                    self.changeAction("walkArmed")
            if self.isShooting:
                self.shoot()
            if not self.walkInPlaceLeft:
                initial = self.bounds.topleft
                self.bounds.topleft = (initial[0] - self.velocity, initial[1])

    def moveRight(self):
        self.isIdle = False
        self.isRight = True
        self.isLeft = False
        if not self.useAbility:
            if not self.isJumping and not self.isFalling and not self.isShooting:
                if not self.isArmed:
                    self.changeAction("walk")
                else:
                    self.changeAction("walkArmed")
            if self.isShooting:
                self.shoot()
            if not self.walkInPlaceRight:
                initial = self.bounds.topleft
                self.bounds.topleft = (initial[0] + self.velocity, initial[1])

    def tickShoot(self, time):
        currentTime = pygame.time.get_ticks()
        if currentTime - self.lastUpdate > time:
            self.isShooting = True
            self.lastUpdate = currentTime
        else:
            self.isShooting = False

    def shootAndMoving(self, player):
        self.isIdle = False
        if self.isCloseTo(player, WALK_PLAYER_DISTANCE):
            self.movingShootTiming = random.randint(1000, 4000)
            if not self.isShooting:
                self.tickShoot(self.movingShootTiming)
        if self.isRight:
            self.moveRight()
        else:
            self.moveLeft()

    def moving(self, player):
        global lastUpdate
        if not player.isShot:
            if self.bounds.x > player.bounds.x:
                if self.isCloseTo(player, PLAYER_DISTANCE):
                    if self.isCloseTo(player, IDLE_ACTOR_DISTANCE):
                        if not self.isShooting:
                            self.tickShoot(self.idleShootTiming)
                        self.inIdle()
                    else:
                        self.shootAndMoving(player)
                    self.changeOrientation(player)
            else:
                if self.isCloseTo(player, IDLE_ACTOR_DISTANCE):
                    if not self.isShooting:
                        self.tickShoot(self.idleShootTiming)
                    self.inIdle()
                else:
                    self.shootAndMoving(player)
                self.changeOrientation(player)
        else:
            if self.isCloseTo(player, 1500):
                if not self.startGoing:
                    self.inIdle()
                time = random.randint(1000, 5000)
                if lastUpdate == 0:
                    lastUpdate = pygame.time.get_ticks()
                currentTime = pygame.time.get_ticks()
                if currentTime - lastUpdate > time:
                    self.startGoing = True
                    lastUpdate = currentTime
                if self.startGoing:
                    self.isIdle = False
                    self.moveLeft()
