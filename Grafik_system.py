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