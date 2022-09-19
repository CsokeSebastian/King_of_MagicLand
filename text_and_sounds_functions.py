import winsound


class IntroMessages:

    @staticmethod
    def intro_msg():

        print("Hello dear stranger and welcome in Magicland!\n"
                "Here you begin the journey of a lifetime, fighting\n"
                "the scariest and terrifying creatures and become your\n"
                "own hero!!\n")

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

    @staticmethod
    def exploring_sound():
        winsound.PlaySound('Exploring.wav', winsound.SND_LOOP + winsound.SND_ASYNC)

    @staticmethod
    def battle_sound():
        winsound.PlaySound('BattleFinal.wav', winsound.SND_LOOP + winsound.SND_ASYNC)
