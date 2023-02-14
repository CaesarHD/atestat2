# This is a sample Python script.
import pygame

from Actor import Actor
from Background import Background
from Enemy import Enemy
from Player import Player
from Screen import Screen
from Spritesheet import Spritesheet


# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


# noinspection SpellCheckingInspection
def main():
    pygame.init()

    clock = pygame.time.Clock()

    screen = Screen(800, 600)
    playerResource = pygame.image.load('E:\\atestat\\pythonProject1\\Images\\ALIEN_FRAMES\\spritesheet.png')
    playerSpritesheet = Spritesheet(playerResource, 57, 57)
    player = Player((0, 100), (2, 2), playerSpritesheet, [4, 6, 3, 1, 2, 4, 6, 3, 1, 2, 3, 6, 2, 3], 2)

    backgroundResource = pygame.image.load('E:\\atestat\\pythonProject1\\Images\\ImaginiInternet\\background.webp')
    backgroundSpritesheet = Spritesheet(backgroundResource, 3840, 2304)
    background = Background((0, 0), (screen.screenWidth, screen.screenHeight), backgroundSpritesheet, [1], 1)

    playerShipResource = pygame.image.load('E:\\atestat\\pythonProject1\\Images\\Alien_Ship\\spritesheet.png')
    playerShipSpritesheet = Spritesheet(playerShipResource, 440, 440)
    playerShip = Actor((0, 0), (1.5, 1.5), playerShipSpritesheet, [1, 1, 1, 1], 1.5)

    enemyResource = pygame.image.load('E:\\atestat\\pythonProject1\\Images\\ENEMY_FRAMES\\spritesheet.png')
    enemySpritesheet = Spritesheet(enemyResource, 57, 57)
    enemy = Enemy((400, 100), (2, 2), enemySpritesheet, [6, 4, 3, 4], 2)

    playerShip.action = 2

    lastUpdate = pygame.time.get_ticks()
    player.animationCooldown = 90


    running = True

    player.action = 3
    enemy.action = 2
    enemy.isLeft = True
    enemy.isRight = False

    while running:

        clock.tick(60)

        background.drawActor(screen)
        playerShip.drawActor(screen)

        currentTime = pygame.time.get_ticks()
        if currentTime - lastUpdate > player.animationCooldown:
            player.tickAnimation()
            enemy.tickAnimation()
            lastUpdate = currentTime

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                match event.key:
                    case pygame.K_q: player.toggleWeapon()
                    case pygame.K_w: player.toggleJump()

        player.gravity()
        enemy.gravity()
        enemy.moving()

        key = pygame.key.get_pressed()

        if key[pygame.K_e]:
            player.toggleShooting()
        if key[pygame.K_a]:
            player.moveLeft()
        elif key[pygame.K_d]:
            player.moveRight()
        else:
            player.inIdle()

        player.jump()

        enemy.drawActor(screen)

        player.drawActor(screen)

        pygame.display.update()

    pygame.quit()



if __name__ == '__main__':
    main()
