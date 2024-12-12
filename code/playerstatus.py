
max_up = 10

class PlayerStatus():
    def __init__(self):
        # resource
        self.gold = 200

        # score
        self.score = 0
        self.round = 1

        # Upgrade
        self.fighterHPUpgrade = 0
        self.fighterATKUpgrade = 0
        self.shieldturretHPUpgrade = 0
        self.gunturretATKUpgrade = 0

        self.roundstarttime = None
        self.bRound = False
    # method
    def getfighterHPUpgrade(self):
        return self.fighterHPUpgrade
    def setfighterHPUpgrade(self, level):
        self.fighterHPUpgrade = level

    def getfighterATKUpgrade(self):
        return self.fighterATKUpgrade
    def setfighterATKUpgrade(self, level):
        self.fighterATKUpgrade = level

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
            self.gold -= 1000
            self.fighterHPUpgrade += 1
    def upgradefighterATK(self):
        if self.fighterATKUpgrade < max_up:
            self.gold -= 1000
            self.fighterATKUpgrade += 1
    def upgradeshieldturretHP(self):
        if self.shieldturretHPUpgrade < max_up:
            self.gold -= 1000
            self.shieldturretHPUpgrade += 1
    def upgradegunturreATK(self):
        if self.gunturretATKUpgrade < max_up:
            self.gold -= 1000
            self.gunturretATKUpgrade += 1

    def upgradeCheck(self):
        if self.gold < 1000:
            return False
        else:
            return True

status = PlayerStatus()