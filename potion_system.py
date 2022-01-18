import random

potionlist = []

def chance_to_give_potion(level):
    chance = random.randint(1, 10) - 0.1 * level
    if chance > 5:
        return True
    else:
        return False

def give_potion():
    PotionType = random.randint(1, 3)
    if PotionType == 1:
        potionlist.append(1)
        return "Healing potion"
    if PotionType == 2:
        potionlist.append(2)
        return "Damage potion"
    if PotionType == 3:
        potionlist.append(3)
        return "Attack again potion"

def use_potion(choice):
    potionlist.remove(choice)
    