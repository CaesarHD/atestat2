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
scene = Scene()

SCROLLING_SPEED = 4

RUBIN_ENEMY_BULLET_SIZE = 3.5
RUBIN_ENEMY_BULLET_SPAWN_LOCATION = 30
RUBIN_ENEMY_SIZE = 2

resourceProvider = level.loadResourcesLevel(1)

staticBackground = Background((0, 0), 2, resourceProvider.getResource("lvl1StaticBackground"))
dinamicBackgorund = Background((0, 0), 2, resourceProvider.getResource("lvl1DinamicBackground"))
ground = Ground((0, 0), 2, resourceProvider.getResource("lvl1Ground"))

player = Character((0, 100), 2, resourceProvider.getResource("player"), 5, 42)
playerShip = Actor((0, 0), 1.5, resourceProvider.getResource("playerShip"))

mines = []
explosions = []

rubinEnemies = []
rubinEnemies = scene.rubinEnemies

ui = UI()

pos = 2000
rubinEnemies.append(
    Enemy((pos, 100), RUBIN_ENEMY_SIZE, resourceProvider.getResource("rubinEnemy"), RUBIN_ENEMY_BULLET_SIZE,
          RUBIN_ENEMY_BULLET_SPAWN_LOCATION))

playerShip.action = 0

lastUpdate = pygame.time.get_ticks()
scroll = 0
playerShip.bounds.bottom = ground.bounds.top
player.action = 15

guardian = Guardian((1000, 100), 2, resourceProvider.getResource("guardian"), 5, 42)

actors = [guardian, playerShip]

mines = player.mines

objects = [playerShip]

playerOpponents = rubinEnemies
enemyOpponents = []

running = True


def main():
    global scroll

    scene.generateEnemy()

    while running:

        clock.tick(60)

        drawEnvironment(scroll)
        ui.renderUI(player, screen)

        if not player.isShot:
            tickGame()
        else:
            gameOver()
        pygame.display.update()

    pygame.quit()


def generateExplosion(pos):
    explosions.append(Actor(pos, 2, resourceProvider.getResource('mineExplosion')))


def drawEnvironment(scroll):
    staticBackground.drawActor(screen)
    dinamicBackgorund.scrolling(screen, scroll)
    ground.scrolling(screen, scroll)
    playerShip.drawActor(screen)


def scrollActors(scroll, actors):
    for actor in actors:
        actor.scrolling(scroll)

    for mine in mines:
        mine.scrolling(scroll)

    for explosion in explosions:
        explosion.scrolling(scroll)


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
            guardian.tickAnimation()
        lastUpdate = currentTime
    player.die()
    player.drawActor(screen)
    for enemy in rubinEnemies:
        enemy.moving(player)
        enemy.drawActor(screen)
    guardian.drawActor(screen)
    for mine in mines:
        mine.drawActor(screen)


def tickGame():
    global running
    global scroll
    global lastUpdate

    updateActorsAnimation()
    handleInputEvent()
    drawCharacters()
    walkInPlace()
    player.abilityTimer()


def drawCharacters():
    global pos
    for enemy in rubinEnemies:
        if not enemy.isShot:
            enemy.gravity(ground)
            enemy.moving(player)
            enemy.drawActor(screen)
            enemy.updateBullet(objects, enemyOpponents, screen)
        else:
            enemy.die()
            if not enemy.isDead:
                enemy.drawActor(screen)
            else:
                rubinEnemies.remove(enemy)
                del enemy
                if player.bulletsReceived < 10:
                    player.bulletsReceived = player.bulletsReceived + 2

    guardian.gravity(ground)
    guardian.drawActor(screen)
    guardian.updateBullet(objects, enemyOpponents, screen)
    guardian.AI(player)

    player.gravity(ground)
    player.jump()
    player.drawActor(screen)
    player.updateBullet(objects, playerOpponents, screen)
    player.placingMine()
    player.drawMine(screen)
    mineExplosion()
    drawExplosion()


def drawExplosion():
    for explosion in explosions:
        explosion.drawActor(screen)
        if explosion.frame == 5:
            explosions.remove(explosion)
            del explosion


def mineToggleExplosion(mine):
    mine.active(player)
    mine.trigger(player, rubinEnemies)


def mineExplosion():
    global pos
    for mine in mines:
        mineToggleExplosion(mine)
        if mine.isTriggered:
            pos = mine.getExplosionCoord()
            generateExplosion(pos)
            mines.remove(mine)
            del mine


def updateActorsAnimation():
    global lastUpdate
    currentTime = pygame.time.get_ticks()
    if currentTime - lastUpdate > player.animationCooldown:
        player.tickAnimation()
        guardian.tickAnimation()
        for enemy in rubinEnemies:
            enemy.tickAnimation()
        for explosion in explosions:
            explosion.tickAnimation()
        lastUpdate = currentTime


def walkInPlace():
    offset = 2 * SCROLLING_SPEED
    if player.walkInPlaceLeft:
        for enemy in rubinEnemies:
            enemy.scrolling(offset)
        scrollActors(offset, actors)
    if player.walkInPlaceRight:
        for enemy in rubinEnemies:
            enemy.scrolling(-offset)
        scrollActors(-offset, actors)


def handleInputEvent():
    global running, scroll
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
            scroll -= SCROLLING_SPEED
            player.walkInPlaceLeft = True
            player.distanceTraveled -= SCROLLING_SPEED
        else:
            player.walkInPlaceLeft = False
        player.moveLeft()
    elif key[pygame.K_d]:
        player.walkInPlaceLeft = False
        if player.toggleScrollBackgroundRight():
            scroll += SCROLLING_SPEED
            player.walkInPlaceRight = True
            player.distanceTraveled += SCROLLING_SPEED
        else:
            player.walkInPlaceRight = False
        player.moveRight()
    else:
        player.inIdle()


if __name__ == '__main__':
    main()
