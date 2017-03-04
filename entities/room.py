from entities.creature import Creature
from entities.loot import Loot
import modules.dice as dice

def generate_loot_objects():
    pass

def generate_monster_list():
    monsterList = list()
    monster = Creature(dice.d6())
    monsterList.append(monster)
    monster = Creature(dice.d6())
    monsterList.append(monster)
    return monsterList

class Room():
    numberOfRooms = 0

    def __init__(self):
        self._monsterList = generate_monster_list()
        self._cleared = False
        self._movingRooms = False
        Room.numberOfRooms += 1

    @property
    def monsterList(self):
        return self._monsterList

    @property
    def cleared(self):
        return self._cleared

    @property
    def movingRooms(self):
        return self._movingRooms

    @cleared.setter
    def cleared(self, boolean):
        self._cleared = boolean

    @movingRooms.setter
    def movingRooms(self, boolean):
        self._movingRooms = boolean

if __name__ == '__main__': pass
