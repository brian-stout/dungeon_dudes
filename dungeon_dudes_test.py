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

class TestClassStr(unittest.TestCase):
    
    def test_object_Creature_str_method(self):
        creature = dungeon_dudes.Creature(0)
        string = creature.__str__()
        self.assertEqual(string, 'Giant Rat: 1 hp')

class TestModuleDice(unittest.TestCase):

    def test_dice_roll_d6(self):
        roll = dungeon_dudes.dice.d6()
        self.assertIn(roll, range(1,6))

    def test_dice_roll_d10(self):
        roll = dungeon_dudes.dice.d10()
        self.assertIn(roll, range(1,10))

    def test_dice_roll_d20(self):
        roll = dungeon_dudes.dice.d20()
        self.assertIn(roll, range(1,20))

    def test_dice_roll_d100(self):
        roll = dungeon_dudes.dice.d100()
        self.assertIn(roll, range(1,100))

    ##def savestate

    ##def menu?
        
        
if __name__ == "__main__":
    unittest.main()
