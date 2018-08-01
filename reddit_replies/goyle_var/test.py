import random
player_num=random.randint(1,20)+player_init
goyle_num=random.randint(1,20)
#attack sequence
def PlayerTurn_vs_Goyle():
    goyle_ac=13
    player_str_mod=2
    player_dex_mod=2
    goyle_turn=0
    player_turn=0
    player_attacknum=0
    goyle_attacknum=0
    goyle_resistancies=["slashing"]
    if player_num>goyle_num or player_num==goyle_num:
        action = input("What will ye do now?\n").lower()
        if action == "attack" or action == "fight" or action == "hit":
            weapon = input("What will ye attack with?\n").lower()
            if weapon == "longsword":
                longsword_damtype="slashing"
                if "longsword" in player_weapons:
                    attack_roll = random.randint(1,20)+player_str_mod
                    if attack_roll>=goyle_ac:
                        if longsword_damtype in goyle_resistancies:
                            goyle_hp = goyle_hp - random.randint(1,8)/2
                            print("Ye hit Goyle! Goyle has %d HP left!" % (goyle_hp))
                            if goyle_hp<=0:
                                print("Goyle is dead!")
                            else:
                                goyle_turn=goyle_turn+1
                                if goyle_turn>player_turn:
                                    result = GoyleTurn()
                        else:
                            goyle_hp = goyle_hp - random.randint(1,8)
                            print("Ye hit Goyle! Goyle has %d HP left!" % (goyle_hp))
                            if goyle_hp<=0:
                                print("Goyle is dead!")
                            else:
                                goyle_turn=goyle_turn+1
                                if goyle_turn>player_turn:
                                    result = GoyleTurn()
                    elif attack_roll<goyle_ac:
                        print("Ye missed!")
                        goyle_turn=goyle_turn+1
                        if goyle_turn>player_turn:
                            result = GoyleTurn()
                else:
                    print("Ye don't have a %s!" % (weapon))
            elif weapon == "hand crossbow".lower() or weapon == "crossbow".lower():
                hand_xbow_damtype="piercing"
                if "hand_crossbow" in player_weapons:
                    attack_roll = random.randint(1,20)+player_dex_mod
                    if attack_roll>=goyle_ac:
                        if hand_xbow_damtype in goyle_resistancies:
                            goyle_hp = goyle_hp - random.randint(1,6)/2
                            print("Ye hit Goyle with yer crossbow! Good shot! Goyle has %d HP left!" % (goyle_hp))
                            if goyle_hp<=0:
                                print("Goyle is dead!")
                            else:
                                goyle_turn=goyle_turn+1
                                if goyle_turn>player_turn:
                                    result = GoyleTurn()
                        else:
                            goyle_hp = goyle_hp - random.randint(1,6)
                            print("Ye hit Goyle with yer crossbow! Good shot! Goyle has %d HP left!" % (goyle_hp))
                            if goyle_hp<=0:
                                print("Goyle is dead!")
                            else:
                                goyle_turn=goyle_turn+1
                                if goyle_turn>player_turn:
                                    result = GoyleTurn()
                    elif attack_roll<goyle_ac:
                        print("Ye missed!")
                        player_attacknum=player_attacknum+1
                        if player_attacknum>goyle_attacknum:
                            GoyleTurn()
                else:
                    print("Well that's not a weapon that's available to you, sonny!")
                    PlayerTurn_vs_Goyle()
        elif action == "Run".lower() or action == "Run away".lower():
            chance = random.randint(1,20)
            if chance > 10:
                print("Ye got away safely!")
                #PathChoice
            else:
                print("Goyle followed ye! Ye wasted yer turn running!")
                player_attacknum=player_attacknum+1
                if player_attacknum>goyle_attacknum:
                    GoyleTurn
        elif action == "talk" or action == "reason":
            print("Ye can't speak to Goyle! While you were busy talking, Goyle took his turn!")
            goyle_turn=goyle_turn+1
            if goyle_turn>player_turn:
                result = GoyleTurn()
        else:
            print("That isn't something ye can do now ya see")
            goyle_turn=goyle_turn+1
            if goyle_turn>player_turn:
                result = PlayerTurn_vs_Goyle()
            
def GoyleTurn():
    goyle_attacknum=0
    player_attacknum=0
    goyle_turn_attack = random.randint(1,3)
    if goyle_turn_attack == 1:
        result=MultiAttack()
        goyle_attacknum=goyle_attacknum+1
        if goyle_attacknum >= player_attacknum:
            PlayerTurn_vs_Goyle()
    if goyle_turn_attack == 2:
        result=Bite()
        goyle_attacknum=goyle_attacknum+1
        if goyle_attacknum >= player_attacknum:
            PlayerTurn_vs_Goyle()
    if goyle_turn_attack == 3:
        result=Claws()
        goyle_attacknum=goyle_attacknum+1
        if goyle_attacknum >= player_attacknum:
            PlayerTurn_vs_Goyle()
