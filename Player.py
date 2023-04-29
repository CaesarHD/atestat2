from Character import Character
import pygame

SCROLLING_SPEED = 4


class Player(Character):
    def __init__(self, pos, scale, resource, bulletSize, bulletSpawnLocation, bulletDamage, collisionOffset):
        super().__init__(pos, scale, resource, bulletSize, bulletSpawnLocation, bulletDamage, collisionOffset)
        self.scrollingSpeed = SCROLLING_SPEED
        self.scroll = 0

    def keyPessedInputEvent(self):
        key = pygame.key.get_pressed()
        if key[pygame.K_SPACE]:
            self.toggleShooting()
        if key[pygame.K_a]:
            self.walkInPlaceRight = False
            if self.toggleScrollBackgroundLeft():
                if not self.isBlocked:
                    self.scroll -= self.scrollingSpeed
                    self.distanceTraveled -= self.scrollingSpeed
                self.walkInPlaceLeft = True
            else:
                self.walkInPlaceLeft = False
            self.moveLeft()
        elif key[pygame.K_d]:
            self.walkInPlaceLeft = False
            if self.toggleScrollBackgroundRight():
                if not self.isBlocked:
                    self.scroll += self.scrollingSpeed
                    self.distanceTraveled += self.scrollingSpeed
                self.walkInPlaceRight = True
            else:
                self.walkInPlaceRight = False
            self.moveRight()
        else:
            self.inIdle()

    def keyDownInputEvent(self, event):
        if event.type == pygame.KEYDOWN:
            match event.key:
                case pygame.K_q:
                    self.toggleWeapon()
                case pygame.K_w:
                    self.toggleJump()
                case pygame.K_e:
                    self.toggleAbility()
