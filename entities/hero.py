from entities.creature import Creature

class Hero(Creature):
    def __init__(self, name):
        super().__init__(0)
        self._name = name
        self._inventory = list()

    @property
    def inventory(self):
        return inventory

    def add_to(self, loot):
        self._inventory.append(loot)

    def print_inventory(self):
        if self._inventory:
            print("Your inventory contains: \n")
            for items in self._inventory:
                print(items)
        else:
            print("Your inventory is empty\n")

if __name__ == '__main__': pass
