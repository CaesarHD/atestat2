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

ashes = False


lvl = 1


def main():
    global levelController
    global nextLevel
    global lvl

    levelController.generateEnemy()
    levelController.generateGuardian()
    levelController.generatePress()
    levelController.generateCable()
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
            levelController.updateActorsList()
            levelController.updateObjectsList()
            levelController.updateRigidBodies()
            nextLevel = False

        clock.tick(60)

        levelController.drawEnvironment()

        if not levelController.player.isShot:
            levelController.tickGame()
        else:
            gameOver()

        pygame.display.update()

    pygame.quit()


def gameOver():
    global lastUpdate
    global ashes

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            levelController.running = False
    currentTime = pygame.time.get_ticks()
    if currentTime - lastUpdate > levelController.player.animationCooldown:
        if not levelController.player.isDead:
            levelController.updateActorsAnimation()
            levelController.ui.renderUI(levelController.player, levelController.screen)
        lastUpdate = currentTime
    levelController.player.die()
    levelController.player.drawActor(screen)
    levelController.drawObjects()
    levelController.drawCharacters()
    levelController.movingPresses()
    levelController.updateActorsAnimation()
    if levelController.player.frame == levelController.player.deathLastFrame and not ashes:
        ashes = True
    if ashes:
        levelController.player.frame = levelController.player.deathLastFrame
    levelController.ui.renderUI(levelController.player, levelController.screen)


if __name__ == '__main__':
    main()
