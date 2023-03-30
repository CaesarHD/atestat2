from Bullet import Bullet
from ResourceProvider import ResourceProvider
import pygame
from pygame import Rect

from Actor import Actor
from Spritesheet import Spritesheet

GROUND = 420
JUMP_HEIGHT = 150
GFORCE = 10


class Character(Actor):

    def __init__(self, pos, scale, resource):
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
        self.isDead = False
        self.bullets = []

    def updateActorBullets(self, actor):
        if actor.isShooting and not actor.bulletReload:
            self.bullets.append(
                Bullet((actor.bounds.x, actor.bounds.y + 42), 5, resourceProvider.getResource(bulletResource),
                       actor.isRight))
            actor.bulletReload = True

        for bullet in bullets:
            if not bullet.out:
                bullet.propell(screen, enemy)
                bullet.drawActor(screen)
                pygame.draw.rect(screen.screen, (255, 0, 0), bullet.bounds)
            else:
                del bullet

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
                if self.frame == 0:
                    self.bulletReload = False
                if self.frame == 3:
                    self.bulletReload = False
                if self.frame == 5:
                    self.isShooting = False
                    self.bulletReload = False

    def moveLeft(self):
        self.walkInPlaceRight = False
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
        if not self.walkInPlaceLeft:
            initial = self.bounds.topleft
            self.bounds.topleft = (initial[0] - self.velocity, initial[1])

    def moveRight(self):
        self.walkInPlaceLeft = False
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
        if not self.walkInPlaceRight:
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
        return self.bounds.x > 600

    def toggleScrollBackgroundLeft(self):
        return self.bounds.x < 400

    def die(self):
        self.action = self.actions["dead"]


    def drawActor(self, screen):
        super().drawActor(screen)
        updateBullets(screen)
        
        