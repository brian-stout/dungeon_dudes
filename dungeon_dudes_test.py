import unittest
import dungeon_dudes as dungeon_dudes

class TestFunction(unittest.TestCase):

    def test_object_Creature_creation(self):
        creature = dungeon_dudes.entities.Creature()

    def test_object_Hero_creation(self):
        hero = dungeon_dudes.entities.Hero()

    def test_object_Loot_creation(self):
        loot = dungeon_dudes.entities.Loot()

    def test_object_Dungeon_creation(self):
        dungeon = dungeon_dudes.entities.Dungeon()

    def test_object_Room_creation(self):
        room = dungeon_dudes.entities.Room()

    def test_object_Dice_creation(self):
        dice = dungeon_dudes.entities.Dice()

    ##def savestate

    ##def menu?
        
        
if __name__ == "__main__":
    unittest.main()
