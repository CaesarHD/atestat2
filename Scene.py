from Enemy import Enemy
from Levels import Levels

RUBIN_ENEMY_BULLET_SIZE = 3.5
RUBIN_ENEMY_BULLET_SPAWN_LOCATION = 30
RUBIN_ENEMY_SIZE = 2


class Scene:

    def __init__(self):
        self.rubinEnemies = []
        self.level = Levels()
        self.resourceProvider = self.level.loadResourcesLevel(1)
        self.enemyPositions = [3000, 4000, 4500, 5500, 6000, 6100, 7000, 7200, 7500, 9000, 9500, 10000, 10100,
                               12000, 13000, 13100, 14500, 14900, 17000, 17100, 17200, 17800, 20000, 20100, 20500, 21000, 21050, 21100, 21500, 22000]

    def generateEnemy(self):
        for pos in self.enemyPositions:
            self.rubinEnemies.append(
                Enemy((pos, 100), RUBIN_ENEMY_SIZE, self.resourceProvider.getResource("rubinEnemy"),
                      RUBIN_ENEMY_BULLET_SIZE,
                      RUBIN_ENEMY_BULLET_SPAWN_LOCATION))
