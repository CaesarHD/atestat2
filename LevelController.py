import pygame


from Actor import Actor
from Background import Background
from Character import Character
from Enemy import Enemy
from Ground import Ground
from Levels import Levels
from Player import Player
from UI import UI

RUBIN_ENEMY_BULLET_SIZE = 3.5
RUBIN_ENEMY_BULLET_SPAWN_LOCATION = 30
RUBIN_ENEMY_SIZE = 2
lastUpdate = pygame.time.get_ticks()
SCROLLING_SPEED = 4


class LevelController:
    def __init__(self, screen, actors):
        self.screen = screen
        self.level = Levels()
        self.lvl = 2
        self.resourceProvider = self.level.loadResourcesLevel(self.lvl)
        self.player = Player((0, 100), 2, self.resourceProvider.getResource("player"), 5, 42, (50, 0))
        self.rubinEnemies = []
        self.enemyPositions = self.level.rubinEnemyPos
        self.staticBackground = Background((0, 0), 2, self.resourceProvider.getResource("staticBackground"))
        self.dinamicBackgorund = Background((0, 0), 2, self.resourceProvider.getResource("dinamicBackground"))
        self.ground = Ground((0, 0), 2, self.resourceProvider.getResource("ground"))
        self.mines = self.player.mines
        self.explosions = []
        self.explosionPos = 0
        self.actors = actors
        self.scroll = 0
        self.playerOpponents = self.rubinEnemies
        self.enemyOpponents = []
        self.running = True
        self.ui = UI()


    def generateEnemy(self):
        for pos in self.enemyPositions:
            self.rubinEnemies.append(
                Enemy((pos, 100),
                      RUBIN_ENEMY_SIZE,
                      self.resourceProvider.getResource("rubinEnemy"),
                      RUBIN_ENEMY_BULLET_SIZE,
                      RUBIN_ENEMY_BULLET_SPAWN_LOCATION,
                      (50, 0)))

    def generateExplosion(self, pos):
        self.explosions.append(Actor(pos, 2, self.resourceProvider.getResource('mineExplosion'), None))

    def mineExplosion(self):
        for mine in self.mines:
            self.mineToggleExplosion(mine)
            if mine.isTriggered:
                self.explosionPos = mine.getExplosionCoord()
                self.generateExplosion(self.explosionPos)
                self.mines.remove(mine)
                del mine

    def drawExplosion(self):
        for explosion in self.explosions:
            explosion.drawActor(self.screen)
            if explosion.frame == 5:
                self.explosions.remove(explosion)
                del explosion

    def mineToggleExplosion(self, mine):
        mine.active(self.player)
        mine.trigger(self.player, self.rubinEnemies)

    def updateActorsAnimation(self):
        global lastUpdate
        currentTime = pygame.time.get_ticks()
        if currentTime - lastUpdate > self.player.animationCooldown:
            self.player.tickAnimation()
            for enemy in self.rubinEnemies:
                enemy.tickAnimation()
            for explosion in self.explosions:
                explosion.tickAnimation()
            lastUpdate = currentTime

    def drawEnvironment(self):
        self.staticBackground.drawActor(self.screen)
        self.dinamicBackgorund.scrolling(self.screen, self.scroll)
        self.ground.scrolling(self.screen, self.scroll)

    def scrollActors(self, offset):
        for actor in self.actors:
            actor.scrolling(offset)

        for mine in self.mines:
            mine.scrolling(offset)

        for explosion in self.explosions:
            explosion.scrolling(offset)

    def scrollScene(self):
        offset = 2 * SCROLLING_SPEED
        if self.player.walkInPlaceLeft:
            for enemy in self.rubinEnemies:
                enemy.scrolling(offset)
            self.scrollActors(offset)
        if self.player.walkInPlaceRight:
            for enemy in self.rubinEnemies:
                enemy.scrolling(-offset)
            self.scrollActors(-offset)

    def drawCharacters(self):
        for enemy in self.rubinEnemies:
            if not enemy.isShot:
                enemy.gravity(self.ground)
                enemy.moving(self.player)
                enemy.drawActor(self.screen)
                enemy.updateBullet(self.actors, self.enemyOpponents, self.screen)
            else:
                enemy.die()
                if not enemy.isDead:
                    enemy.drawActor(self.screen)
                else:
                    self.rubinEnemies.remove(enemy)
                    del enemy
                    if self.player.bulletsReceived < 10:
                        self.player.bulletsReceived = self.player.bulletsReceived + 2

        self.player.gravity(self.ground)
        self.player.jump()
        self.player.drawActor(self.screen)
        self.player.updateBullet(self.actors, self.playerOpponents, self.screen)
        self.player.placingMine()
        self.player.drawMine(self.screen)
        self.mineExplosion()
        self.drawExplosion()

    def tickGame(self):
        self.updateActorsAnimation()
        self.player.abilityTimer()
        self.player.handleInputEvent(self.running)
        self.drawCharacters()
        self.scrollScene()

    def levelUp(self):
        self.lvl += 1

