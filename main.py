from text_functions import IntroMessages
from playsound import playsound



def play_main_menu_sound():
    playsound('Main_Menu.wav', False)


def if_want_to_play():

    max_try = 5
    counter = 0
    for answer in range(1, max_try):
        answer = input("Do you want to begin your adventure?\n").lower()
        if answer == "yes":
            print("Alright then, let's begin!")
            break
            # start_game()
        elif answer == "no":
            print("Then come back when you have the balls!")
            break
            # exit_game()
        else:
            counter += 1
            if counter < 3:
                print("Enter 'yes/no'!")
            elif counter == 3:
                print("Last chance to chose an option, otherwise I will exit!")
            elif counter == 4:
                print("Told you!")
                # exit_game()


play_main_menu_sound()
IntroMessages.intro_msg()
if_want_to_play()
