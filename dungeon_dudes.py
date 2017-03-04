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

"""
    generate_rooms() is responsible for creating a list of rooms for the players to travel
        through.

    It does so by getting a random number from 1 to 6 and adding it to 6, so the smallest 
room count can be 7 and the highest can be 6.

    It picks the room type by divding the number of rooms by 3 and celing it, so 
every 3 rooms There's another type.

    The function also makes sure the last room in the list is the boss room
"""
def generate_rooms():
    numberOfRooms = 6 + dice.d6()
    roomList = list()

    for number in range(0, numberOfRooms):
        #Every 3 rooms the room type will go up by one
        room = Room(math.ceil(Room.numberOfRooms/3))
        roomList.append(room)

    roomList[-1].make_boss_room()

    return roomList

"""
    roll_for_initiative() sets the initiative value for the hero and every monster at the start
        of every battle.
"""
def roll_for_initiative(hero, monsterList):
    for monster in monsterList:
        monster.initiative = dice.d20()

    hero.initiative = dice.d20()

"""
        move_to_next_room() is responsible for handling the logic for transitioning 
            to the next room

        If the room has been cleared the hero will always move on to the next room.  
            Otherwise, The hero must roll a 15 or higher for every monster 
            in the room to escape

        If the hero is in the boss room he can't escape
"""
def move_to_next_room(room):
    if room.cleared:
        room.movingRooms = True
    else:
        for monster in room.monsterList:
            if monster.name == "The Overlord":
                print("The OverLord laughs at your attempt to escape!")
                break
            roll = dice.d20()
            if roll < 15:
                print("Your escape attempt failed!")
                break
            else:
                print("You successfully escaped to the next room!\n")
                room.movingRooms = True
                break

"""
    room_enemy_statuses() prints out the statuses of all the monsters in the Monsterlist
"""
def room_enemy_statuses(monsterList):
    for monster in monsterList:
        print(monster)


"""
    use_menu() is the main function that handles the game play logic

    The loop exists so the player turn isn't ended by checking statuses.  Only by actions such
        as attacking or attempting to escape.
"""
def use_menu(hero, room):

    print("A - Check your inventory")
    #Changes what the B option says based if they're enemies to impede the player
    if room.cleared:
        print("B - Move on to the next room")
    else:
        print("B - run to the next room")
    print("C - Check your health")
    #Doesn't give you the option to check the health of all the dead enemies
    if not room.cleared:
        print("D - Check their health")
    #If there are no enemies to be attacked then the menu won't prompt the user to
    if not room.cleared:
        print("E - Attack the nearest enemy")

    while True:
        switch = input("Select a menu option: ")

        #Chained ELIF's acting as a switch statement
        if switch.upper() == "A":
            hero.print_inventory() #Check inventory
        elif switch.upper() == "B":
            move_to_next_room(room) #Attempt to move to the next room
            break
        elif switch.upper() == "C":
            print(hero) #Prints out the hero's name and hp
        elif switch.upper() == "D":
            room_enemy_statuses(room.monsterList) #Prints out all the monster's names and hp
        elif switch.upper() == "E":
            #If the room is empty and the player tries to attack nothing the game lets em know
            if room.cleared:
                print("\nThere are no monsters to fight!")
            else:
                #Attacks the monster with the highest initiative
                hero.attack(room.monsterList[0])
                #Checks to see if attack killed it
                if room.monsterList[0].is_dead():
                    room.monsterList.pop(0) #Remove monster from list
                    loot = Loot(dice.d10()) #Get a random loot drop from monster
                    hero.add_to(loot)
                #If there's no more monsters in the list, the room has been cleared
                if not room.monsterList:
                    room.cleared = True
            break
        #Option to quit the program
        elif switch.upper() == "Q":
            exit()
        #Default option for if the user inputs a bad letter
        else:
            print("Please enter a proper value")


def main():

    #Create's a hero with the chosen name
    name = input("What is the hero's name? : ")
    hero = Hero(name)

    #Creating boss
    boss = Creature(7)

    print("You start your glorious adventure! \n")

    #Create's a list of rooms for  the hero to move through
    roomList = generate_rooms()
    currentRoom = 0

    #Main gameplay loop
    while True:
        
        #If this is true, that means currentRoom has been incremented past the roomList index
        #And there aren't any rooms left to go through so the hero won
        if currentRoom == Room.numberOfRooms:
            break

        #Runs a function that prints the name of the room and gives a description
        roomList[currentRoom].room_description()

        #Makes a shorter reference to improve readability
        monsterList = roomList[currentRoom].monsterList

        #Sets the initiative for all the monsters
        roll_for_initiative(hero, monsterList)

        #Makes it so the monster with the highest initiative is in index 0
        monsterList.sort(reverse=True)

        #If the monster's initiative is higher, he gets to attack first
        if(monsterList[0].initiative > hero.initiative):
            print(monsterList[0].name + " got the jump on the hero!\n")
            monsterList[0].attack(hero)
        while True:

            #Prompts the user for what he wants to do
            use_menu(hero, roomList[currentRoom])
            
            #If the user has successfully completed the room, set the currentRoom index one higher
            #So the next loop uses the next room's information
            if roomList[currentRoom].movingRooms == True:
                currentRoom += 1
                break

            #Checks to see if there's monsters
            elif roomList[currentRoom].cleared == False:
                print("")
                monsterList[0].attack(hero) #First monster attacks the player
                #Checks to see if the player died
                if hero.is_dead():
                    print("The hero is dead!")
                    exit()

    print("You have succeeded in your quest to escape The Overlord's strong hold")

if __name__ == "__main__":
    main()
