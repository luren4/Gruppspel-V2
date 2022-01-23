import random

def foundchest(w, a, r, l):
        
    new_weapon = (w + random.randint(1, 30)) + 2 * l
    new_armour = (a + random.randint(1, 40)) + 2 * l
    new_ring = round((r + 0.03 * random.randint(1, 6) + 0.03 * l), 2)

    return (new_weapon, new_armour, new_ring)


def chestchoice(new_w, new_a, new_r, w, a, r, choice):
    if choice == 1:
        return (new_w, a, r)

    if choice == 2:
        return (w, new_a, r)

    if choice == 3:
        return (w, a, new_r)