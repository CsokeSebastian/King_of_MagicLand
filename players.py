
class Player:
    def __init__(self, type_of, life, power, attack):
        self.name = type_of
        self.life = life
        self.power = power
        self.attack = attack


class Warrior(Player):
    def __init__(self):
        super().__init__("Warrior", 100, 50, 25)
        self.inventory = {"Wooden axe": 10,
                          "Wooden shield": 20}


class Wizard(Player):
    def __init__(self):
        super().__init__("Wizard", 50, 100, 25)
        self.inventory = {"Wooden stick": 20,
                          "Short lasting shield": 10}


class Elf(Player):
    def __init__(self):
        super().__init__("Elf", 75, 75, 25)
        self.inventory = {"Wooden sword": 10,
                          "Magic shield": 20}


class Archer(Player):
    def __init__(self):
        super().__init__("Archer", 40, 150, 30)
        self.inventory = {"Wooden bow": 20,
                          "Wooden shield": 10}
