# This is a sample Python script.
import pygame

from Actor import Actor
from Background import Background
from Player import Player
from Screen import Screen
from Spritesheet import Spritesheet


# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def main():
    pygame.init()

    clock = pygame.time.Clock()

    screen = Screen(800, 600)
    playerResource = pygame.image.load('E:\\atestat\\pythonProject1\\Images\\ALIEN_FRAMES\\spritesheet.png')
    playerSpritesheet = Spritesheet(playerResource)
    player = Player((0, 100), (2, 2), playerSpritesheet, [4, 6, 4, 4, 6, 4, 3, 6, 5], 57, 57)

    backgroundResource = pygame.image.load('E:\\atestat\\pythonProject1\\Images\\ImaginiInternet\\background.webp')
    backgrounSpritesheet = Spritesheet(backgroundResource)
    background = Background((0, 0), (screen.screenWidth, screen.screenHeight), backgrounSpritesheet, [1], 1, 1)

    playerShipResource = pygame.image.load('E:\\atestat\\pythonProject1\\Images\\Alien_Ship\\spritesheet.png')
    playerShipSpritesheet = Spritesheet(playerShipResource)
    playerShip = Actor((0, 0), (1.5, 1.5), playerShipSpritesheet, [1, 1, 1], 440, 440)
    playerShip.action = 2

    lastUpdate = pygame.time.get_ticks()
    player.animationCooldown = 90

    initialPos = player.bounds.topleft[1]

    running = True

    player.action = 2

    while running:

        clock.tick(60)

        background.drawActor(screen)
        # playerShip.drawActor(screen)
        screen.blit(playerShipResource, (0, 0))

        currentTime = pygame.time.get_ticks()
        if currentTime - lastUpdate > player.animationCooldown:
            player.tickAnimation()
            lastUpdate = currentTime

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    if not player.isArmed:
                        player.isArmed = True
                    else:
                        player.isArmed = False
                if event.key == pygame.K_w and not player.isFalling and not player.isJumping:
                    initialPos = player.bounds.topleft[1]
                    player.isJumping = True

        player.gravity()
        player.jump(initialPos)

        key = pygame.key.get_pressed()

        if key[pygame.K_e] and player.isArmed and not player.isShooting:
            player.isShooting = True

        if key[pygame.K_a]:
            player.moveLeft()
        elif key[pygame.K_d]:
            player.moveRight()
        else:
            if not player.isFalling and not player.isJumping:
                player.isIdle = True
                player.inIdle()

        if player.frame >= len(player.animationList[player.action]):
            player.frame = 0
        player.drawActor(screen)

        pygame.display.update()

    pygame.quit()


if __name__ == '__main__':
    main()
