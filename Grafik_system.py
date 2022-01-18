from zlib import DEF_BUF_SIZE


def welcometext():
    print("\n"*40)

    print("             Welcome to DungeonKeep             ")
    print("________________________________________________")
    print("\n"*15)





def foundchesttext(new_w, new_a, new_r, w, a, r):

    print("\n"*40)
    print("             Du hittade en kista!             ")
    print("________________________________________________")
    print(f"Du får välja en av sakerna i den magiska kistan")
    print("‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾")
    print("\n\n\n\n")
    




    print("             Välj en av nedanstående                                   Ditt inventory just nu             ")
    print("________________________________________________            ________________________________________________")
    print(f"Val 1  *  nytt vapen med {new_w} damage                         Ditt svärd har nu {w} damage")
    print(f"Val 2  *  ny armor med {new_a} i skydd                          Din rustning har nu {a} i skydd")
    print(f"Val 3  *  ny ring med {new_r} gånger din damage                 Din ring har nu {r} gånger din damage")
    print("‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾            ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾")
    print("\n\n")

def You_found_a_potion(potiontype):
    print("\n"*40)

    print("               You Found a potion               ")
    print("________________________________________________")
    print(f"               {potiontype}                    ")
    print("\n"*14)

def Dodged_enemy():
    print("You managed to dodge the monster, damn")

def Found_enemy(monster_attack, monster_health):
    print(f"A monster is approaching you with {monster_attack} damage and {monster_health} health.")

def Dice_roll(attackMultiplier, playerDamage, playerRing):
    print(f"You rolled a {attackMultiplier} meaning your damage will be multiliped {attackMultiplier /10 + 1}x times! This results in {(attackMultiplier /10 + 1) * playerDamage * playerRing} damage")

def Enemy_struck():
    print("You struck the enemy!")

def Killed_enemy():
    print("You killed the enemy")

def Enemy_Survived(remainingEnemyHealth):
    print(f"The enemy survived your attack and has {remainingEnemyHealth} health left")


def Enemy_didnt_pierce_armor(enemyAttack, playerArmor):
    print(f"The enemy hit you with {enemyAttack} damage but didnt pierce your armor that is {playerArmor}")


def Player_lost_health(remaining_health):
    print(f"The enemy hit you hard but you survived. It pierced your armor and left you with {remaining_health} health")

def Player_died():
    print("You died")


