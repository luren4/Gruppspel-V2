import random

def found_enemy(level):
    enemy_attack = 50 + random.randint(20, 50) * level
    enemy_health = 100 + random.randint(40, 80) * level
    return (enemy_attack, enemy_health)

def Roll_dice():
    return random.randint(1, 6)

def Damage_enemy(playerDamage, damageMultiplier, playerRing):
    return playerDamage * playerRing * (damageMultiplier / 10 + 1)

def Damage_player(enemyAttack, playerArmor, playerHealth):
    return playerHealth + playerArmor - enemyAttack