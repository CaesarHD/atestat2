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

    def loadResourcesLevel1(self):
        self.resourceProvider.registerResource("rubinEnemy", self.storage.rubinEnemySpriteSheet,
                                               self.storage.rubinEnemyAnimationFrames, self.storage.rubinEnemyFrameSize,
                                               self.action.getActions("rubinEnemy"),
                                               self.storage.rubinBullet, None)
        self.resourceProvider.registerResource("player", self.storage.playerSpritesheet,
                                               self.storage.playerAnimationFrames, self.storage.playerFrameSize,
                                               self.action.getActions("player"), self.storage.playerBullet, self.storage.mine)
        self.resourceProvider.registerResource("playerShip", self.storage.playerShipSpriteSheet,
                                               self.storage.playerShipAnimationFrames,
                                               self.storage.playerShipFrameSize, self.action.getActions("playerShip"),
                                               None, None)
        self.resourceProvider.registerResource("lvl1Ground", self.storage.groundSpritesheet, [1],
                                               self.storage.lvl1GroundSize, None, None, None)
        self.resourceProvider.registerResource("lvl1StaticBackground", self.storage.staticBackgroundSpritesheet, [1],
                                               self.storage.staticBackgroundSize, None, None, None)
        self.resourceProvider.registerResource("lvl1DinamicBackground", self.storage.dinamicBackgroundSpritesheet,
                                               self.storage.dinamicBackgroundAnimationFrames,
                                               self.storage.dinamicBackgroundSize, None, None, None)
        self.resourceProvider.registerResource("guardian", self.storage.guardianSpritesheet,
                                               self.storage.guardianAnimationFrames, self.storage.guardianFrameSize,
                                               self.action.getActions("guardian"), self.storage.guardianBullet, None)
        self.resourceProvider.registerResource("mine", self.storage.mineSpritesheet, [1], self.storage.mineSize, None, None, None)
        self.resourceProvider.registerResource('mineExplosion', self.storage.mineExplosionSpritesheet, [9], self.storage.mineExplosionSize,
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

    def loadResourcesLevel(self, level):
        match level:
            case 1:
                self.loadResourcesLevel1()
        return self.resourceProvider
