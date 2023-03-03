from Actions import Actions
from ResourceProvider import ResourceProvider


class Levels:
    def __init__(self):
        self.levels = []
        self.resourcesLvl1 = {}

        self.resourceProvider = ResourceProvider()
        self.action = Actions()

        rubinEnemy = self.resourceProvider.registerResource("rubinEnemy", 'Images/ENEMY_FRAMES/spritesheet.png', [6, 4, 3, 4], (57, 57), self.action.getActions("rubinEnemy"))
        player = self.resourceProvider.registerResource("player", 'Images/ALIEN_FRAMES/spritesheet.png', [4, 6, 3, 1, 2, 4, 6, 3, 1, 2, 3, 6, 2, 3], (57, 57), self.action.getActions("player"))
        playerShip = self.resourceProvider.registerResource("playerShip", 'Images/Alien_Ship/spritesheet.png', [1, 1, 1, 1], (440, 440), self.action.getActions("playerShip"))
        frontBackground = self.resourceProvider.registerResource("lvl1BG", 'Images/Backgrounds/LVL1/dinamicSpritesheet.png', [1, 1, 1], (1138, 320), None)
        behindBackground = self.resourceProvider.registerResource("lvl1BG_behind", 'Images/Backgrounds/LVL1/staticSpritesheet.png', [4], (569, 320), None)
        ground = self.resourceProvider.registerResource("lvl1Ground", 'Images/Backgrounds/LVL1/ground.png', [1], (1138, 38), None)

        self.resourcesLvl1 = {
            "rubinEnemy": rubinEnemy,
            "player": player,
            "playerShip": playerShip,
            "frontBackground": frontBackground,
            "behindBackground": behindBackground,
            "ground": ground
        }
    def getLevelResource(self, level, actor):
        level -= 1
        return self.resourcesLvl1[actor].getResource
