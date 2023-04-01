# This is a sample Python script.
from Bullet import Bullet
import pygame

from Actions import Actions
from Actor import Actor
from Background import Background
from Enemy import Enemy
from Character import Character
from Ground import Ground
from Levels import Levels
from ResourceProvider import ResourceProvider
from Screen import Screen
from Spritesheet import Spritesheet


# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


# noinspection SpellCheckingInspection
pygame.init()

clock = pygame.time.Clock()
screen = Screen(800*1.42, 480*1.33)
# level = Levels()
resourceProvider = ResourceProvider()
action = Actions()
resourceProvider.registerResource("playerBullet", 'Images/Bullet/player_bullet.png', [1], (28, 5), None, None)
resourceProvider.registerResource("rubinBullet", 'Images/Bullet/enemy_bullet.png', [1], (28, 5), None, None)
playerBullet = resourceProvider.getResource("playerBullet")
rubinBullet = resourceProvider.getResource("rubinBullet")
resourceProvider.registerResource("rubinEnemy", 'Images/ENEMY_FRAMES/spritesheet.png', [6, 4, 3, 4, 5], (57, 57), action.getActions("rubinEnemy"), rubinBullet)
resourceProvider.registerResource("player", 'Images/ALIEN_FRAMES/spritesheet.png', [4, 6, 3, 1, 2, 4, 6, 3, 1, 2, 3, 6, 2, 3, 2, 6], (57, 57), action.getActions("player"), playerBullet)
resourceProvider.registerResource("playerShip", 'Images/Alien_Ship/spritesheet.png', [1, 1, 1, 1], (485, 197), action.getActions("playerShip"), None)
resourceProvider.registerResource("lvl1Ground", 'Images/Levels/Level1/LEVEL_1/GROUND_2_FLAT.png', [1], (1138, 38), None, None)
resourceProvider.registerResource("lvl1StaticBackground", 'Images/Levels/Level1/LEVEL_1/BACKGROUND.png', [1], (569, 320), None, None)
resourceProvider.registerResource("lvl1DinamicBackground", 'Images/Levels/Level1/LEVEL_1/spritesheet (3).png', [1, 1, 1], (1138, 320), None, None)

staticBackground = Background((0, 0), 2, resourceProvider.getResource("lvl1StaticBackground"))
dinamicBackgorund = Background((0, 0), 2, resourceProvider.getResource("lvl1DinamicBackground"))
ground = Ground((0, 0), 2, resourceProvider.getResource("lvl1Ground"))

player = Character((500, 100), 2, resourceProvider.getResource("player"), 5, 42)
playerShip = Actor((0, 0), 1.5, resourceProvider.getResource("playerShip"))
enemy1 = Enemy((0, 100), 2, resourceProvider.getResource("rubinEnemy"), 3.5, 30)
enemy2 = Enemy((1000, 100), 2, resourceProvider.getResource("rubinEnemy"), 3.5, 30)
enemy3 = Enemy((5000, 100), 2, resourceProvider.getResource("rubinEnemy"), 3.5, 30)
enemy4 = Enemy((10000, 100), 2, resourceProvider.getResource("rubinEnemy"), 3.5, 30)

rubinEnemies = []

# rubinEnemies.append(enemy1)
# rubinEnemies.append(enemy2)
# rubinEnemies.append(enemy3)
# rubinEnemies.append(enemy4)

playerShip.action = 0

lastUpdate = pygame.time.get_ticks()
scroll = 0
playerShip.bounds.bottom = ground.bounds.top
player.action = 15

objects = [playerShip]

playerOpponents = rubinEnemies
enemyOpponents = []

running = True

def main():

    global scroll

    while running:

        clock.tick(60)

        drawEnvironment(scroll)

        if not player.isShot:
            tickGame()
        else:
            gameOver()
        pygame.display.update()

    pygame.quit()


def drawEnvironment(scroll):

    staticBackground.drawActor(screen)
    dinamicBackgorund.scrolling(screen, scroll)
    ground.scrolling(screen, scroll)
    playerShip.drawActor(screen)


def gameOver():
    global running
    global lastUpdate

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    currentTime = pygame.time.get_ticks()
    if currentTime - lastUpdate > player.animationCooldown:
        if player.frame != 5:
            player.tickAnimation()
        for enemy in rubinEnemies:
            enemy.tickAnimation()
            lastUpdate = currentTime
    player.die()
    player.drawActor(screen)
    for enemy in rubinEnemies:
        enemy.drawActor(screen)


def tickGame():
    global running
    global scroll
    global lastUpdate

    updateActorsAnimation()
    handleInputEvent()
    drawCharacters()

    walkInPlace()

    # print(player.bulletsReceived)


def drawCharacters():

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
                if player.bulletsReceived < player.bulletsReceived:
                    player.bulletsReceived = player.bulletsReceived + 1

    player.gravity(ground)
    player.jump()
    player.drawActor(screen)
    player.updateBullet(objects, playerOpponents, screen)

def updateActorsAnimation():
    global lastUpdate
    currentTime = pygame.time.get_ticks()
    if currentTime - lastUpdate > player.animationCooldown:
        player.tickAnimation()
        for enemy in rubinEnemies:
            enemy.tickAnimation()
        lastUpdate = currentTime


def walkInPlace():
    offset = 8
    if player.walkInPlaceLeft:
        playerShip.scrolling(offset)
        for enemy in rubinEnemies:
            enemy.scrolling(offset)
    if player.walkInPlaceRight:
        playerShip.scrolling(-offset)
        for enemy in rubinEnemies:
            enemy.scrolling(-offset)


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

    key = pygame.key.get_pressed()
    if key[pygame.K_p]:
        player.isShot = True
    if key[pygame.K_SPACE]:
        player.toggleShooting()
    if key[pygame.K_a]:
        player.moveLeft()
        if player.toggleScrollBackgroundLeft():
            scroll -= 4
            player.walkInPlaceLeft = True
    elif key[pygame.K_d]:
        player.moveRight()
        if player.toggleScrollBackgroundRight():
            scroll += 4
            player.walkInPlaceRight = True
    else:
        player.inIdle()


if __name__ == '__main__':
    main()
