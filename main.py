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
def main():
    pygame.init()

    clock = pygame.time.Clock()

    screen = Screen(800*1.42, 480*1.33)

    # level = Levels()

    resourceProvider = ResourceProvider()
    action = Actions()
    resourceProvider.registerResource("playerBullet", 'Images\Bullet\player_bullet.png', [1], (28, 5), None, None)
    playerBullet = Bullet((0, 0), 5, resourceProvider.getResource("playerBullet"))
    resourceProvider.registerResource("rubinEnemy", 'Images/ENEMY_FRAMES/spritesheet.png', [6, 4, 3, 4], (57, 57), action.getActions("rubinEnemy"), None)
    resourceProvider.registerResource("player", 'Images/ALIEN_FRAMES/spritesheet.png', [4, 6, 3, 1, 2, 4, 6, 3, 1, 2, 3, 6, 2, 3], (57, 57), action.getActions("player"), playerBullet)
    resourceProvider.registerResource("playerShip", 'Images/Alien_Ship/spritesheet.png', [1, 1, 1, 1], (485, 197), action.getActions("playerShip"), None)
    resourceProvider.registerResource("lvl1BG", 'Images/Backgrounds/LVL1/dinamicSpritesheet.png', [1, 1, 1], (1138, 320), None, None)
    resourceProvider.registerResource("lvl1BG_Spate", 'Images/Backgrounds/LVL1/staticSpritesheet.png', [4], (569, 320), None, None)
    resourceProvider.registerResource("lvl1Ground", 'Images/Backgrounds/LVL1/ground.png', [1], (1138, 38), None, None)

    player = Character((500, 100), 2, resourceProvider.getResource("player"))

    background = Background((0, 0), 2, resourceProvider.getResource("lvl1BG"))
    backgroundSpate = Background((0, 0), 2, resourceProvider.getResource("lvl1BG_Spate"))
    ground = Ground((0, 0), 2, resourceProvider.getResource("lvl1Ground"))

    playerShip = Actor((0, 0), 1.5, resourceProvider.getResource("playerShip"))
    enemy = Enemy((200, 100), 2, resourceProvider.getResource("rubinEnemy"))

    playerShip.action = 0

    lastUpdate = pygame.time.get_ticks()
    player.animationCooldown = 90

    color = (220, 225, 220)

    running = True

    scroll = 0

    playerShip.bounds.bottom = ground.bounds.top

    while running:

        screen.fill(color)

        clock.tick(60)
        backgroundSpate.drawActor(screen)
        background.scrolling(screen, scroll)
        ground.scrolling(screen, scroll)
        playerShip.drawActor(screen)

        if player.walkInPlaceLeft:
            playerShip.scrolling(8)
            enemy.scrolling(8)
        if player.walkInPlaceRight:
            playerShip.scrolling(-8)
            enemy.scrolling(-8)


        currentTime = pygame.time.get_ticks()
        if currentTime - lastUpdate > player.animationCooldown:
            player.tickAnimation()
            enemy.tickAnimation()
            backgroundSpate.tickAnimation()
            lastUpdate = currentTime

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                match event.key:
                    case pygame.K_q: player.toggleWeapon()
                    case pygame.K_w: player.toggleJump()

        player.gravity(ground)
        enemy.gravity(ground)
        enemy.moving(player)

        key = pygame.key.get_pressed()

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

        player.jump()

        enemy.drawActor(screen)

        player.drawActor(screen)

        if player.bullet.release:
            player.bullet.drawActor(screen)
            # pygame.draw.rect(screen.screen, (255,0,0), player.bullet.bounds)
        # pygame.draw.rect(screen.screen, (255, 0, 0), playerShip.bounds)
        # pygame.draw.rect(screen.screen, (255, 0, 0), player.bounds)
        # pygame.draw.rect(screen.screen, (255, 0, 0), ground.bounds)

        pygame.display.update()

    pygame.quit()

if __name__ == '__main__':
    main()
