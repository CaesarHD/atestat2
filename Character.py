from Bullet import Bullet
from Mine import Mine
from ResourceProvider import ResourceProvider
import pygame
from pygame import Rect

from Actor import Actor
from Spritesheet import Spritesheet

RIGHT_SCROLL_BOUNDARY = 600
LEFT_SCROLL_BOUNDARY = 400

GROUND = 420
JUMP_HEIGHT = 150
GFORCE = 10
RIGHT_MAP_BORDER = 1138*10
LEFT_MAP_BORDER = 0
SCREEN_WIDTH = 800*1.42
PLAYER_OFFSET = 4


class Character(Actor):

    def __init__(self, pos, scale, resource, bulletSize, bulletSpawnLocation):
        super().__init__(pos, scale, resource)
        self.preJumpPosition = GROUND
        self.isShooting = False
        self.isJumping = False
        self.isArmed = False
        self.isPreJumping = False
        self.isLanding = False
        self.velocity = 8
        self.actions = resource.actions
        self.walkInPlaceRight = False
        self.walkInPlaceLeft = False
        self.bulletReload = False
        self.isShot = False
        self.isDead = False
        self.bullets = []
        self.bullet = resource.bullet
        self.bulletSpawnLocation = bulletSpawnLocation
        self.bulletSize = bulletSize
        self.bulletsReceived = 7
        self.animationFrames = resource.animationFrames
        self.deathLastFrame = self.animationFrames[len(self.animationFrames) - 1] - 1
        self.distanceTraveled = 0
        # self.mine = Mine()

    def fall(self):
        self.isIdle = False
        if self.isArmed:
            self.action = self.actions["jumpArmed"]
            if self.isShooting:
                self.shoot()
        else:
            self.action = self.actions["jump"]

        self.gravityForce += 1.5
        self.moveDown()
        # self.isLanding = True

    def jump(self):
        if self.isJumping and not self.isFalling:
            self.isIdle = False
            if self.isPreJumping:
                self.preJump()
            else:
                if self.isArmed:
                    self.action = self.actions["jumpArmed"]
                    if self.isShooting:
                        self.shoot()
                else:
                    self.action = self.actions["jump"]

            # TODO: calculate this based on JUMP_HEIGHT
            self.gravityForce -= 0.3
            if self.gravityForce <= 0.1:
                self.gravityForce = 0.1

            self.moveUp()
            currentPos = self.bounds.topleft[1]
            if self.preJumpPosition - currentPos > JUMP_HEIGHT:
                self.isJumping = False

    def preJump(self):
        if self.isPreJumping:
            if self.isArmed:
                self.action = self.actions["preJumpArmed"]
            else:
                self.action = self.actions["preJump"]
            if self.frame == 2:
                self.isPreJumping = False

    def landing(self, objects):
        if self.isLanding:
            self.bounds.bottom = objects.bounds.top
            if self.isArmed:
                self.action = self.actions["landingArmed"]
            else:
                self.action = self.actions["landing"]
            if self.frame == 1:
                self.isLanding = False

    def shoot(self):
        if self.isIdle:
            self.action = self.actions["idleShoot"]
            if self.frame == 2:
                self.isShooting = False
                self.bulletReload = False
        else:
            if self.isJumping or self.isFalling:
                self.action = self.actions["jumpShoot"]
                if self.frame == 2:
                    self.isShooting = False
                    self.bulletReload = False
            else:
                self.action = self.actions["walkShoot"]
                if self.frame == 5 or self.frame == 2:
                    self.isShooting = False
                    self.bulletReload = False

    def moveLeft(self):
        self.isLeft = True
        self.isRight = False
        self.isIdle = False
        if not self.isJumping and not self.isFalling and not self.isShooting:
            if not self.isArmed:
                self.action = self.actions["walk"]
            else:
                self.action = self.actions["walkArmed"]
        if self.isShooting:
            self.shoot()
        if not self.walkInPlaceLeft and not self.bounds.x <= LEFT_MAP_BORDER:
            initial = self.bounds.topleft
            self.bounds.topleft = (initial[0] - self.velocity, initial[1])

    def moveRight(self):
        self.isIdle = False
        self.isRight = True
        self.isLeft = False
        if not self.isJumping and not self.isFalling and not self.isShooting:
            if not self.isArmed:
                self.action = self.actions["walk"]
            else:
                self.action = self.actions["walkArmed"]
        if self.isShooting:
            self.shoot()
        if not self.walkInPlaceRight and not self.bounds.x >= (SCREEN_WIDTH - self.bounds.size[1]):
            initial = self.bounds.topleft
            self.bounds.topleft = (initial[0] + self.velocity, initial[1])


    def inIdle(self):
        self.walkInPlaceRight = False
        self.walkInPlaceLeft = False
        if not self.isFalling and not self.isJumping:
            self.isIdle = True

            if self.isShooting:
                self.shoot()
            else:
                if self.isArmed:
                    self.action = self.actions["idleArmed"]
                else:
                    self.action = self.actions["idle"]

    def moveUp(self):
        initial = self.bounds.topleft
        self.bounds.topleft = (initial[0], initial[1] - self.gravityForce)

    def moveDown(self):
        initial = self.bounds.topleft
        self.bounds.topleft = (initial[0], initial[1] + self.gravityForce)

    def isCollideWith(self, obstacle):
        return self.bounds.colliderect(obstacle.bounds)

    def isOnObject(self, obstacle):
        return self.bounds.bottom + self.gravityForce > obstacle.bounds.top

    def placeCharacterOnObject(self, obstacle):
        self.bounds.bottom = obstacle.bounds.top

    def gravity(self, obstacle):
        if not self.isOnObject(obstacle):
            if not self.isJumping:
                self.isFalling = True
                self.isIdle = False
                self.fall()
        else:
            self.placeCharacterOnObject(obstacle)
            self.isFalling = False
            self.gravityForce = GFORCE

    def toggleWeapon(self):
        self.isArmed = not self.isArmed

    def toggleJump(self):
        if not self.isFalling and not self.isJumping:
            self.isJumping = True
            self.isPreJumping = True
            self.preJumpPosition = self.bounds.topleft[1]

    def toggleShooting(self):
        if self.isArmed and not self.isShooting:
            self.isShooting = True

    def toggleScrollBackgroundRight(self):
        return self.bounds.x >= RIGHT_SCROLL_BOUNDARY and self.distanceTraveled < (RIGHT_MAP_BORDER - RIGHT_SCROLL_BOUNDARY - self.bounds.size[1])

    def toggleScrollBackgroundLeft(self):
        return self.bounds.x <= LEFT_SCROLL_BOUNDARY and self.distanceTraveled > 0

    def updateBullet(self, objects, characters, screen):
        if self.isShooting and not self.bulletReload:
            self.bullets.append(
                Bullet((self.bounds.x, self.bounds.y + self.bulletSpawnLocation), self.bulletSize, self.bullet,
                       self.isRight))
            self.bulletReload = True
        for bullet in self.bullets:
            if not bullet.out:
                bullet.propell(objects, characters, screen)
                bullet.drawActor(screen)
            else:
                self.bullets.remove(bullet)
                del bullet
    def die(self):
        if self.isJumping or self.isFalling:
            self.action = self.actions["deadInAir"]
        else:
            self.action = self.actions["dead"]
        if not self.isDead:
            if self.frame == self.deathLastFrame:
                self.isDead = True
    
    def placingMine(self):
        self.isIdle = False
        self.action = self.actions["placingMine"]


