# This is a sample Python script.
import pygame

from Actor import Actor
from Player import Player
from Screen import Screen

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.



def main():
    pygame.init()

    screen = Screen(800, 600)
    playerSpritesheet = pygame.image.load('E:\\atestat\\pythonProject1\\Images\\ALIEN_FRAMES\\spritesheet (4).png')

    player = Player((0, 0), (5, 5), playerSpritesheet)

    background = Actor((0, 0), (screen.screenWidth, screen.screenHeight))
    backgroundImage = pygame.image.load('E:\\atestat\\pythonProject1\\Images\\ImaginiInternet\\background.webp')
    backgroundImage = pygame.transform.scale(backgroundImage, background.size)

    lastUpdate = pygame.time.get_ticks()
    animationCooldown = 120


    running = True


    player.action = 4

    while running:

        background.drawActor(backgroundImage, screen, (0, 0))

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


