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

def generate_menu(hero, room):
    print("A - Check your inventory")
    if room.is_room_cleared:
        print("B - Move on to the next room")
    else:
        print("B - Sneak to the next room")
    print("C - Check your health")
    print("D - Check their health")
    print("E - Attack the nearest enemy")

    
    

def main():

    #TODO:  Prompt hero for name
    hero = Hero("Bob")

    #Creating boss
    boss = Creature(7)

    print("You start your glorious adventure!")

    roomList = generate_rooms()

    print(roomList)

if __name__ == "__main__":
    main()
