import modules.dice as dice

class Creature():
    ##TODO: Needs to import this from a file stored outside of the program
    ##          or reorganize the list to make each entry single line
    creatureList = [[10, 3, "Hero"], [1, 1, "Giant Rat"], [1, 3, "Wolf"],
                    [3, 1, "Skeleton"], [2, 2, "Goblin"], [5, 1, "Undead"],
                    [5, 3, "Orc Warrior"], [10, 3, "The Overlord"]]

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
    #TODO: Raise exceptions for trying to set values like DiceRolls, or maxHp

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

    def __str__(self):
        return self._name + ": " + str(self._hp) + "/" + str(self._maxHp) + " hp"

    def __lt__(self, other):
        return self.initiative < other.initiative

    def __gt__(self, other):
        return self.initiative > other.initiative


    def take_damage(self, dmg):
        self.hp -= dmg
        #Ensures no overkills happens
        if self.hp < 0:
            self.hp = 0

    def attack(self, other):

        selfHighestRoll = 0
        for numberOfRolls in range(self.diceRolls):
            roll = dice.d6()
            if roll > selfHighestRoll:
                selfHighestRoll = roll

        otherHighestRoll = 0
        for numberOfRolls in range(other.diceRolls):
            roll = dice.d6()
            if roll > otherHighestRoll:
                otherHighestRoll = roll

        if selfHighestRoll >= otherHighestRoll:
            print(self.name + " hit " + other.name + "!")
            other.take_damage(1)
        else:
            print(self.name + " missed " + other.name + "!")
      

    def is_dead(self):
        if self.hp == 0:
            return True
        else:
            return False

if __name__ == '__main__': pass

