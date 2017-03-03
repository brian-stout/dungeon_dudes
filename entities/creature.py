class Creature():
    ##TODO: Needs to import this from a file stored outside of the program
    creatureList = [[1, "Giant Rat"]]

    def __init__(self, creatureType):
        self._creatureType = creatureType
        self._hp = Creature.creatureList[creatureType][0]
        self._name = Creature.creatureList[creatureType][1]

    @property
    def hp(self):
        return self._hp

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

if __name__ == '__main__': pass

