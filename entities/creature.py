class Creature():
    ##TODO: Needs to import this from a file stored outside of the program
    ##          or reorganize the list to make each entry single line
    ##TODO:
    ##TODO:
    ##TODO:  Add a number of dice rolls to the creatureList
    ##TODO:
    ##TODO:
    creatureList = [[10,3, "Hero"], [2, 1, "Giant Rat"]]

    def __init__(self, creatureType = 0):
        self._creatureType = creatureType
        self._maxHp = Creature.creatureList[creatureType][0]
        self._hp = Creature.creatureList[creatureType][0]
        self._diceRolls = Creature.creatureList[creatureType][1]
        self._name = Creature.creatureList[creatureType][2]

    @property
    def maxHp(self):
        return self._maxHp

    @property
    def hp(self):
        return self._hp

    @property
    def diceRolls(self):
        return self._diceRolls

    @property
    def creatureType(self):
        return self._creatureType

    @property
    def name(self):
        return self._name

    @hp.setter
    def hp(self, hp):
        self._hp = hp

    @name.setter
    def name(self, name):
        self._name = name

    @creatureType.setter
    def creatureType(self, creatureType):
        self._creatureType = creatureType
        self._name = Creature.creatureList[creatureType][1]

    def __str__(self):
        return self._name + ": " + str(self._hp) + "/" + str(self._maxHp) + " hp"

    def take_damage(self, dmg):
        self.hp -= dmg
        #Ensures no overkills happens
        if self.hp < 0:
            self.hp = 0

    def is_dead(self):
        if self.hp == 0:
            return True
        else:
            return False

if __name__ == '__main__': pass

