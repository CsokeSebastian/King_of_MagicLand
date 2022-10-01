import random


class Enemy:
    def __init__(self, type_of, life, attack):
        self.type_of = type_of
        self.life = life
        self.attack = attack


class Goblin(Enemy):
    def __init__(self):
        super().__init__("Goblin", 80, 20)


class Orc(Enemy):

    def __init__(self):
        super().__init__("Orc", 100, 30)


class Troll(Enemy):

    def __init__(self):
        super().__init__("Troll", 150, 50)



def enemy_sel():

    goblin = Goblin()
    orc = Orc()
    troll = Troll()
    enemy_opt = (goblin, orc, troll)
    enemy = random.choice(enemy_opt)
    print(f"Your enemy is: {enemy.type_of}\nattack: {enemy.attack}\nlife: {enemy.life}")
    return enemy


bad_char = enemy_sel()
