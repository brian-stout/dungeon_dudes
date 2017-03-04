from entities.creature import Creature
from entities.loot import Loot
import modules.dice as dice

def generate_loot_objects():
    pass

def generate_monster_list():
    monster = Creature(dice.d6())
    monsterList = list()
    monsterList.append(monster)
    return monsterList

class Room():
    numberOfRooms = 0

    def __init__(self):
        self._monsterList = generate_monster_list()
        self._roomCleared = False
        Room.numberOfRooms += 1

    @property
    def monsterList(self):
        return self._monsterList

    @property
    def roomCleared(self):
        return self._roomCleared

    @roomCleared.setter
    def roomCleared(self, boolean):
        self._roomCleared = boolean

    def is_room_cleared():
        return self._roomCleared

if __name__ == '__main__': pass
