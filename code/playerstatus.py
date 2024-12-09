
max_up = 5

class PlayerStatus():
    def __init__(self):
        # resource
        self.gold = 0

        # score
        self.score = 0

        # Upgrade
        self.fighterHPUpgrade = 0
        self.shieldturretHPUpgrade = 0
        self.gunturretATKUpgrade = 0

    # method
    def getfighterHPUpgrade(self):
        return self.fighterHPUpgrade
    def setfighterHPUpgrade(self, level):
        self.fighterHPUpgrade = level

    def getshieldturretHPUpgrade(self):
        return self.shieldturretHPUpgrade
    def setshieldturretHPUpgrade(self, level):
        self.shieldturretHPUpgrade = level

    def getgunturretATKUpgrade(self):
        return self.gunturretATKUpgrade
    def setgunturretATKUpgrade(self, level):
        self.gunturretATKUpgrade = level

    # Upgrade
    def upgradefighterHP(self):
        if self.fighterHPUpgrade < max_up:
            self.fighterHPUpgrade += 1
    def upgradeshieldturretHP(self):
        if self.shieldturreHPUpgrade < max_up:
            self.shieldturreHPUpgrade += 1
    def upgradegunturreATK(self):
        if self.gunturretATKUpgrade < max_up:
            self.gunturretATKUpgrade += 1
    pass

status = PlayerStatus()