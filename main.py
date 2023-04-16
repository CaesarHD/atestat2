# This is a sample Python script.
from Bullet import Bullet
import pygame

from Actions import Actions
from Actor import Actor
from Background import Background
from Enemy import Enemy
from Character import Character
from Ground import Ground
from Guardian import Guardian
from Levels import Levels
from ResourceProvider import ResourceProvider
from LevelController import LevelController
from Screen import Screen
from Spritesheet import Spritesheet
from Icons import Icons
from UI import UI

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


# noinspection SpellCheckingInspection
pygame.init()

clock = pygame.time.Clock()
screen = Screen(800 * 1.42, 480 * 1.33)
level = Levels()
actors = []
levelController = LevelController(screen, actors)
nextLevel = False
SCROLLING_SPEED = 4

# playerShip = Actor((0, 0), 1.5, resourceProvider.getResource("playerShip"), None)

rubinEnemies = levelController.rubinEnemies

lastUpdate = pygame.time.get_ticks()

# guardian = Guardian((1000, 100), 2, resourceProvider.getResource("guardian"), 5, 42, (15, 0))

levelController = LevelController(screen, actors)


def main():
    global levelController
    global nextLevel

    levelController.generateEnemy()
    levelController.generateGuardian()
    levelController.generatePress()
    levelController.generateCable()
    levelController.updateActorsList()
    levelController.updateObjectsList()
    levelController.updateRigidBodies()

    while levelController.running:
        if nextLevel:
            levelController.levelUp()
            levelController = LevelController(screen, actors)
            levelController.generateEnemy()
            nextLevel = False

        clock.tick(60)

        levelController.drawEnvironment()

        if not levelController.player.isShot:
            levelController.tickGame()
        else:
            gameOver()

        levelController.ui.renderUI(levelController.player, levelController.screen)

        pygame.display.update()

    pygame.quit()


def gameOver():
    global lastUpdate

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            levelController.running = False
    currentTime = pygame.time.get_ticks()
    if currentTime - lastUpdate > levelController.player.animationCooldown:
        if not levelController.player.isDead:
            levelController.player.tickAnimation()
        for enemy in levelController.rubinEnemies:
            enemy.tickAnimation()
        lastUpdate = currentTime
    levelController.player.die()
    levelController.player.drawActor(screen)
    for enemy in levelController.rubinEnemies:
        enemy.moving(levelController.player)
        enemy.drawActor(levelController.screen)
    for mine in levelController.mines:
        mine.drawActor(levelController.screen)
    levelController.updateActorsAnimation()


if __name__ == '__main__':
    main()
