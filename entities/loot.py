import modules.dice as dice

class Loot():

    lootList = [[],[1, "Wooden stick", "A worthless wooden stick you couldn't help but pick up"],
                [10, "Silver locket", "A shiny golden locket which can't be opened for some reason"],
                [2, "Skull", "To be used for monologue before final boss"],
                [8, "", "A worthless wooden stick you couldn't help but pick up."],
                [20, "Golden Locket", "On the inside contains a picture of two loving skeletons"],
                [30, "Golden Ring", "With no enchantments this item is virtually worthless"],
                [40, "Diamond Ring", "Slightly less worthless then a golden ring"],
                [50, "Diamond encrusted goblet", "Seems impractical to drink out of"],
                [10, "Katana", "This sword isn't very useful, but it looks cool I guess"],
                [1000, "The OverLord's medallion", "With this you could become overlord ya know."]]

    def __init__(self, lootType = 0):
        self._lootType = lootType
        self._value = Loot.lootList[lootType][0]
        self._name = Loot.lootList[lootType][1]
        self._description = Loot.lootList[lootType][2]

    @property
    def lootType(self):
        return self._lootType 

    @property
    def value(self):
        return self._value

    @property
    def name(self):
        return self._name

    @property
    def description(self):
        return self._description

    @lootType.setter
    def lootType(self, lootType):
        self._lootType = lootType

    @value.setter
    def value(self, value):
        self._value = value

    @name.setter
    def name(self, name):
        self._name = name

    @description.setter
    def description(self, description):
        self._description = description

    def __str__(self):
        return self._name + " (" + str(self._value) + ") " + self._description

if __name__ == '__main__': pass
