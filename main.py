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
levelController = LevelController(screen, 1)
nextLevel = False
SCROLLING_SPEED = 4

lastUpdate = pygame.time.get_ticks()

restart = False
ashes = False

lvl = 1


def main():
    global levelController
    global nextLevel
    global lvl

    levelController.generateEnemy()
    levelController.generateGuardian()
    levelController.generatePress()
    levelController.generatePipe()
    levelController.generateLaser()
    levelController.generateCable()
    levelController.generateGate()
    levelController.updateActorsList()
    levelController.updateObjectsList()
    levelController.updateRigidBodies()
    levelController.isLevelZero = True

    while levelController.running:
        nextLevel = levelController.nextLevel()
        if nextLevel:
            lvl = levelController.levelUp()
            levelController = LevelController(screen, lvl)
            levelController.generateEnemy()
            levelController.generateGuardian()
            levelController.generatePress()
            levelController.generateCable()
            levelController.generatePipe()
            levelController.generateLaser()
            levelController.generateGate()
            levelController.updateActorsList()
            levelController.updateObjectsList()
            levelController.updateRigidBodies()
            nextLevel = False

        clock.tick(60)

        levelController.drawEnvironment()

        if not levelController.player.isShot:
            levelController.tickGame()
        else:
            levelController.gameOver()
        pygame.display.update()

    pygame.quit()


if __name__ == '__main__':
    main()
