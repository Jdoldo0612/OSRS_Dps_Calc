import math

# Constants
Pray_BurstOfStr = 1.05
Pray_SupHumStr = 1.1
Pray_UltStr = 1.15
Pray_Chiv = 1.18
Pray_Piety = 1.23


# Defining functions for the potions as they are str level dependent
def Pot_Str(strLvl):
    return (math.floor(((strLvl * 0.1) + 2)))


def Pot_SupStr(strLvl):
    return (math.floor(((strLvl * 0.15) + 5)))


# Melee
pietyBoost = 1.23
combatStyle = 1  # 1 if controlled, 3 if aggressive

# verifying can match calcs, then move to interface after
StrengthLevel = 99

EffStrLvl = math.floor((StrengthLevel + Pot_SupStr(StrengthLevel)) * pietyBoost) + combatStyle + 8

# Naked with whip rn for calc purposes
GearStrBonus = 82

MaxHit = math.floor(((EffStrLvl * (64 + GearStrBonus)) + 320) / 640)

print(MaxHit)
