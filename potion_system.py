import random

def chance_to_give_potion(level):
    chance = random.randint(1, 10) - 0.1 * level
    if chance > 5:
        return True
    else:
        return False

def give_potion():
    PotionType = random.randint(1, 3)
    if PotionType == 1:
        return 1
    if PotionType == 2:
        return 2
    if PotionType == 3:
        return 3

# def use_potion(choice):
#     return choice
    