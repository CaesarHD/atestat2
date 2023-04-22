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
        self.laserPos = []
        self.pipePose = []
        self.cablePos = []

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
        self.rubinEnemyPos = [3000, 4000, 4500, 5500, 6000, 6100, 7000, 7200, 7500, 9000, 9500, 10000, 10100,
                              12000, 13000, 13100, 14500, 14900, 17000, 17100, 17200, 17800, 20000, 20100, 20500, 21000,
                              21050, 21100, 21500, 22000]
        self.gatePos = []
        self.pressPos = []
        self.guardiansPos = []

    def loadResourcesLevel2(self):
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
        self.resourceProvider.registerResource("pipe", self.storage.lvl2PipeSpritesheet, [1],
                                               self.storage.lvl2PipeSize,
                                               None, None, None)
        self.resourceProvider.registerResource("laser", self.storage.lvl2LaserSpritesheet,
                                               self.storage.lvl2LaserAnimationFrames,
                                               self.storage.lvl2LaserSize,
                                               None, None, None)
        self.resourceProvider.registerResource("cable", self.storage.lvl2CableSpritesheet, [6],
                                               self.storage.lvl2CableSize, None, None, None)
        self.gatePos = []
        self.cablePos = [700]
        self.pressPos = [1500]
        self.laserPos = []
        self.pipePose = []
        self.rubinEnemyPos = []
        self.guardiansPos = [1000]

    def loadResourcesLevel(self, level):
        match level:
            case 0:
                self.loadResourcesLevel0()
            case 1:
                self.loadResourcesLevel1()
            case 2:
                self.loadResourcesLevel2()
        return self.resourceProvider
