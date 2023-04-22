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
        self.lvl0BackgroundSpritesheet = 'Images/Levels/LEVEL_0/BackgroundMain.png'
        self.lvl0BackgroundSize = (569, 320)
        self.pressKeyTextSpriteSheet = 'Images/Levels/LEVEL_0/PressKey.png'
        self.pressKeyTextSize = (569, 320)
        self.vitaexLogoSpritesheet = 'Images/Levels/LEVEL_0/VITAEX.png'
        self.vitaexLogoSize = (569, 320)
        self.voyagerSpritesheet = 'Images/Levels/LEVEL_0/Voyager_Sonda.png'
        self.voyagerSize = (122, 180)
        self.asteroidSpritesheet = 'Images/Levels/LEVEL_0/Asteroid.png'
        self.asteroidSize = (82, 82)
        self.lvl1GroundSize = (1138, 38)
        self.lvl1StaticBackgroundSpritesheet = 'Images/Levels/LEVEL_1/BACKGROUND.png'
        self.lvl1StaticBackgroundSize = (569, 320)
        self.lvl1DinamicBackgroundSpritesheet = 'Images/Levels/LEVEL_1/spritesheet (3).png'
        self.lvl1DinamicBackgroundSize = (1138, 320)
        self.lvl1DinamicBackgroundAnimationFrames = [1, 1, 1]
        self.lvl1GroundSpritesheet = 'Images/Levels/LEVEL_1/GROUND_2_FLAT.png'
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
        self.lvl2CableSpritesheet = 'Images/Levels/LEVEL_2/FISIERE_VITAEX_LVL2/Cable/cable.png'
        self.lvl2CableSize = (102, 282)
        self.lvl2LaserSpritesheet = 'Images/Levels/LEVEL_2/FISIERE_VITAEX_LVL2/Laser/laser.png'
        self.lvl2LaserSize = (69, 282)
        self.lvl2LaserAnimationFrames = [3, 10]
        self.lvl2PipeSpritesheet = 'Images/Levels/LEVEL_2/FISIERE_VITAEX_LVL2/Pipe/pipe.png'
        self.lvl2PressUpSpriteSheet = 'Images/Levels/LEVEL_2/FISIERE_VITAEX_LVL2/Press/press_up.png'
        self.lvl2PressUpSize = (69, 272)
        self.lvl2PressDownSpriteSheet = 'Images/Levels/LEVEL_2/FISIERE_VITAEX_LVL2/Press/press_down.png'
        self.lvl2PressDownSize = (69, 10)
        self.lvl2PipeSize = (108, 282)
        self.lvl2GroundSize = (569, 38)
        self.lvl2StaticBackgroundSpritesheet = 'Images/Levels/LEVEL_2/FISIERE_VITAEX_LVL2/Background/staticBackground.png'
        self.lvl2StaticBackgroundSize = (569, 320)
        self.lvl2DinamicBackgroundSpritesheet = 'Images/Levels/LEVEL_2/FISIERE_VITAEX_LVL2/Background/spritesheet (22).png'
        self.lvl2DinamicBackgroundSize = (569, 320)
        self.lvl2DinamicBackgroundAnimationFrames = [1, 1, 1]
        self.lvl2GroundSpritesheet = 'Images/Levels/LEVEL_2/FISIERE_VITAEX_LVL2/Background/FLOOR.png'
        self.menuTextSpritesheet = 'Images/Levels/Menu/spritesheet (24).png'
        self.menuTextAnimationFrames = [7]
        self.menuTextSize = (107, 31)

    def getResource(self):
        return self.resourceProvider
