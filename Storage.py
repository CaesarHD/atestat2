from ResourceProvider import ResourceProvider


class Storage:
    def __init__(self):
        self.resourceProvider = ResourceProvider()

        self.playerBulletSize = (28, 5)
        self.rubinEnemyBulletSize = (28, 5)
        self.mineSize = (21, 6)

        self.playerBulletSpriteSheet = 'Images/Bullet/player_bullet.png'
        self.rubinBulletSpriteSheet = 'Images/Bullet/enemy_bullet.png'
        self.guardianBulletSpriteSheet = 'Images/Bullet/player_bullet.png'
        self.mineSpritesheet = 'Images/Levels/LEVEL_1/MINE_BASIC_SP1.png'

        self.resourceProvider.registerResource("playerBullet", self.playerBulletSpriteSheet, [1],
                                               self.playerBulletSize, None,
                                               None, None)
        self.resourceProvider.registerResource("rubinBullet", self.rubinBulletSpriteSheet, [1],
                                               self.rubinEnemyBulletSize, None,
                                               None, None)
        self.resourceProvider.registerResource("guardianBullet", self.guardianBulletSpriteSheet, [1],
                                               self.playerBulletSize, None,
                                               None, None)
        self.resourceProvider.registerResource('mine', self.mineSpritesheet, [1], self.mineSize, None, None, None)
        self.guardianBullet = self.resourceProvider.getResource("guardianBullet")
        self.playerBullet = self.resourceProvider.getResource("playerBullet")
        self.rubinBullet = self.resourceProvider.getResource("rubinBullet")
        self.mine = self.resourceProvider.getResource('mine')

        self.playerAnimationFrames = [4, 6, 3, 1, 2, 4, 6, 3, 1, 2, 3, 6, 2, 3, 1, 6, 7, 7]
        self.playerFrameSize = (57, 57)
        self.rubinEnemySpriteSheet = 'Images/ENEMY_FRAMES/spritesheet.png'
        self.rubinEnemyAnimationFrames = [6, 4, 3, 4, 6]
        self.rubinEnemyFrameSize = (57, 57)
        self.playerShipSpriteSheet = 'Images/Alien_Ship/spritesheet.png'
        self.playerShipAnimationFrames = [1, 1, 1, 1]
        self.playerShipFrameSize = (485, 197)
        self.lvl1GroundSize = (1138, 38)
        self.staticBackgroundSpritesheet = 'Images/Levels/LEVEL_1/BACKGROUND.png'
        self.staticBackgroundSize = (569, 320)
        self.dinamicBackgroundSpritesheet = 'Images/Levels/LEVEL_1/spritesheet (3).png'
        self.dinamicBackgroundSize = (1138, 320)
        self.dinamicBackgroundAnimationFrames = [1, 1, 1]
        self.groundSpritesheet = 'Images/Levels/LEVEL_1/GROUND_2_FLAT.png'
        self.playerSpritesheet = 'Images/ALIEN_FRAMES/spritesheet.png'
        self.guardianSpritesheet = 'Images/Levels/LEVEL_1/guardian.png'
        self.guardianAnimationFrames = [4, 3]
        self.guardianFrameSize = (57, 57)
        self.mineExplosionSpritesheet = 'Images/Levels/LEVEL_1/mine_explosion_spritesheet.png'
        self.mineExplosionSize = (100, 92)
        self.lifeBarFrames = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
        self.lifeBarSpritesheet = 'Images/Game_UI/UI/player_life_bar.png'
        self.lifeBarSize = (119, 99)
        self.abilityIconSize = (33, 34)
        self.mineIconFrames = [1, 1, 1]
        self.mineIconSpritesheet = 'Images/Game_UI/UI/mine_icon.png'
        self.gunIconSpritesheet = 'Images/Game_UI/UI/gun_icon.png'
        self.gunIconFrames = [1, 1]
        self.lvl2CableSpritesheet = 'Images/Levels/LEVEL_2/FISIERE_VITAEX_LVL2/Cablu/cable.png'
        self.lvl2CableSize = (102, 282)
        self.lvl2LaserSpritesheet = 'Images/Levels/LEVEL_2/FISIERE_VITAEX_LVL2/Laser/laser.png'
        self.lvl2LaserSize = (69, 282)
        self.lvl2PipeSpritesheet = 'Images/Levels/LEVEL_2/FISIERE_VITAEX_LVL2/Teava/pipe.png'
        self.lvl2PressUpSpriteSheet = 'Images/Levels/LEVEL_2/FISIERE_VITAEX_LVL2/Presa/press_up.png'
        self.lvl2PressDownSpriteSheet = 'Images/Levels/LEVEL_2/FISIERE_VITAEX_LVL2/Presa/press_down.png'
        self.lvl2PipeSize = (108, 282)

    def getResource(self):
        return self.resourceProvider
