import random
import math


class Player:
    def __init__(self, life, weapon, attack, armour):
        self.life = life
        self.weapon = weapon
        self.attack = attack
        self.armour = armour

    def open_chest(self):
        self.weapon = self.weapon + random.randrange(-30, 30, 5)
        self.armour = self.armour + random.randrange(-30, 30, 5)

    def total_points(self):
        self.life += self.armour
        self.attack += self.weapon


class Warrior(Player):
    def __init__(self, life=100, weapon=50, attack=25, armour=25):
        super().__init__(life, weapon, attack, armour)
        self.type_of_char = "Warrior"
        self.type_of_weapon = "sword"
        self.type_of_armour = "shield"


class Wizard(Player):
    def __init__(self, life=50, weapon=100, attack=25, armour=10):
        super().__init__(life, weapon, attack, armour)
        self.type_of_char = "Wizard"
        self.type_of_weapon = "wand"
        self.type_of_armour = "cape"


class Elf(Player):
    def __init__(self, life=75, weapon=75, attack=25, armour=20):
        super().__init__(life, weapon, attack, armour)
        self.type_of_char = "Elf"
        self.type_of_weapon = "sword"
        self.type_of_armour = "rainbow"


class Archer(Player):
    def __init__(self, life=40, weapon=150, attack=30, armour=10):
        super().__init__(life, weapon, attack, armour)
        self.type_of_char = "Archer"
        self.type_of_weapon = "bow and arrow"
        self.type_of_armour = "shield"
