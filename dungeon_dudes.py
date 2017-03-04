#!usr/bin/env python3

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
        room = Room()
        roomList.append(room)

    return roomList


def roll_for_initiative(hero, room):
    for monster in room.monsterList:
        monster.initiative = dice.d20()

    hero.initiative = dice.d20()


def check_inventory(hero):
    print("Checking inventory")

def move_to_next_room(room):
    print("Moving to next room")

def hero_status(hero):
    print("Hero status")

def room_enemy_statuses(monsterList):
    print("All the enemy statuses")

def attack_enemy(hero, monster):
    print("Attacking the enemy")

def use_menu(hero, room, monster):

    function_switch = {"A" : check_inventory, "B" : move_to_next_room,
                       "C" : print, "D" : room_enemy_statuses,
                       "E" : hero.attack}

    print("A - Check your inventory")
    if room.is_room_cleared:
        print("B - Move on to the next room")
    else:
        print("B - Sneak to the next room")
    print("C - Check your health")
    print("D - Check their health")
    print("E - Attack the nearest enemy")

    switch = input("Select a menu option")

    
    

def main():

    #TODO:  Prompt hero for name
    hero = Hero("Bob")

    #Creating boss
    boss = Creature(7)

    print("You start your glorious adventure!")

    roomList = generate_rooms()
    currentRoom = 0

    roll_for_initiative(hero, roomList[currentRoom])
    monsterList = roomList[currentRoom].monsterList
    monsterList.sort(reverse=True)
    
    for monster in monsterList:
        print(monster, end="")
        print(" " + str(monster.initiative))

    #use_menu(hero, roomList[currentRoom], roomList[currentRoom].monsterList[0])



if __name__ == "__main__":
    main()
