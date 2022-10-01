import math
from players import *
from enemy import *
from text_and_sounds_functions import *
# import os
# import time
import random


def if_want_to_play():

    options = 4
    counter_play = 0
    for answer in range(options):
        answer = input("Do you want to begin your adventure?\nEnter 'y' for yes or 'n' for no.\n").lower()
        if answer == "y":
            print("Alright then, let's begin!\n")
            break
        elif answer == "n":
            print("Then come back when you have the balls!\n")
            break
        else:
            counter_play += 1
            if counter_play < 3:
                print("Enter 'yes/no'!")
            elif counter_play == 3:
                print("Last chance to chose an option, otherwise I will exit!")
            elif counter_play == 4:
                print("Told you!")


def select_character():

    print("These are your option:")
    Messages.char_options()
    max_try = 4
    char_sel = Player
    counter_options = 0
    for char_sel in range(max_try):
        char_sel = int(input("Brave man, as what hero do you chose to begin?\n"))
        if char_sel == 1:
            (Messages.warrior_intro())
            char_sel = Warrior
            break
        elif char_sel == 2:
            (Messages.wizard_intro())
            char_sel = Wizard
            break
        elif char_sel == 3:
            (Messages.elf_intro())
            char_sel = Elf
            break
        elif char_sel == 4:
            (Messages.archer_intro())
            char_sel = Archer
            break
        else:
            counter_options += 1
            if counter_options < 3:
                print("Enter a valid option!")
            elif counter_options == 3:
                print("Last chance to chose an option, otherwise I will exit!")
            elif counter_options == 4:
                print("Told you!")

    return char_sel


# Sounds.main_menu_sound()
Messages.intro_msg()
if_want_to_play()
chosen_character = select_character()
player_name = input(f"Please enter your name, brave {chosen_character.__name__}: \n")


def chosen_path():

    print(f"My dear {player_name}, you begin your journey back to your throne and you have arrived\n"
          f" to a crossroad and you have to chose a path on which you want to go to\n")
    PathOptions.choose_path()
    path_option = ""
    path_num = 4
    for path in range(path_num):
        path = int(input("Please select a option: \n"))
        if path == 1:
            path_option = "forest"
            PathMessages.forest_message()
            break
        elif path == 2:
            path_option = "town"
            PathMessages.town_message()
            break
        elif path == 3:
            path_option = "dungeon"
            PathMessages.dungeon_message()
            break
        else:
            print("Enter a valid path option!")
            continue
    return path_option


chosen_path()
# Sounds.exploring_sound()


def if_open_chest():
    print(f"This are you weapons now: \n{chosen_character().type_of_weapon} - {chosen_character().weapon}\n"
          f"{chosen_character().type_of_armour} - {chosen_character().armour}\n")
    chest_open = input("Do you open the chest?\n 'y' for yes 'n' for no!\n")
    if chest_open == "y":
        chosen_character().open_chest()
        chosen_character().total_points()
        print(f"This are you new weapons: \n{chosen_character().type_of_weapon} - {chosen_character().weapon}\n"
            f"{chosen_character().type_of_armour} - {chosen_character().armour}\n")
    elif chest_open == "n":
        print("You move on with what do you already have!")
    else:
        print("Choose a valid option!")

if_open_chest()


def battle_scene(user, enemy):

    user.attack(enemy)
    print(f"You are attacking with a power of {user.power}, your have {user.life} ")
    enemy.attack(user)
    print(f'{enemy.type_of} is attacking you with a power of {enemy.power} and he has {enemy.life} left\n')
    if user.life <= 0:
        print(f"Our {user.type_of} has been killed by a {enemy.type_of}!")
    elif enemy.hp <= 0:
        print(f'Well done grand {user.type_of}!!! You defeated the {enemy.type_of}\n')
