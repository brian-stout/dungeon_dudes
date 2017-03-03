class Creature():
    def __init__(self):
        self._hp = 1
        self._creatureType = 0

    @property
    def hp(self):
        return self._hp

    @property
    def type(self):
        return self._type

    @hp.setter
    def hp(self, hp):
        self._hp = hp

    @type.setter
    def type(self, creatureType):
        self._creatureType = creatureType

if __name__ == '__main__': pass

