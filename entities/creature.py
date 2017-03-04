import modules.dice as dice

"""
    The creature class is responsible for creating all the living objects in the game, including
        the player.

    It contains the basic logic for the actions living things can take, such as dying
        or attacking things.

    It also contains the data for a creature's initaitive, his hp, and how many attack rolls
        he gets.

    A multidimensional class variable is used to generate the hard coded data.
"""
class Creature():

    #HP, number of attack die, and the a creature name
    creatureList = [[20, 3, "Hero"], [1, 1, "Giant Rat"], [1, 2, "Wolf"],
                    [3, 1, "Skeleton"], [2, 2, "Goblin"], [5, 1, "Undead"],
                    [5, 2, "Orc Warrior"], [10, 2, "The Overlord"]]

    def __init__(self, creatureType = 0):
        self._creatureType = creatureType
        self._maxHp = Creature.creatureList[creatureType][0]
        self._hp = Creature.creatureList[creatureType][0]
        self._diceRolls = Creature.creatureList[creatureType][1]
        self._name = Creature.creatureList[creatureType][2]
        self._initiative = 0

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

    @property
    def initiative(self):
        return self._initiative

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

    @initiative.setter
    def initiative(self, initiative):
        self._initiative = initiative

    #Prints out the name and it's hp/maxHP
    def __str__(self):
        return self._name + ": " + str(self._hp) + "/" + str(self._maxHp) + " hp"

    #Used by the sort function to sort monsters by there initiative
    def __lt__(self, other):
        return self.initiative < other.initiative

    def __gt__(self, other):
        return self.initiative > other.initiative

    #A function that damages the creature, can be used for traps or when another creature
    #successfully attacks this one
    def take_damage(self, dmg):
        self.hp -= dmg
        #Ensures no overkills happens
        if self.hp < 0:
            self.hp = 0

    #Logic handles attacking another creature.  Goes through with the dice rolls and determines
    #Which one happens based on the highest dice roll
    def attack(self, other):

        selfHighestRoll = 0 #Highest roll for the creature attacking
        #Rolls the dice by the amount of rolls the creature has
        for numberOfRolls in range(self.diceRolls):
            roll = dice.d6()
            if roll > selfHighestRoll:
                selfHighestRoll = roll

        #Same thing for the other creature
        otherHighestRoll = 0
        for numberOfRolls in range(other.diceRolls):
            roll = dice.d6()
            if roll > otherHighestRoll:
                otherHighestRoll = roll

        #If self wins then the other takes the damage
        if selfHighestRoll >= otherHighestRoll:
            print(self.name + " hit " + other.name + "!\n")
            other.take_damage(1)
        #If self loses then it displays a miss
        else:
            print(self.name + " missed " + other.name + "!\n")
      
    #method to quickly check if something is dead
    def is_dead(self):
        if self.hp == 0:
            return True
        else:
            return False

if __name__ == '__main__': pass

