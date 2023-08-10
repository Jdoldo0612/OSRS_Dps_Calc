import math

def CalcMaxHit(StrLevel, GearStrBonus, Prayer, CombatStyle, Potion):
    prayerMultiplier = 0
    CombatStyleBonus = 0
    PotionBonus = 0

    if(Prayer.lower() == "burst of strength"):
        prayerMultiplier = 1.05
    elif(Prayer.lower() == "superhuman strength"):
        prayerMultiplier = 1.1
    elif(Prayer.lower() == "ultimate strength"):
        prayerMultiplier = 1.15
    elif(Prayer.lower() == "chivalry"):
        prayerMultiplier = 1.18
    elif(Prayer.lower() == "piety"):
        prayerMultiplier = 1.23

    if(CombatStyle.lower() == "controlled"):
        CombatStyleBonus = 1
    elif(CombatStyle.lower() == "aggressive"):
        CombatStyleBonus = 3

    if(Potion.lower() == "strength"):
        PotionBonus = math.floor(((StrLevel * 0.1) + 2))
    elif(Potion.lower() == "super strength"):
        PotionBonus = math.floor(((StrLevel * 0.15) + 5))
    elif(Potion.lower() == "overload"):
        PotionBonus = 6 + math.floor(StrLevel * 0.16)
    elif(Potion.lower() == "smelling salts"):
        PotionBonus = 11 + math.floor(StrLevel * 0.16)

    effStrLvl = math.floor((StrLevel + PotionBonus) * prayerMultiplier) + CombatStyleBonus + 8

    maxHit = math.floor(((effStrLvl * (64 + GearStrBonus)) + 320) / 640)

    return(maxHit)

print(CalcMaxHit(99,82,"Piety","Controlled","Super Strength"))
