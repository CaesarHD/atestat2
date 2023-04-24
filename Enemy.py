import random

import pygame

from Character import Character

GROUND = 420
GFORCE = 10
IDLE_ACTOR_DISTANCE = 200
WALK_PLAYER_DISTANCE = 1000
PLAYER_DISTANCE = 1200


class Enemy(Character):
    def __init__(self, pos, scale, resource, bulletSize, bulletSpawnLocation, collisionOffset):
        super().__init__(pos, scale, resource, bulletSize, bulletSpawnLocation, collisionOffset)
        self.isShooting = False
        self.isJumping = False
        self.isArmed = True
        self.isPreJumping = False
        self.isLanding = False
        self.velocity = 6
        self.isShot = False
        self.isDead = False
        self.bulletsReceived = 3
        self.idleShootTiming = 500
        self.movingShootTiming = 0
        self.lastUpdate = 0

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
