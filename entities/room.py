from entities.creature import Creature
from entities.loot import Loot
import modules.dice as dice



class Room():
    numberOfRooms = 0

    def __init__(self):
        self._monsterList = self.generate_monster_list()
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

    def generate_monster_list(self):
        monsterList = list()

        roll = dice.d6()
        monster = Creature(dice.d6())
        monsterList.append(monster)

        if roll < 4:
            monster = Creature(dice.d6())
            monsterList.append(monster)

        return monsterList

    def make_boss_room(self):
        monsterList = list()
        monster = Creature(7)
        monsterList.append(monster)

        self._monsterList = monsterList

if __name__ == '__main__': pass
