import pygame

from Actor import Actor
from Background import Background
from Cable import Cable
from Character import Character
from Enemy import Enemy
from Ground import Ground
from Guardian import Guardian
from Levels import Levels
from Player import Player
from Press import Press
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
        self.scroll = self.player.scroll
        self.playerOpponents = self.rubinEnemies
        self.enemyOpponents = [self.player]
        self.running = True
        self.ui = UI()
        self.guardianPosition = self.level.guardiansPos
        self.guardians = []
        self.guardianEnemy = []
        self.guardianEnemy.append(self.player)
        self.pressXPos = self.level.pressPos
        self.presses = []
        self.objects = []
        self.objects.append(self.ground)
        self.cablePos = self.level.cablePos
        self.cables = []
        self.enemyBulletTarget = []
        self.enemyBulletTarget.append(self.player)
        self.guardianBulletTarget = []
        self.guardianBulletTarget.append(self.player)
        self.rigidBodies = []

    def generateEnemy(self):
        for pos in self.enemyPositions:
            self.rubinEnemies.append(
                Enemy((pos, 100),
                      RUBIN_ENEMY_SIZE,
                      self.resourceProvider.getResource("rubinEnemy"),
                      RUBIN_ENEMY_BULLET_SIZE,
                      RUBIN_ENEMY_BULLET_SPAWN_LOCATION,
                      (50, 0)))


    def updateActorsList(self):
        for enemy in self.rubinEnemies:
            self.actors.append(enemy)
        for guardian in self.guardians:
            self.actors.append(guardian)
        for cable in self.cables:
            self.actors.append(cable)
            self.enemyBulletTarget.append(cable)
        for press in self.presses:
            self.actors.append(press.pressUp)
            self.actors.append(press.pressDown)

    def updateObjectsList(self):
        for press in self.presses:
            self.objects.append(press.pressDown)

    def generateGuardian(self):
        for pos in self.guardianPosition:
            self.guardians.append(
                Guardian((pos, 100),
                         2,
                         self.resourceProvider.getResource("guardian"),
                         5,
                         42,
                         (50, 0)))

    def generatePress(self):
        for xPos in self.pressXPos:
            self.presses.append(Press(xPos, self.resourceProvider))

    def updateRigidBodies(self):
        for press in self.presses:
            self.rigidBodies.append(press.pressUp)

    def generateCable(self):
        for pos in self.cablePos:
            self.cables.append(Cable((pos, 0), 2,
                                     self.resourceProvider.getResource("cable"),
                                     (20, 250)))

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
            for actor in self.actors:
                actor.tickAnimation()
            for explosion in self.explosions:
                explosion.tickAnimation()
            lastUpdate = currentTime

    def drawEnvironment(self):
        self.staticBackground.drawActor(self.screen)
        self.dinamicBackgorund.scrolling(self.screen, self.player.scroll)
        self.ground.scrolling(self.screen, self.player.scroll)

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
            self.scrollActors(offset)
        if self.player.walkInPlaceRight:
            self.scrollActors(-offset)

    def drawCharacters(self):
        self.drawObjects()
        self.enemyAlgorithm()
        self.guardianAlgorithm()
        self.playerAlgorithm()

    def drawObjects(self):
        for press in self.presses:
            press.drawActor(self.screen)
            press.playerPressed(self.player)
        for cable in self.cables:
            cable.drawActor(self.screen)
            cable.working(self.player)

    def enemyAlgorithm(self):
        for enemy in self.rubinEnemies:
            if not enemy.isShot:
                enemy.gravity(self.objects)
                enemy.moving(self.player)
                enemy.drawActor(self.screen)
                enemy.updateBullet(self.enemyBulletTarget, self.enemyOpponents, self.screen)
            else:
                enemy.die()
                if not enemy.isDead:
                    enemy.drawActor(self.screen)
                else:
                    self.rubinEnemies.remove(enemy)
                    self.actors.remove(enemy)
                    del enemy
                    if self.player.bulletsReceived < 10:
                        self.player.bulletsReceived = self.player.bulletsReceived + 2

    def playerAlgorithm(self):
        self.player.collideWithRigidBody(self.rigidBodies)
        self.player.gravity(self.objects)
        self.player.jump()
        self.player.drawActor(self.screen)
        self.player.updateBullet(self.actors, self.playerOpponents, self.screen)
        self.player.placingMine()
        self.player.drawMine(self.screen)
        self.mineExplosion()
        self.drawExplosion()

    def guardianAlgorithm(self):
        for guardian in self.guardians:
            guardian.gravity(self.objects)
            guardian.isLeft = True
            guardian.isRight = False
            guardian.updateBullet(self.guardianBulletTarget, self.guardianEnemy, self.screen)
            if guardian.isCloseTo(self.player, 200):
                guardian.isShooting = True
            else:
                guardian.isShooting = False
            guardian.inIdle()

            guardian.drawActor(self.screen)

    def tickGame(self):
        self.updateActorsAnimation()
        self.player.abilityTimer()
        self.handleInputEvent()
        self.drawCharacters()
        self.scrollScene()

    def levelUp(self):
        self.lvl += 1

    def handleInputEvent(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            self.player.keyDownInputEvent(event)
        self.player.keyPessedInputEvent()
