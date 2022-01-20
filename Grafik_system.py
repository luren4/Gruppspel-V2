

def welcometext():
    print("\n"*40)

    print("             Welcome to DungeonKeep             ")
    print("________________________________________________")
    print("\n"*15)




def foundchesttext(new_w, new_a, new_r, w, a, r, health, level):

    print("\n"*40)
    print("             Du hittade en kista!                                         ")
    print("________________________________________________            ________________________________________________")
    print(f"Du får välja en av sakerna i den magiska kistan                  Health: {health}            Level: {level}") 
    print("‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾            ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾")
    print("\n\n\n\n")
    




    print("             Välj en av nedanstående                                   Ditt inventory just nu             ")
    print("________________________________________________            ________________________________________________")
    print(f"Val 1  *  nytt vapen med {new_w} damage                         Ditt svärd har nu {w} damage")
    print(f"Val 2  *  ny armor med {new_a} i skydd                          Din rustning har nu {a} i skydd")
    print(f"Val 3  *  ny ring med {new_r} gånger din damage                 Din ring har nu {r} gånger din damage")
    print("‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾            ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾")
    print("\n\n")

def You_found_a_potion(potiontype):
    if potiontype == 1:
        potion = "Healing_potion"
    if potiontype == 2:
        potion = "Damage_potion"
    if potiontype == 3:
        potion = "Attack_again_potion"
    print("\n"*40)

    print("               You Found a potion               ")
    print("________________________________________________")
    print(f"               {potion}                    ")
    print("\n"*14)

def Potion_inventory_show(potionInventory):
    healingPotions, damagePotions, attackAgain = potionInventory.count(1), potionInventory.count(2), potionInventory.count(3)
    print("\nThis is your potion inventory:")
    print(f"You have {healingPotions} healing potions")
    print(f"You have {damagePotions} damage potions")
    print(f"You have {attackAgain} attack again potions")

def Potion_inventory_choice(potionInventory):
    healingPotions, damagePotions, attackAgain = potionInventory.count(1), potionInventory.count(2), potionInventory.count(3)
    print("\n\n\nChoose your potion:")
    print(f"Choice 1 => Healing potion, You have {healingPotions}x")
    print(f"Choice 2 => Damage potion, You have {damagePotions}x")
    print(f"Choice 3 => Attack again potion, You have {attackAgain}x")

def Potion_missing():
    print("You dont have that potion")

def You_used_a_healing_potion(heal, playerhealth):
    print(f"You used a healing potion and regained {heal} health. You therefor now have {playerhealth}")

def You_used_a_damage_potion():
    print("You used a damage potion damaging the enemy 100")


def You_used_an_attack_again_potion():
    print("You used an attack again potion wich lets you attack again")



def Dodged_enemy():
    print("You managed to dodge the monster, damn")

def Found_enemy(monster_attack, monster_health):
    print(f"A monster is approaching you with {monster_attack} damage and {round(monster_health, 2)} health.")

def Dice_roll(attackMultiplier, playerDamage, playerRing):
    print(f"You rolled a {attackMultiplier} meaning your damage will be multiliped {attackMultiplier /10 + 1}x times! This results in {round((attackMultiplier /10 + 1) * playerDamage * playerRing, 2)} damage")

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


