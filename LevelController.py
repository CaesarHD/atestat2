import pygame

from Actor import Actor
from Background import Background
from Cable import Cable
from Enemy import Enemy
from Gate import Gate
from Ground import Ground
from Guardian import Guardian
from Laser import Laser
from LevelZero import LevelZero
from Levels import Levels
from Pipe import Pipe
from Player import Player
from Press import Press
from UI import UI


RUBIN_ENEMY_BULLET_SIZE = 3.5
RUBIN_ENEMY_BULLET_SPAWN_LOCATION = 30
RUBIN_ENEMY_SIZE = 2
lastUpdate = pygame.time.get_ticks()
SCROLLING_SPEED = 4
SCREEN_WIDTH = 800 * 1.42


def checkForKeyPress():
    keys = pygame.key.get_pressed()
    if not any(keys):
        return False
    else:
        return True


class LevelController:
    def __init__(self, screen, lvl):
        self.screen = screen
        self.level = Levels()
        self.lvl = lvl
        self.resourceProvider = self.level.loadResourcesLevel(self.lvl)
        self.player = Player((0, 100), 2, self.resourceProvider.getResource("player"), 5, 42, (35, 0))
        self.rubinEnemies = []
        self.enemyPositions = self.level.rubinEnemyPos
        self.staticBackground = Background((0, 0), 2, self.resourceProvider.getResource("staticBackground"))
        self.dinamicBackgorund = Background((0, 0), 2, self.resourceProvider.getResource("dinamicBackground"))
        self.ground = Ground((-10, 0), 2, self.resourceProvider.getResource("ground"))
        self.mines = self.player.mines
        self.explosions = []
        self.explosionPos = 0
        self.actors = []
        self.scroll = self.player.scroll
        self.playerOpponents = self.rubinEnemies
        self.enemyOpponents = [self.player]
        self.running = True
        self.ui = UI()
        self.guardianPosition = self.level.guardiansPos
        self.guardians = []
        self.guardianEnemy = [self.player]
        self.pressXPos = self.level.pressPos
        self.pressYOffset = self.level.pressOffset
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
        self.isInMenu = False
        self.isLevelZero = False
        self.lvlZero = LevelZero()
        self.menuText = Actor((20, 570), 2, self.resourceProvider.getResource("pauseTextMenu"), None)
        self.pipePos = self.level.pipePos
        self.pipes = []
        self.lasers = []
        self.laserPos = self.level.laserPos
        self.gates = []
        self.gatePos = self.level.gatePos
        self.restartLevel = False
        self.isOver = False
        self.restart = None
        self.ashes = False

    def levelZero(self):
        resourceProvider = self.level.loadResourcesLevel(0)
        staticBackground = Background((0, 0), 2, resourceProvider.getResource("staticBackground"))
        vitaexLogo = Actor((0, 0), 2, resourceProvider.getResource("vitaexLogo"), None)
        pressKey = Actor((0, 0), 2, resourceProvider.getResource("pressKey"), None)
        voyager = Actor((0, 0), 2, resourceProvider.getResource("voyager"), None)

        staticBackground.drawActor(self.screen)
        vitaexLogo.drawActor(self.screen)
        pressKey.drawActor(self.screen)
        voyager.drawActor(self.screen)

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
        for pipe in self.pipes:
            self.actors.append(pipe)
        for laser in self.lasers:
            self.actors.append(laser.laserTop)
            self.actors.append(laser.laserSlab)
        for gate in self.gates:
            self.actors.append(gate.dinamicGate)
            self.actors.append(gate.staticGate)
            self.actors.append(gate.gateWall)
        for press in self.presses:
            self.actors.append(press.pressUp)
            self.actors.append(press.pressDown)

    def updateObjectsList(self):
        for press in self.presses:
            self.objects.append(press.pressDown)
        for laser in self.lasers:
            self.objects.append(laser.laserSlab)

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
        index = 0
        for xPos in self.pressXPos:
            self.presses.append(Press(xPos, self.pressYOffset[index], self.resourceProvider))
            index += 1

    def generateGate(self):
        for pos in self.gatePos:
            self.gates.append(Gate(pos, self.resourceProvider))

    def generateLaser(self):
        for posX in self.laserPos:
            self.lasers.append(Laser(posX, self.resourceProvider))

    def updateRigidBodies(self):
        for press in self.presses:
            self.rigidBodies.append(press.pressUp)
        for gate in self.gates:
            self.rigidBodies.append(gate.dinamicGate)

    def generateCable(self):
        for pos in self.cablePos:
            self.cables.append(Cable((pos, 0), 2,
                                     self.resourceProvider.getResource("cable"),
                                     (20, 250)))

    def generatePipe(self):
        for pos in self.pipePos:
            self.pipes.append(Pipe((pos, 0), 2,
                                   self.resourceProvider.getResource("pipe"), (20, 250)))

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
        if self.player.walkInPlaceLeft and not self.player.isBlocked:
            self.scrollActors(offset)
        if self.player.walkInPlaceRight and not self.player.isBlocked:
            self.scrollActors(-offset)

    def characterAI(self):
        self.enemyAlgorithm()
        self.guardianAlgorithm()
        self.playerAlgorithm()

    def drawCharacters(self):
        for enemy in self.rubinEnemies:
            enemy.drawActor(self.screen)
            enemy.drawBullets(self.screen)
        for guardian in self.guardians:
            guardian.drawActor(self.screen)
            guardian.drawBullets(self.screen)
        self.player.drawActor(self.screen)
        self.player.drawBullets(self.screen)

    def drawObjects(self):
        for press in self.presses:
            press.drawActor(self.screen)
            press.playerPressed(self.player)
        for cable in self.cables:
            cable.drawActor(self.screen)
            cable.working(self.player)
        for pipe in self.pipes:
            pipe.drawActor(self.screen)
            pipe.collideWith(self.player)
        for laser in self.lasers:
            laser.drawActor(self.screen)
            laser.working()
        for gate in self.gates:
            gate.drawGate(self.screen)
        self.player.drawMine(self.screen)

    def movingPresses(self):
        for press in self.presses:
            press.moving()

    def steamGasePipe(self):
        for pipe in self.pipes:
            pipe.working()

    def laserBurn(self):
        for laser in self.lasers:
            laser.playerBurned(self.player)

    def gateWorking(self):
        for gate in self.gates:
            gate.working(self.player)

    def enemyAlgorithm(self):
        for enemy in self.rubinEnemies:
            if not enemy.isShot:
                enemy.gravity(self.objects)
                enemy.moving(self.player)
                enemy.updateBullet(self.enemyBulletTarget, self.enemyOpponents, self.screen)
            else:
                enemy.die()
                if not enemy.isDead:
                    continue
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
        self.player.updateBullet(self.actors, self.playerOpponents, self.screen)
        self.player.placingMine()
        self.mineExplosion()
        self.drawExplosion()

    def guardianAlgorithm(self):
        for guardian in self.guardians:
            guardian.working(self.gates[0], self.objects, self.player)
            guardian.updateBullet(self.guardianBulletTarget, self.guardianEnemy, self.screen)

    def tickGame(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            if not self.isInMenu and not self.isLevelZero:
                self.player.keyDownInputEvent(event)

            if self.isLevelZero:
                if event.type == pygame.KEYDOWN:
                    if checkForKeyPress():
                        self.isLevelZero = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.isInMenu = not self.isInMenu

        if self.isInMenu:
            self.menu()
            return

        if self.isLevelZero:
            self.lvlZero.drawLevel(self.screen)
            return

        self.updateActorsAnimation()
        self.player.abilityTimer()
        self.player.keyPessedInputEvent()
        self.characterAI()
        self.drawObjects()
        self.drawCharacters()
        self.movingPresses()
        self.gateWorking()
        self.steamGasePipe()
        self.laserBurn()
        self.scrollScene()
        self.ui.renderUI(self.player, self.screen)

    def nextLevel(self):
        if self.player.bounds.x >= (SCREEN_WIDTH - self.player.bounds.size[1]) - 2:
            self.restartLevel = False
            return True
        if self.restartLevel:
            self.restartLevel = False
            self.lvl -= 1
            return True

        return False

    def levelUp(self):
        self.lvl += 1
        return self.lvl

    def menu(self):
        global lastUpdate
        self.drawObjects()
        self.drawCharacters()
        self.ui.drawUI(self.screen)
        img = pygame.Surface((800 * 1.42, 480 * 1.33))
        img.set_alpha(150)
        img.fill((0, 0, 0))
        self.screen.blit(img, (0, 0))
        self.menuText.drawActor(self.screen)

        currentTime = pygame.time.get_ticks()
        if currentTime - lastUpdate > self.player.animationCooldown:
            self.menuText.tickAnimation()
            lastUpdate = currentTime

    def gameOver(self):
        global lastUpdate
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            if self.restart:
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_r:
                        self.restartLevel = True

        # currentTime = pygame.time.get_ticks()
        # if currentTime - lastUpdate > self.player.animationCooldown:
        #     self.updateActorsAnimation()
        #     self.ui.renderUI(self.player, self.screen)
        #     lastUpdate = currentTime
        self.player.die()
        self.player.drawActor(self.screen)
        self.characterAI()
        self.steamGasePipe()
        self.drawObjects()
        self.drawCharacters()
        self.movingPresses()
        self.updateActorsAnimation()
        self.player.updateBullet(self.actors, self.playerOpponents, self.screen)
        for guardian in self.guardians:
            guardian.updateBullet(self.actors, self.guardianEnemy, self.screen)
        for enemy in self.rubinEnemies:
            enemy.updateBullet(self.actors, self.enemyOpponents, self.screen)

        if self.player.frame == self.player.deathLastFrame and not self.ashes:
            self.ashes = True
        if self.ashes:
            self.player.frame = self.player.deathLastFrame
            self.restart = True
        self.ui.renderUI(self.player, self.screen)
