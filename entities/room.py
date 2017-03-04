from entities.creature import Creature
from entities.loot import Loot
import modules.dice as dice

"""
    The room class create's objects that contain the metadata for the rooms the player is currently
        in.

    It's has a multi-dimensional list which contains a room name and it's description used to
        texts when a player enters a new room.

    The room also contains a list of monsters for easy access by the game logic.
"""
class Room():

    roomDesc = [["dark dank dungeon. ", """You're surrounded by stone. The room is dimly lit, and from what you can see the walls are incredibly dirty. """],
                ["well lit dank dungeon. ", """You're surrounded by stone. The room is well lit, showing just how awful the designer of this dungeon did. """],
                ["normal room. ", """Out of the dungeon, the walls look like a regular castle.  There's armor and mediocre paintings lining up against the wall"""],
                ["castle courtyard. ", """The sun spills from over the castle walls.  The dirt below your feet is well packed from constant travel.  You're surrounded by castle walls"""],
                ["castle exit. ", """The only exit to the castle is a large oak wooden door.  At the opening stands the king of the castle, a villainous man know only as The Overlord"""]]

    numberOfRooms = 0

    def __init__(self, roomType = 0):
        #Create a list of monsters
        self._monsterList = self.generate_monster_list()
        self._cleared = False
        self._movingRooms = False
        self._roomType = roomType
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

        #Pick a monster to add
        roll = dice.d6()
        monster = Creature(dice.d6())
        monsterList.append(monster)

        #If the monster was weaker add another
        if roll < 4:
            monster = Creature(dice.d6())
            monsterList.append(monster)

        return monsterList

    #Function making it easy to set the last room of the room list to a boss room
    def make_boss_room(self):
        monsterList = list()
        #Adding the boss, and overwriting the base mobs
        monster = Creature(7)
        monsterList.append(monster)

        #roomType 4 is the boss room
        self.roomType = 4
        self._monsterList = monsterList

    #Used to print a description of the room upon entering it
    def room_description(self):
        print ("You enter a " + Room.roomDesc[self._roomType][0])
        print(Room.roomDesc[self._roomType][1] + "\n")

if __name__ == '__main__': pass
