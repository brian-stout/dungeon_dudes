#!usr/bin/env python3

#Importing math for ceil
import math

#Importing the classes for the objects in this game
from entities.creature import Creature
from entities.hero import Hero
from entities.loot import Loot
from entities.room import Room

#Importing functions from modules for the game
import modules.dice as dice

def generate_rooms():
    numberOfRooms = 6 + dice.d6()
    roomList = list()

    for number in range(0, numberOfRooms):
        #Every 3 rooms the room type will go up by one
        room = Room(math.ceil(Room.numberOfRooms/3))
        roomList.append(room)

    roomList[-1].make_boss_room()

    return roomList


def roll_for_initiative(hero, monsterList):
    for monster in monsterList:
        monster.initiative = dice.d20()

    hero.initiative = dice.d20()

def move_to_next_room(room):
    if room.cleared:
        room.movingRooms = True
    else:
        for monster in room.monsterList:
            if monster.name == "The Overlord":
                break
            roll = dice.d20()
            if roll < 15:
                break
            else:
                room.movingRooms = True

            
def hero_status(hero):
    print(hero)

def room_enemy_statuses(monsterList):
    for monster in monsterList:
        print(monster)

def use_menu(hero, room):

    print("A - Check your inventory")
    if room.cleared:
        print("B - Move on to the next room")
    else:
        print("B - Sneak to the next room")
    print("C - Check your health")
    if not room.cleared:
        print("D - Check their health")
    if not room.cleared:
        print("E - Attack the nearest enemy")

    while True:
        switch = input("Select a menu option: ")

        if switch.upper() == "A":
            hero.print_inventory()
        elif switch.upper() == "B":
            move_to_next_room(room)
            break
        elif switch.upper() == "C":
            hero_status(hero)
        elif switch.upper() == "D":
            room_enemy_statuses(room.monsterList)
        elif switch.upper() == "E":
            if room.cleared:
                print("There are no monsters to fight!")
            else:
                print("")
                hero.attack(room.monsterList[0])
                if room.monsterList[0].is_dead():
                    room.monsterList.pop(0)
                    loot = Loot(dice.d10())
                    hero.add_to(loot)
                if not room.monsterList:
                    room.cleared = True
            break
        elif switch.upper() == "Q":
            exit()
        else:
            print("Please enter a proper value")
        

    
    

def main():

    #TODO:  Prompt hero for name
    hero = Hero("Bob")

    #Creating boss
    boss = Creature(7)

    print("You start your glorious adventure! \n")

    roomList = generate_rooms()
    currentRoom = 0

    while True:
        if currentRoom == Room.numberOfRooms:
            break

        roomList[currentRoom].room_description()

        monsterList = roomList[currentRoom].monsterList
        roll_for_initiative(hero, monsterList)

        monsterList.sort(reverse=True)

        if(monsterList[0].initiative > hero.initiative):
            print(monsterList[0].name + " got the jump on the hero!\n")
            monsterList[0].attack(hero)
        while True:
            use_menu(hero, roomList[currentRoom])
            if roomList[currentRoom].movingRooms == True:
                currentRoom += 1
                break
            elif roomList[currentRoom].cleared == False:
                print("")
                monsterList[0].attack(hero)
                if hero.is_dead():
                    print("The hero is dead!")
                    exit() #more legitimate exit here

    print("You have succeeded in your quest!")



if __name__ == "__main__":
    main()