#MultiAttack
def MultiAttack():
    try:
        player_turn=0
        goyle_turn=0
        player_hp=int(input("How much HP do ye have remaining?\n"))
        player_ac = 11
        player_resistancies = "Piercing"
        goyle_attack_hits_multi = "Goyle hits ye with MultiAttack!"
        goyle_attack_miss = "Goyle's attack misses!"
        goyle_attack = random.randint(1,20)
        if goyle_attack + 2>player_ac:
            if "piercing" in player_resistancies and "slashing" in player_resistancies:
                damage=((random.randint(1,6)+2))/2+((random.randint(1,6)+2)/2)
                player_hp=player_hp-damage
                print(goyle_attack_hits_multi, "You have", player_hp, "HP left")
                goyle_turn=goyle_turn+1
                if goyle_turn>player_turn:
                    PlayerTurn_vs_Goyle()
            elif "piercing" in player_resistancies or "slashing" in player_resistancies:
                damage=((random.randint(1,6)+2))/2+(random.randint(1,6)+2)
                player_hp=player_hp-damage
                print(goyle_attack_hits_multi, "You have", player_hp, "HP left")
                goyle_turn=goyle_turn+1
                if goyle_turn>player_turn:
                    PlayerTurn_vs_Goyle()
            else:
                damage=(random.randint(1,6)+2)+(random.randint(1,6)+2)
                player_hp=player_hp-damage
                print(goyle_attack_hits_multi, "You have", player_hp, "HP left")
                goyle_turn=goyle_turn+1
                if goyle_turn>player_turn:
                    PlayerTurn_vs_Goyle()
        elif goyle_attack + 2<=player_ac:
            damage = 0
            print(goyle_attack_miss)
            goyle_turn=goyle_turn+1
            if goyle_turn>player_turn:
                PlayerTurn_vs_Goyle()
    except ValueError:
        print("Well that's not a valid option, me friend!")
        GoyleTurn()
        
#bite                  
def Bite():
    try:
        player_hp=int(input("How much HP do ye have remaining?\n"))
        player_ac = 11
        player_resistancies = "Piercing"
        goyle_attack_hits_bite = "Goyle hits with Bite!"
        goyle_attack_miss = "Goyle's attack misses!"
        goyle_attack = random.randint(1,20)
        goyle_turn=0
        player_turn=0
        if goyle_attack + 2>player_ac:
            if "piercing" in player_resistancies:
                damage=((random.randint(1,6)+2))/2
                player_hp=player_hp-damage
                print(goyle_attack_hits_bite, "You have", player_hp, "HP left")
                goyle_turn=goyle_turn+1
                if goyle_turn>player_turn:
                    PlayerTurn_vs_Goyle()
            else:
                damage=(random.randint(1,6)+2)
                player_hp=player_hp-damage
                print(goyle_attack_hits_bite, "You have", player_hp, "HP left")
                goyle_turn=goyle_turn+1
                if goyle_turn>player_turn:
                    PlayerTurn_vs_Goyle()
        elif goyle_attack + 2<=player_ac:
            damage = 0
            print(goyle_attack_miss)
            goyle_turn=goyle_turn+1
            if goyle_turn>player_turn:
                PlayerTurn_vs_Goyle()
    except ValueError:
        print("Well that's not a valid option, me friend!")
        GoyleTurn()
        
#claws
def Claws():
    try:
        player_hp=int(input("How much HP do ye have remaining?\n"))
        player_ac = 11
        player_resistancies = "Piercing"
        goyle_attack_hits_claws = "Goyle hits with Claws!"
        goyle_attack_miss = "Goyle's attack misses!"
        goyle_attack = random.randint(1,20)
        goyle_turn=0
        player_turn=0
        if goyle_attack + 2>player_ac:
            if "slashing" in player_resistancies:
                damage=((random.randint(1,6)+2))/2
                player_hp=player_hp-damage
                print(goyle_attack_hits_claws, "You have", player_hp, "HP left")
                goyle_turn=goyle_turn+1
                if goyle_turn>player_turn:
                    PlayerTurn_vs_Goyle()
            else:
                damage=(random.randint(1,6)+2)
                player_hp=player_hp-damage
                print(goyle_attack_hits_claws, "You have", player_hp, "HP left")
                goyle_turn=goyle_turn+1
                if goyle_turn>player_turn:
                    PlayerTurn_vs_Goyle()
        elif goyle_attack + 2<=player_ac:
            damage = 0
            print(goyle_attack_miss)
            goyle_turn=goyle_turn+1
            if goyle_turn>player_turn:
                PlayerTurn_vs_Goyle()
    except ValueError:
        print("Well that's not a valid option, me friend!")
        GoyleTurn()
print("There is a gargoyle. It bares its teeth at ye and growls. It doesn't seem to be speaking any language ye recognize until it says three sentences, which seem to be very rehearsed: 'My name is Goyle, the defender of the lost realm. The treasure you seek beyond this path carries dangers beyond your reckoning. If you wish to proceed, then prepare to die!'.")

if player_num>goyle_num:    
    result=PlayerTurn_vs_Goyle()
if player_num==goyle_num:
    result=PlayerTurn_vs_Goyle()
if goyle_num>player_num:
    result=GoyleTurn()
