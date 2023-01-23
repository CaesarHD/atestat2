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
    player = Player((0, 100), (2, 2), playerSpritesheet, [4, 4, 5, 1, 6], 57, 57)

    backgroundResource = pygame.image.load('E:\\atestat\\pythonProject1\\Images\\ImaginiInternet\\background.webp')
    backgrounSpritesheet = Spritesheet(backgroundResource)
    background = Background((0, 0), (screen.screenWidth, screen.screenHeight), backgrounSpritesheet, [1], 1, 1)


    lastUpdate = pygame.time.get_ticks()
    animationCooldown = 120


    running = True

    player.action = 1

    while running:


        clock.tick(60)

        background.drawActor(screen)

        currentTime = pygame.time.get_ticks()
        if currentTime - lastUpdate > animationCooldown:
            player.tickAnimation()
            lastUpdate = currentTime
        player.drawActor(screen)

        if player.bounds.topleft[1] < 450:
            player.moveDown()


        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w:
                    player.moveUp()

        key = pygame.key.get_pressed()
        if key[pygame.K_a]:
            player.moveLeft()
            player.action = 4
        elif key[pygame.K_d]:
            player.moveRight()
            player.action = 4
        else:
            player.action = 1
            player.frame = 0
        pygame.display.update()

    pygame.quit()




if __name__ == '__main__':
    main()


