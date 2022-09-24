import game_functions
from players import *
from text_and_sounds_functions import *
# import os
# import time
# import random


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

chest_open = input("Do you open the chest?\n 'y' for yes 'n' for no!\n")
if chosen_character == Warrior:
    if chest_open == "y":
        game_functions.random_items_warrior()
        print(Warrior().inventory)
    elif chest_open == "n":
        print("You move on with what do you already have!")
    else:
        print("Chose a valid option!")
elif chosen_character == Wizard:
    if chest_open == "y":
        game_functions.random_items_wizard()
        print(Wizard().inventory)
    elif chest_open == "n":
        print("You move on with what do you already have!")
    else:
        print("Chose a valid option!")
elif chosen_character == Elf:
    if chest_open == "y":
        game_functions.random_item_elf()
        print(Elf().inventory)
    elif chest_open == "n":
        print("You move on with what do you already have!")
    else:
        print("Chose a valid option!")

elif chosen_character == Archer:
    if chest_open == "y":
        game_functions.random_item_archer()
        print(Archer().inventory)
    elif chest_open == "n":
        print("You move on with what do you already have!")

    else:
        print("Chose a valid option!")


# to do
# to create the battle function
    # let the random function decide with who is the player fighting
    # with random and time, do a function in which they hit each other and decrease their life and armour
    # for each character the hit points are different
    # the first who runs out of life, dies
    # print the final message
