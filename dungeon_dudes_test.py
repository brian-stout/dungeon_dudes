import unittest
import dungeon_dudes as dungeon_dudes

class TestClassCreation(unittest.TestCase):

    def test_object_Creature_creation(self):
        creature = dungeon_dudes.Creature(0)
        self.assertEqual(creature.creatureType, 0)
        self.assertEqual(creature.hp, 1)
        self.assertEqual(creature.name, "Giant Rat")

    def test_object_Hero_creation(self):
        hero = dungeon_dudes.Hero()

    def test_object_Loot_creation(self):
        loot = dungeon_dudes.Loot()

    def test_object_Dungeon_creation(self):
        dungeon = dungeon_dudes.Dungeon()

    def test_object_Room_creation(self):
        room = dungeon_dudes.Room()

    def test_object_Dice_creation(self):
        dice = dungeon_dudes.Dice()

class TestClassStr(unittest.TestCase):
    
    def test_object_Creature_str_method(self):
        creature = dungeon_dudes.Creature(0)
        string = creature.__str__()
        self.assertEqual(string, 'Giant Rat: 1 hp')

    ##def savestate

    ##def menu?
        
        
if __name__ == "__main__":
    unittest.main()
