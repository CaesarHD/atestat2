from Actions import Actions
from ResourceProvider import ResourceProvider
from Storage import Storage


class Levels:
    def __init__(self):
        self.levels = []
        self.resourcesLvl1 = {}
        self.numberOfFrames = []
        self.action = Actions()
        self.storage = Storage()
        self.resourceProvider = self.storage.getResource()

        self.staticBackground = None
        self.dinamicBackground = None
        self.rubinEnemyPos = []
        self.player = None
        self.playerShip = None
        self.guardiansPos = []
        self.gatePos = []
        self.pressPos = []
        self.pressOffset = []
        self.laserPos = []
        self.pipePos = []
        self.cablePos = []
        self.antennaPos = []
        self.controlPanelPos = []

    def loadResourcesLevel0(self):
        self.resourceProvider.registerResource("staticBackground", self.storage.lvl0BackgroundSpritesheet, [1],
                                               self.storage.lvl0BackgroundSize, None, None, None)
        self.resourceProvider.registerResource("vitaexLogo", self.storage.vitaexLogoSpritesheet, [1],
                                               self.storage.vitaexLogoSize, None, None, None)
        self.resourceProvider.registerResource("pressKey", self.storage.pressKeyTextSpriteSheet, [1],
                                               self.storage.pressKeyTextSize, None, None, None)
        self.resourceProvider.registerResource("voyager", self.storage.voyagerSpritesheet, [1],
                                               self.storage.voyagerSize, None, None, None)
        self.resourceProvider.registerResource("asteroid", self.storage.asteroidSpritesheet, [1],
                                               self.storage.asteroidSize, None, None, None)

    def loadResourcesLevel1(self):
        self.resourceProvider.registerResource("antenna", self.storage.lvl1AntennaSpritesheet, [1],
                                               self.storage.lvl1AntennaSize, None, None, None)
        self.resourceProvider.registerResource("controlPanel", self.storage.lvl1ControlsPanelSpritesheet, self.storage.lvl1ControlsPanelFrame,
                                               self.storage.lvl1ControlsPanelSize, None, None, None)
        self.resourceProvider.registerResource("rubinEnemy", self.storage.rubinEnemySpriteSheet,
                                               self.storage.rubinEnemyAnimationFrames, self.storage.rubinEnemyFrameSize,
                                               self.action.getActions("rubinEnemy"),
                                               self.storage.rubinBullet, None)
        self.resourceProvider.registerResource("player", self.storage.playerSpritesheet,
                                               self.storage.playerAnimationFrames, self.storage.playerFrameSize,
                                               self.action.getActions("player"), self.storage.playerBullet,
                                               self.storage.mine
                                               )
        self.resourceProvider.registerResource("playerShip", self.storage.playerShipSpriteSheet,
                                               self.storage.playerShipAnimationFrames,
                                               self.storage.playerShipFrameSize, self.action.getActions("playerShip"),
                                               None, None)
        self.resourceProvider.registerResource("ground", self.storage.lvl1GroundSpritesheet, [1],
                                               self.storage.lvl1GroundSize, None, None, None)
        self.resourceProvider.registerResource("staticBackground", self.storage.lvl1StaticBackgroundSpritesheet, [1],
                                               self.storage.lvl1StaticBackgroundSize, None, None, None)
        self.resourceProvider.registerResource("dinamicBackground", self.storage.lvl1DinamicBackgroundSpritesheet,
                                               self.storage.lvl1DinamicBackgroundAnimationFrames,
                                               self.storage.lvl1DinamicBackgroundSize, None, None, None)
        self.resourceProvider.registerResource("guardian", self.storage.guardianSpritesheet,
                                               self.storage.guardianAnimationFrames, self.storage.guardianFrameSize,
                                               self.action.getActions("guardian"), self.storage.guardianBullet, None)
        self.resourceProvider.registerResource("mine", self.storage.mineSpritesheet, [1], self.storage.mineSize, None,
                                               None, None)
        self.resourceProvider.registerResource('mineExplosion', self.storage.mineExplosionSpritesheet, [9],
                                               self.storage.mineExplosionSize,
                                               None, None, None)
        self.resourceProvider.registerResource("lifeBar", self.storage.lifeBarSpritesheet,
                                               self.storage.lifeBarFrames, self.storage.lifeBarSize,
                                               None, None, None)
        self.resourceProvider.registerResource("mineIcon", self.storage.mineIconSpritesheet,
                                               self.storage.mineIconFrames, self.storage.abilityIconSize,
                                               self.action.getActions("playerAbility"), None, None)
        self.resourceProvider.registerResource("gunIcon", self.storage.gunIconSpritesheet,
                                               self.storage.gunIconFrames, self.storage.abilityIconSize,
                                               self.action.getActions("playerGunStates"), None, None)
        self.resourceProvider.registerResource("pauseTextMenu", self.storage.menuTextSpritesheet,
                                               self.storage.menuTextAnimationFrames,
                                               self.storage.menuTextSize, None, None, None)
        self.rubinEnemyPos = [3000, 4000, 4500, 5500, 6000, 6100, 7000, 7200, 7500, 9000, 9500, 10000, 10100,
                              12000, 13000, 13100, 14500, 14900, 17000, 17100, 17200, 17800, 20000, 20100, 20500, 21000,
                              21050, 21100, 21500, 22000]
        self.gatePos = []
        self.pressPos = []
        self.guardiansPos = []
        self.antennaPos = [10]

    def loadResourcesLevel2(self):
        self.resourceProvider.registerResource("antenna", self.storage.lvl1AntennaSpritesheet, [1],
                                               self.storage.lvl1AntennaSize, None, None, None)
        self.resourceProvider.registerResource("rubinEnemy", self.storage.rubinEnemySpriteSheet,
                                               self.storage.rubinEnemyAnimationFrames, self.storage.rubinEnemyFrameSize,
                                               self.action.getActions("rubinEnemy"),
                                               self.storage.rubinBullet, None)
        self.resourceProvider.registerResource("player", self.storage.playerSpritesheet,
                                               self.storage.playerAnimationFrames, self.storage.playerFrameSize,
                                               self.action.getActions("player"), self.storage.playerBullet,
                                               self.storage.mine
                                               )
        self.resourceProvider.registerResource("playerShip", self.storage.playerShipSpriteSheet,
                                               self.storage.playerShipAnimationFrames,
                                               self.storage.playerShipFrameSize, self.action.getActions("playerShip"),
                                               None, None)
        self.resourceProvider.registerResource("ground", self.storage.lvl2GroundSpritesheet, [1],
                                               self.storage.lvl2GroundSize, None, None, None)
        self.resourceProvider.registerResource("staticBackground", self.storage.lvl2StaticBackgroundSpritesheet, [1],
                                               self.storage.lvl2StaticBackgroundSize, None, None, None)
        self.resourceProvider.registerResource("dinamicBackground", self.storage.lvl2DinamicBackgroundSpritesheet,
                                               self.storage.lvl2DinamicBackgroundAnimationFrames,
                                               self.storage.lvl2DinamicBackgroundSize, None, None, None)
        self.resourceProvider.registerResource("guardian", self.storage.guardianSpritesheet,
                                               self.storage.guardianAnimationFrames, self.storage.guardianFrameSize,
                                               self.action.getActions("guardian"), self.storage.guardianBullet, None)
        self.resourceProvider.registerResource("mine", self.storage.mineSpritesheet, [1], self.storage.mineSize, None,
                                               None, None)
        self.resourceProvider.registerResource('mineExplosion', self.storage.mineExplosionSpritesheet, [9],
                                               self.storage.mineExplosionSize,
                                               None, None, None)
        self.resourceProvider.registerResource("lifeBar", self.storage.lifeBarSpritesheet,
                                               self.storage.lifeBarFrames, self.storage.lifeBarSize,
                                               None, None, None)
        self.resourceProvider.registerResource("mineIcon", self.storage.mineIconSpritesheet,
                                               self.storage.mineIconFrames, self.storage.abilityIconSize,
                                               self.action.getActions("playerAbility"), None, None)
        self.resourceProvider.registerResource("gunIcon", self.storage.gunIconSpritesheet,
                                               self.storage.gunIconFrames, self.storage.abilityIconSize,
                                               self.action.getActions("playerGunStates"), None, None)
        self.resourceProvider.registerResource("pressUp", self.storage.lvl2PressUpSpriteSheet, [1],
                                               self.storage.lvl2PressUpSize,
                                               None, None, None)
        self.resourceProvider.registerResource("pressDown", self.storage.lvl2PressDownSpriteSheet, [1],
                                               self.storage.lvl2PressDownSize,
                                               None, None, None)
        self.resourceProvider.registerResource("pipe", self.storage.lvl2PipeSpritesheet, [1, 5],
                                               self.storage.lvl2PipeSize,
                                               None, None, None)
        self.resourceProvider.registerResource("laserTop", self.storage.lvl2LaserTopSpritesheet,
                                               self.storage.lvl2LaserAnimationFrames,
                                               self.storage.lvl2LaserTopSize,
                                               None, None, None)
        self.resourceProvider.registerResource("laserSlab", self.storage.lvl2LaserSlabSpritesheet,
                                               self.storage.lvl2LaserAnimationFrames,
                                               self.storage.lvl2LaserSlabSize,
                                               None, None, None)
        self.resourceProvider.registerResource("cable", self.storage.lvl2CableSpritesheet, [6],
                                               self.storage.lvl2CableSize, None, None, None)
        self.resourceProvider.registerResource("pauseTextMenu", self.storage.menuTextSpritesheet,
                                               self.storage.menuTextAnimationFrames,
                                               self.storage.menuTextSize, None, None, None)
        self.resourceProvider.registerResource("staticGate", self.storage.staticGateSpritesheet, [1],
                                               self.storage.gateSize, None, None, None)
        self.resourceProvider.registerResource("dinamicGate", self.storage.dinamicGateSpritesheet, [1],
                                               self.storage.gateSize, None, None, None)
        self.resourceProvider.registerResource("gateWall", self.storage.gateWallSpritesheet, [1],
                                               self.storage.gateSize, None, None, None)
        self.cablePos = [4200, 5900, 6200]
        self.pressPos = [3000, 3150, 3300, 7000, 7150, 7300, 9500, 9650, 9800, 9950]
        self.pressOffset = [0, 250, 50, 0, 300, 150, 0, 250, 50, 300]
        self.pipePos = [2400, 3700, 6500]
        self.laserPos = [5000, 8000]
        self.gatePos = [1500]
        self.guardiansPos = [1650]

    def loadResourcesLevel3(self):
        self.resourceProvider.registerResource("antenna", self.storage.lvl1AntennaSpritesheet, [1],
                                               self.storage.lvl1AntennaSize, None, None, None)

        self.resourceProvider.registerResource("rubinEnemy", self.storage.rubinEnemySpriteSheet,
                                               self.storage.rubinEnemyAnimationFrames, self.storage.rubinEnemyFrameSize,
                                               self.action.getActions("rubinEnemy"),
                                               self.storage.rubinBullet, None)
        self.resourceProvider.registerResource("player", self.storage.playerSpritesheet,
                                               self.storage.playerAnimationFrames, self.storage.playerFrameSize,
                                               self.action.getActions("player"), self.storage.playerBullet,
                                               self.storage.mine
                                               )
        self.resourceProvider.registerResource("playerShip", self.storage.playerShipSpriteSheet,
                                               self.storage.playerShipAnimationFrames,
                                               self.storage.playerShipFrameSize, self.action.getActions("playerShip"),
                                               None, None)
        self.resourceProvider.registerResource("ground", self.storage.lvl2GroundSpritesheet, [1],
                                               self.storage.lvl2GroundSize, None, None, None)
        self.resourceProvider.registerResource("staticBackground", self.storage.lvl2StaticBackgroundSpritesheet, [1],
                                               self.storage.lvl2StaticBackgroundSize, None, None, None)
        self.resourceProvider.registerResource("dinamicBackground", self.storage.lvl2DinamicBackgroundSpritesheet,
                                               self.storage.lvl2DinamicBackgroundAnimationFrames,
                                               self.storage.lvl2DinamicBackgroundSize, None, None, None)
        self.resourceProvider.registerResource("guardian", self.storage.guardianSpritesheet,
                                               self.storage.guardianAnimationFrames, self.storage.guardianFrameSize,
                                               self.action.getActions("guardian"), self.storage.guardianBullet, None)
        self.resourceProvider.registerResource("mine", self.storage.mineSpritesheet, [1], self.storage.mineSize, None,
                                               None, None)
        self.resourceProvider.registerResource('mineExplosion', self.storage.mineExplosionSpritesheet, [9],
                                               self.storage.mineExplosionSize,
                                               None, None, None)
        self.resourceProvider.registerResource("lifeBar", self.storage.lifeBarSpritesheet,
                                               self.storage.lifeBarFrames, self.storage.lifeBarSize,
                                               None, None, None)
        self.resourceProvider.registerResource("mineIcon", self.storage.mineIconSpritesheet,
                                               self.storage.mineIconFrames, self.storage.abilityIconSize,
                                               self.action.getActions("playerAbility"), None, None)
        self.resourceProvider.registerResource("gunIcon", self.storage.gunIconSpritesheet,
                                               self.storage.gunIconFrames, self.storage.abilityIconSize,
                                               self.action.getActions("playerGunStates"), None, None)
        self.resourceProvider.registerResource("pressUp", self.storage.lvl2PressUpSpriteSheet, [1],
                                               self.storage.lvl2PressUpSize,
                                               None, None, None)
        self.resourceProvider.registerResource("pressDown", self.storage.lvl2PressDownSpriteSheet, [1],
                                               self.storage.lvl2PressDownSize,
                                               None, None, None)
        self.resourceProvider.registerResource("pipe", self.storage.lvl2PipeSpritesheet, [1, 5],
                                               self.storage.lvl2PipeSize,
                                               None, None, None)
        self.resourceProvider.registerResource("laserTop", self.storage.lvl2LaserTopSpritesheet,
                                               self.storage.lvl2LaserAnimationFrames,
                                               self.storage.lvl2LaserTopSize,
                                               None, None, None)
        self.resourceProvider.registerResource("laserSlab", self.storage.lvl2LaserSlabSpritesheet,
                                               self.storage.lvl2LaserAnimationFrames,
                                               self.storage.lvl2LaserSlabSize,
                                               None, None, None)
        self.resourceProvider.registerResource("cable", self.storage.lvl2CableSpritesheet, [6],
                                               self.storage.lvl2CableSize, None, None, None)
        self.resourceProvider.registerResource("pauseTextMenu", self.storage.menuTextSpritesheet,
                                               self.storage.menuTextAnimationFrames,
                                               self.storage.menuTextSize, None, None, None)
        self.resourceProvider.registerResource("staticGate", self.storage.staticGateSpritesheet, [1],
                                               self.storage.gateSize, None, None, None)
        self.resourceProvider.registerResource("dinamicGate", self.storage.dinamicGateSpritesheet, [1],
                                               self.storage.gateSize, None, None, None)
        self.resourceProvider.registerResource("gateWall", self.storage.gateWallSpritesheet, [1],
                                               self.storage.gateSize, None, None, None)
        self.resourceProvider.registerResource("toBeContinuedText", self.storage.toBeContinuedSpritesheet, [1],
                                               self.storage.toBeContinuedSize, None, None, None)

    def loadResourcesLevel(self, level):
        match level:
            case 0:
                self.loadResourcesLevel0()
            case 1:
                self.loadResourcesLevel1()
            case 2:
                self.loadResourcesLevel2()
            case 3:
                self.loadResourcesLevel3()
        return self.resourceProvider
