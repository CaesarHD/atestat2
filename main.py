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
from Scene import Scene
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
lvl = 1
rubinEnemyPositions = [3000, 4000, 4500, 5500, 6000, 6100, 7000, 7200, 7500, 9000, 9500, 10000, 10100,
                               12000, 13000, 13100, 14500, 14900, 17000, 17100, 17200, 17800, 20000, 20100, 20500, 21000, 21050, 21100, 21500, 22000]
resourceProvider = level.loadResourcesLevel(1)
player = Character((0, 100), 2, resourceProvider.getResource("player"), 5, 42, (50, 0))
actors = []
scene = Scene(screen, player, rubinEnemyPositions, lvl, actors)

SCROLLING_SPEED = 4

# playerShip = Actor((0, 0), 1.5, resourceProvider.getResource("playerShip"), None)

rubinEnemies = scene.rubinEnemies

ui = UI()

explosionPos = 2000

lastUpdate = pygame.time.get_ticks()
scroll = 0
# playerShip.bounds.bottom = ground.bounds.top

# guardian = Guardian((1000, 100), 2, resourceProvider.getResource("guardian"), 5, 42, (15, 0))


running = True


def main():

    scene.generateEnemy()

    while running:

        clock.tick(60)

        scene.drawEnvironment()
        ui.renderUI(player, screen)

        if not player.isShot:
            tickGame()
        else:
            gameOver()
        pygame.display.update()

    pygame.quit()



def gameOver():
    global running
    global lastUpdate

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    currentTime = pygame.time.get_ticks()
    if currentTime - lastUpdate > player.animationCooldown:
        if not player.isDead:
            player.tickAnimation()
        for enemy in rubinEnemies:
            enemy.tickAnimation()
        lastUpdate = currentTime
    player.die()
    player.drawActor(screen)
    for enemy in rubinEnemies:
        enemy.moving(player)
        enemy.drawActor(screen)
    for mine in mines:
        mine.drawActor(screen)
    scene.updateActorsAnimation()


def tickGame():
    scene.updateActorsAnimation()
    player.abilityTimer()
    handleInputEvent()
    scene.drawCharacters()
    walkInPlace()


def walkInPlace():
    offset = 2 * SCROLLING_SPEED
    if player.walkInPlaceLeft:
        for enemy in rubinEnemies:
            enemy.scrolling(offset)
        scene.scrollActors(offset)
    if player.walkInPlaceRight:
        for enemy in rubinEnemies:
            enemy.scrolling(-offset)
        scene.scrollActors(-offset)


def handleInputEvent():
    global running
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            match event.key:
                case pygame.K_q:
                    player.toggleWeapon()
                case pygame.K_w:
                    player.toggleJump()
                case pygame.K_e:
                    player.toggleAbility()

    key = pygame.key.get_pressed()
    if key[pygame.K_SPACE]:
        player.toggleShooting()
    if key[pygame.K_a]:
        player.walkInPlaceRight = False
        if player.toggleScrollBackgroundLeft():
            scene.scroll -= SCROLLING_SPEED
            player.walkInPlaceLeft = True
            player.distanceTraveled -= SCROLLING_SPEED
        else:
            player.walkInPlaceLeft = False
        player.moveLeft()
    elif key[pygame.K_d]:
        player.walkInPlaceLeft = False
        if player.toggleScrollBackgroundRight():
            scene.scroll += SCROLLING_SPEED
            player.walkInPlaceRight = True
            player.distanceTraveled += SCROLLING_SPEED
        else:
            player.walkInPlaceRight = False
        player.moveRight()
    else:
        player.inIdle()


if __name__ == '__main__':
    main()
