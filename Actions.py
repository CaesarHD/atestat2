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
                         "dead": 15,
                         "deadInAir": 16}

        guardianActions = {"idle": 0,
                         "walk": 0,
                         "preJump": 0,
                         "jump": 0,
                         "landing": 0,
                         "idleArmed": 0,
                         "walkArmed": 0,
                         "preJumpArmed": 0,
                         "jumpArmed": 0,
                         "landingArmed": 0,
                         "idleShoot": 1,
                         "walkShoot": 0,
                         "preJumpShoot": 0,
                         "jumpShoot": 0,
                         "landingShoot": 0,
                         "dead": 0,
                         "deadInAir": 0}

        rubinsActions = {"idleArmed": 0,
                         "walkArmed": 1,
                         "idleShoot": 2,
                         "jumpShoot": 2,
                         "walkShoot": 3,
                         "dead": 4,
                         "idle": 0,
                         "walk": 0,
                         "preJump": 0,
                         "jump": 0,
                         "landing": 0,
                         "preJumpArmed": 0,
                         "jumpArmed": 0,
                         "landingArmed": 0,
                         "preJumpShoot": 0,
                         "landingShoot": 0,
                         "deadInAir": 0
                         }

        playerShipActions = {"landedOFF": 0,
                             "airOFF": 1,
                             "landedON": 2,
                             "airON": 3}

        self.__cache = {"player": playerActions,
                        "rubinEnemy": rubinsActions,
                        "playerShip": playerShipActions,
                        "guardian": guardianActions}

    def getActions(self, name):
        return self.__cache[name]
