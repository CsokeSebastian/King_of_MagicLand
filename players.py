
class Player:
    def __init__(self, type_of, life, power, attack):
        self.name = type_of
        self.life = life
        self.power = power
        self.inventory = []
        self.attack = attack


class Warrior(Player):
    def __init__(self):
        super().__init__("Warrior", 100, 50, 25)


class Wizard(Player):
    def __init__(self):
        super().__init__("Wizard", 50, 100, 25)


class Elf(Player):
    def __init__(self):
        super().__init__("Elf", 75, 75, 25)


class Archer(Player):
    def __init__(self):
        super().__init__("Archer", 40, 150, 30)
