from typing import NoReturn
import Chest_system
import Grafik_system
import potion_system

#Startvärden för spelaren
playerWeapon = 100
playerArmor = 100
playerRing = 1
playerLevel = 1




#Välkommst medelande ________________________________________________________________
Grafik_system.welcometext()
int(input("test-->"))

keepgoing = 1
while keepgoing == 1:
    #Kista ______________________________________________________________________________

    #Här finner spelaren en kista som tar fram tre nya möjliga accesory val
    new_weapon, new_armor, new_ring = Chest_system.foundchest(playerWeapon, playerArmor, playerRing, playerLevel)

    #Här displayas nuvarande men även de nya hitttade accesoriesen
    Grafik_system.foundchesttext(new_weapon, new_armor, new_ring, playerWeapon, playerArmor, playerRing)

    #Här väljer spelaren bland de tre nya möjliga valen
    NewAcessoryChoice = int(input("Välj ditt val --->  "))

    #Här tillsätts det nya valet i spelarens inventory
    playerWeapon, playerArmor, playerRing = Chest_system.chestchoice(new_weapon, new_armor, new_ring, playerWeapon, playerArmor, playerRing, NewAcessoryChoice)
    playerLevel += 1


    #Potion _____________________________________________________________________________________

    if potion_system.chance_to_give_potion(playerLevel) == True:
        potiontype = potion_system.give_potion()
        Grafik_system.You_found_a_potion(potiontype)
    else:
        print("hi")
    int(input("test--> "))