from Actor import Actor
import pygame


class Bullet(Actor):
    def __init__(self, pos, scale, resource, isRight, damage):
        super().__init__(pos, scale, resource, None)
        self.isRight = isRight
        self.out = False

        if self.isRight:
            self.bounds.x += 30
        else:
            self.bounds.x -= 50
        self.damage = damage

    def collideWithObjects(self, objects, characters, screen):
        return self.collideWithActors(objects) or self.collideWithActors(characters) or self.collideWithScreen(screen)

    def collideWithCharacters(self, characters):
        for character in characters:
            if (abs(self.bounds.x - character.bounds.x) < 60 and
                (self.bounds.top >= character.bounds.top)) and \
                    (self.bounds.bottom <= character.bounds.bottom):
                character.bulletsReceived = character.bulletsReceived - self.damage
            if character.bulletsReceived == 0:
                character.isShot = True

    def collideWithActors(self, actors):
        for actor in actors:
            if (abs(self.bounds.x - actor.bounds.x) < 60 and
                (self.bounds.top >= actor.bounds.top)) and \
                    (self.bounds.bottom <= actor.bounds.bottom):
                return True

    def collideWithScreen(self, screen):
        return self.bounds.x > screen.screenWidth or self.bounds.x < 0

    def propell(self, objects, characters, screen):
        if not self.collideWithObjects(objects, characters, screen):
            if self.isRight:
                self.moveRight(40)
            else:
                self.moveLeft(40)
        elif self.collideWithCharacters(characters):
            self.out = True

        else:
            self.out = True
