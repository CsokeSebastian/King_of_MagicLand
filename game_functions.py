import random

better_warrior_chest_items = {"steel sword": 15,
                              "steel shield": 25},
worse_warrior_chest_items = {"knife": 5,
                             "helmet": 15}
better_wizard_chest_items = {"better wooden stick": 25,
                             "long lasting shield": 15}
worse_wizard_chest_items = {"worse wooden stick": 15,
                            "smaller shield": 5}
better_elf_chest_items = {"steel sword": 15,
                          "better shield": 25}
worse_elf_chest_items = {"knife": 5,
                         "smaller shield": 15}
better_archer_chest_items = {"better bow and arrows": 25,
                             "better shield": 15}
worse_archer_chest_items = {"sling": 15,
                            "feather shield": 5}
new_warrior_items = [better_warrior_chest_items, worse_warrior_chest_items]
new_wizard_items = [better_wizard_chest_items, worse_wizard_chest_items]
new_elf_items = [better_elf_chest_items, worse_elf_chest_items]
new_archer_items = [better_archer_chest_items, worse_archer_chest_items]


def random_items_warrior():
    new_items = random.choice(new_warrior_items)
    return new_items


def random_items_wizard():
    new_items = random.choice(new_wizard_items)
    return new_items


def random_item_elf():
    new_items = random.choice(new_elf_items)
    return new_items


def random_item_archer():
    new_items = random.choice(new_archer_items)
    return new_items
