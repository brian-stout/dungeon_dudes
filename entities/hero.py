from entities.creature import Creature


"""
    A hero character (the playable character.)  Is essentially a creature with the ability
        to keep an inventory and have a dynamic name
"""
class Hero(Creature):
    def __init__(self, name):
        #Initializing all the creature's values
        super().__init__(0)
        #Player can set his name
        self._name = name
        self._inventory = list()

    @property
    def inventory(self):
        return inventory

    #Adding loot to the inventory
    def add_to(self, loot):
        self._inventory.append(loot)

    def print_inventory(self):
        #Makes sure there actually is something in the inventory first
        if self._inventory:
            print("Your inventory contains: \n")
            for items in self._inventory:
                print(items)
        else:
            print("Your inventory is empty\n")

if __name__ == '__main__': pass
