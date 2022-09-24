import winsound
# Text functions


class Messages:

    @staticmethod
    def intro_msg():

        print("Hello dear stranger and welcome in Magicland!\n"
            "Here you begin the journey of a lifetime, fighting\n"
            "the scariest and terrifying creatures and become your\n"
            "own hero!!\n")

    @ staticmethod
    def char_options():
        print("1: Warrior\n2: Wizard\n3: Elf\n4: Archer\n")

    @staticmethod
    def warrior_intro():

        print("My dear warrior, you, with your sword and skills\n"
            "are going to save MagicLand from the evil beasts that\n"
            "will cross your path in this journey!\n")

    @staticmethod
    def wizard_intro():

        print("My dear wizard, you, with your wand and skills\n"
            "are going to save MagicLand from the evil beasts that\n"
            "will cross your path in this journey!\n")

    @staticmethod
    def elf_intro():

        print("My dear elf, you, with your sword and skills\n"
            "are going to save MagicLand from the evil beasts that\n"
            "will cross your path in this journey!\n")

    @staticmethod
    def archer_intro():

        print("My dear archer, you, with your bow and skills\n"
            "are going to save MagicLand from the evil beasts that\n"
            "will cross your path in this journey!\n")

# Sound functions:


class Sounds:

    @staticmethod
    def main_menu_sound():
        winsound.PlaySound('Main_Menu.wav', winsound.SND_LOOP + winsound.SND_ASYNC)
        # winsound.PlaySound(None, winsound.SND_PURGE)

    @staticmethod
    def exploring_sound():
        winsound.PlaySound('Exploring.wav', winsound.SND_LOOP + winsound.SND_ASYNC)
        # winsound.PlaySound(None, winsound.SND_PURGE)

    @staticmethod
    def battle_sound():
        winsound.PlaySound('BattleFinal.wav', winsound.SND_LOOP + winsound.SND_ASYNC)
        # winsound.PlaySound(None, winsound.SND_PURGE)


class PathOptions:

    @staticmethod
    def choose_path():
        print("1: Forest\n2: Town\n3: Dungeon\n")


class PathMessages:

    @staticmethod
    def forest_message():
        print("You have chosen the forest path.\n"
              "On this path your are walking alone thru a dark forest with tall threes and you an old man a chest.\n"
              "He asks you if you want to trade your weapon for what's in the chest, and he tells you that inside \n"
              "it may be a weapon weaker or better than yours.\n")

    @staticmethod
    def town_message():
        print("You have chosen the town path.\n"
              "Your journey begins entering a town with strange people and creatures one of them offers you a chest\n"
              "asks you if you want to trade your weapon for what's in the chest, and he tells you that inside \n"
              "it may be a weapon weaker or better than yours.\n")

    @staticmethod
    def dungeon_message():
        print("You have chosen the dungeon path.\n"
              "You are creeping thru a dungeon and under a ray of light you see a chest. Inside is a weapon,\n"
              "but you don't know if this weapon is better or not than yours, and this chest it can only be\n"
              "open with your currently weapon. If you chose to open the chest you lose your current weapon.\n")
