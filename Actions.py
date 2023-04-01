class Actions:
    def __init__(self):
        playerActions = {"idle": 0,
                         "walk": 1,
                         "preJump": 2,
                         "jump": 3,
                         "landing": 4,
                         "idleArmed": 5,
                         "walkArmed": 6,
                         "preJumpArmed": 7,
                         "jumpArmed": 8,
                         "landingArmed": 9,
                         "idleShoot": 10,
                         "walkShoot": 11,
                         "preJumpShoot": 12,
                         "jumpShoot": 13,
                         "landingShoot": 14,
                         "dead": 15}

        rubinsActions = {"idleArmed": 0,
                         "walkArmed": 1,
                         "idleShoot": 2,
                         "jumpShoot": 2,
                         "walkShoot": 3,
                         "dead": 4}

        playerShipActions = {"landedOFF": 0,
                             "airOFF": 1,
                             "landedON": 2,
                             "airON": 3}

        self.__cache = {"player": playerActions,
                        "rubinEnemy": rubinsActions,
                        "playerShip": playerShipActions}

    def getActions(self, name):
        return self.__cache[name]
