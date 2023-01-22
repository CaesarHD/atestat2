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

    screen = Screen(800, 600)
    playerResource = pygame.image.load('E:\\atestat\\pythonProject1\\Images\\ALIEN_FRAMES\\spritesheet (4).png')
    playerSpritesheet = Spritesheet(playerResource)
    player = Player((0, 0), (5, 5), playerSpritesheet)

    backgroundResource = pygame.image.load('E:\\atestat\\pythonProject1\\Images\\ImaginiInternet\\background.webp')
    backgrounSpritesheet = Spritesheet(backgroundResource)
    background = Background((0, 0), (screen.screenWidth, screen.screenHeight), backgrounSpritesheet)


    lastUpdate = pygame.time.get_ticks()
    animationCooldown = 120


    running = True


    player.action = 4

    while running:

        background.drawActor(screen, (0, 0))

        currentTime = pygame.time.get_ticks()
        if currentTime - lastUpdate > animationCooldown:
            player.tickAnimation()
            lastUpdate = currentTime
        player.draw(screen, (0, 0))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        pygame.display.update()

    pygame.quit()




if __name__ == '__main__':
    main()


