import unittest
import dungeon_dudes as dungeon_dudes

class TestClassCreature(unittest.TestCase):

    def test_object_Creature_creation(self):
        creature = dungeon_dudes.Creature(0)
        self.assertEqual(creature.creatureType, 0)
        self.assertEqual(creature.hp, dungeon_dudes.Creature.creatureList[0][0])
        self.assertEqual(creature.maxHp, dungeon_dudes.Creature.creatureList[0][0])
        self.assertEqual(creature.name, "Giant Rat")

    def test_object_Creature_damage_method(self):
        creature = dungeon_dudes.Creature(0)
        creature.damage(1)
        self.assertEqual(creature.hp, 1)
        self.assertEqual(creature.maxHp, dungeon_dudes.Creature.creatureList[0][0])

        #Tests to make hp never drops below 0
        creature.damage(10)
        self.assertEqual(creature.hp, 0)

    def test_object_Creature_is_dead_method(self):
        creature = dungeon_dudes.Creature(0)
        creature.damage(2)
        self.assertTrue(creature.is_dead())

    def test_object_Creature_str_method(self):
        creature = dungeon_dudes.Creature(0)
        string = creature.__str__()
        self.assertEqual(string, 'Giant Rat: 2 hp')

class TestClassHero(unittest.TestCase):

    def test_object_Hero_creation(self):
        hero = dungeon_dudes.Hero()

class TestClassLoot(unittest.TestCase):

    def test_object_Loot_creation(self):
        loot = dungeon_dudes.Loot()

class TestClassDungeon(unittest.TestCase):

    def test_object_Dungeon_creation(self):
        dungeon = dungeon_dudes.Dungeon()

class TestClassRoom(unittest.TestCase):

    def test_object_Room_creation(self):
        room = dungeon_dudes.Room()

class TestModuleDice(unittest.TestCase):

    def test_dice_roll_d6(self):
        roll = dungeon_dudes.dice.d6()
        self.assertIn(roll, range(1,7)) #Gives number between 0 and 7 (1-6)

    def test_dice_roll_d10(self):
        roll = dungeon_dudes.dice.d10()
        self.assertIn(roll, range(1,11))

    def test_dice_roll_d20(self):
        roll = dungeon_dudes.dice.d20()
        self.assertIn(roll, range(1,21))

    def test_dice_roll_d100(self):
        roll = dungeon_dudes.dice.d100()
        self.assertIn(roll, range(1,101))

    ##def savestate

    ##def menu?
        
        
if __name__ == "__main__":
    unittest.main()
