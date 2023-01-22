# This is a sample Python script.
import pygame

from Actor import Actor
from Player import Player
from Screen import Screen

pygame.init()

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

screen = Screen(800, 600)
playerSpritesheet = pygame.image.load('E:\\atestat\\VITAEX\\Images\\ALIEN_FRAMES\\spritesheet (4).png')

player = Player((0, 0), (5, 5), playerSpritesheet)

background = Actor((0, 0), (screen.screenWidth, screen.screenHeight))
backgroundImage = pygame.image.load('E:\\atestat\\VITAEX\\Images\\ImaginiInternet\\background.webp')
backgroundImage = pygame.transform.scale(backgroundImage, background.size)

lastUpdate = pygame.time.get_ticks()
animationCooldown = 120


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')


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