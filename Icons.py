from Actions import Actions
from Actor import Actor


class Icons(Actor):
    def __init__(self, pos, scale, resource):
        super().__init__(pos, scale, resource)
        self.action = Actions()
        self.actions = resource.actions
        self.action = 0

    def abilityState(self, state):
        match state:
            case 'idle':
                self.action = self.actions['idle']
            case 'active':
                self.action = self.actions['active']
            case 'passive':
                self.action = self.actions['passive']

    def abilityChangeState(self, player):
        if player.abilityOn:
            self.abilityState('idle')
            if player.useAbility:
                self.abilityState('active')
        else:
            self.abilityState('passive')

    def gunIconStatus(self, player):
        if player.isArmed:
            self.abilityState('active')
        else:
            self.abilityState('idle')

    def lifeBarStages(self, player):
        match player.bulletsReceived:
            case 0: self.action = 10
            case 1: self.action = 9
            case 2: self.action = 8
            case 3: self.action = 7
            case 4: self.action = 6
            case 5: self.action = 5
            case 6: self.action = 4
            case 7: self.action = 3
            case 8: self.action = 2
            case 9: self.action = 1
            case 10: self.action = 0
        if player.isDead:
            self.action = 10

