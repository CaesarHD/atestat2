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
    playerResource = pygame.image.load('E:\\atestat\\pythonProject1\\Images\\ALIEN_FRAMES\\spritesheet (4).png')
    playerSpritesheet = Spritesheet(playerResource)
    player = Player((0, 100), (1, 1), playerSpritesheet, [4, 4, 5, 1, 6], 57, 57)

    backgroundResource = pygame.image.load('E:\\atestat\\pythonProject1\\Images\\ImaginiInternet\\background.webp')
    backgrounSpritesheet = Spritesheet(backgroundResource)
    background = Background((0, 0), (screen.screenWidth, screen.screenHeight), backgrounSpritesheet, [1], 1, 1)

    lastUpdate = pygame.time.get_ticks()
    animationCooldown = 120

    initialPos = player.bounds.topleft[1]

    running = True

    player.action = 2

    while running:

        clock.tick(60)

        background.drawActor(screen)

        if player.frame >= len(player.animationList[player.action]):
            player.frame = 0

        currentTime = pygame.time.get_ticks()
        if currentTime - lastUpdate > animationCooldown:
            player.tickAnimation()
            lastUpdate = currentTime

        player.drawActor(screen)

        if player.bounds.topleft[1] < 520 and not player.isJumping:
            player.isFalling = True
        else:
            player.isFalling = False
            player.action = 1

        player.fall()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w and not player.isFalling and not player.isJumping:
                    initialPos = player.bounds.topleft[1]
                    player.isJumping = True

        player.jump(initialPos)

        key = pygame.key.get_pressed()
        if key[pygame.K_a]:
            if not player.isJumping and not player.isFalling:
                player.action = 4
            player.moveLeft()
        elif key[pygame.K_d]:
            if not player.isJumping and not player.isFalling:
                player.action = 4
            player.moveRight()

        pygame.display.update()

    pygame.quit()


if __name__ == '__main__':
    main()
