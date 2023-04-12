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
RIGHT_MAP_BORDER = 1138 * 10
LEFT_MAP_BORDER = 0
SCREEN_WIDTH = 800 * 1.42
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
        self.bulletsReceived = 10
        self.animationFrames = resource.animationFrames
        self.deathLastFrame = self.animationFrames[len(self.animationFrames) - 1] - 1
        self.distanceTraveled = 0
        self.useAbility = False
        self.abilityOn = True
        self.mines = []
        self.mine = resource.mine
        self.abilityCooldown = 20000
        self.abilityLastUpdate = 0

    def changeAction(self, action):
        if not self.action == self.actions[action]:
            self.actionChanged = True
            self.frame = 0
            self.action = self.actions[action]

    def fall(self):
        self.isIdle = False
        if self.isArmed:
            if self.isShooting:
                self.shoot()
            else:
                self.changeAction("jumpArmed")
        else:
            self.changeAction("jump")

        self.gravityForce += 1.5
        self.moveDown()
        # self.isLanding = True

    def jump(self):
        if self.isJumping and not self.isFalling and not self.useAbility:
            self.isIdle = False
            # if self.isPreJumping:
            #     self.preJump()
            # else:
            if self.isArmed:
                if self.isShooting:
                    self.shoot()
                else:
                    self.changeAction("jumpArmed")
            else:
                self.changeAction("jump")

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
                self.changeAction("preJumpArmed")
            else:
                self.changeAction("preJump")
            if self.frame == 2:
                self.isPreJumping = False

    def landing(self, objects):
        if self.isLanding:
            self.bounds.bottom = objects.bounds.top
            if self.isArmed:
                self.changeAction("landingArmed")
            else:
                self.changeAction("landing")
            if self.frame == 1:
                self.isLanding = False

    def shoot(self):
        if not self.useAbility:
            if self.isIdle:
                self.changeAction("idleShoot")
                if self.frame == 2:
                    self.isShooting = False
                    self.bulletReload = False
            else:
                if self.isJumping or self.isFalling:
                    self.changeAction("jumpShoot")
                    if self.frame == 2:
                        self.isShooting = False
                        self.bulletReload = False
                else:
                    self.changeAction("walkShoot")
                    if self.frame == 5 or self.frame == 2:
                        self.isShooting = False
                        self.bulletReload = False


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
            if not self.walkInPlaceLeft and not self.bounds.x <= LEFT_MAP_BORDER:
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
            if not self.walkInPlaceRight and not self.bounds.x >= (SCREEN_WIDTH - self.bounds.size[1]):
                initial = self.bounds.topleft
                self.bounds.topleft = (initial[0] + self.velocity, initial[1])

    def inIdle(self):
        if not self.useAbility:
            self.walkInPlaceRight = False
            self.walkInPlaceLeft = False
            if not self.isFalling and not self.isJumping:
                self.isIdle = True

                if self.isShooting:
                    self.shoot()
                else:
                    if self.isArmed:
                        self.changeAction("idleArmed")
                    else:
                        self.changeAction("idle")

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
        if not self.isFalling and not self.isJumping and not self.useAbility:
            self.isJumping = True
            self.isPreJumping = True
            self.preJumpPosition = self.bounds.topleft[1]

    def toggleShooting(self):
        if self.isArmed and not self.isShooting and not self.useAbility:
            self.isShooting = True

    def toggleScrollBackgroundRight(self):
        return self.bounds.x >= RIGHT_SCROLL_BOUNDARY and self.distanceTraveled < (
                    RIGHT_MAP_BORDER - RIGHT_SCROLL_BOUNDARY - self.bounds.size[1]) and not self.useAbility

    def toggleScrollBackgroundLeft(self):
        return self.bounds.x <= LEFT_SCROLL_BOUNDARY and self.distanceTraveled > 0 and not self.useAbility

    def abilityTimer(self):
        if not self.abilityOn:
            currentTime = pygame.time.get_ticks()
            if currentTime - self.abilityLastUpdate > self.abilityCooldown:
                self.abilityOn = True
                self.abilityLastUpdate = currentTime

    def toggleAbility(self):
        if self.abilityOn and not self.isJumping and not self.isFalling and not self.useAbility:
            self.useAbility = True

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
            self.changeAction("deadInAir")
        else:
            self.changeAction("dead")
        if not self.isDead:
            if self.frame == self.deathLastFrame:
                self.isDead = True

    def generateMine(self):
        if self.isLeft:
            pos = (self.bounds.x + 21, self.bounds.bottom - 12)
        else:
            pos = (self.bounds.x + 51, self.bounds.bottom - 12)
        self.mines.append(Mine(pos, 2, self.mine))

    def placingMine(self):
        if self.useAbility:
            self.abilityOn = False
            self.changeAction("placingMine")
            if self.frame == 4:
                self.generateMine()
            if self.frame == 5:
                self.useAbility = False

    def drawMine(self, screen):
        for mine in self.mines:
            mine.drawActor(screen)
