import math

class meleeDPS:
    AtkLvl = 0
    StrLvl = 0
    Prayer = ""
    CombatStyle = ""
    StrPotion = ""
    AtkPotion = ""
    GearStrBonus = 0
    GearAtkBonus = 0
    TargetDefLvl = 0
    TargetStyleDef = 0
    WepSpeed_Ticks = 0
    UsingSalve = False
    UsingVoid = False
    UsingSlayHelm = False

    def CalcMaxHit(self):
        prayerMultiplier = 0
        CombatStyleBonus = 0
        PotionBonus = 0

        if(self.Prayer.lower() == "burst of strength"):
            prayerMultiplier = 1.05
        elif(self.Prayer.lower() == "superhuman strength"):
            prayerMultiplier = 1.1
        elif(self.Prayer.lower() == "ultimate strength"):
            prayerMultiplier = 1.15
        elif(self.Prayer.lower() == "chivalry"):
            prayerMultiplier = 1.18
        elif(self.Prayer.lower() == "piety"):
            prayerMultiplier = 1.23

        if(self.CombatStyle.lower() == "controlled"):
            CombatStyleBonus = 1
        elif(self.CombatStyle.lower() == "aggressive"):
            CombatStyleBonus = 3

        if(self.StrPotion.lower() == "strength"):
            PotionBonus = math.floor(((self.StrLvl * 0.1) + 2))
        elif(self.StrPotion.lower() == "super strength"):
            PotionBonus = math.floor(((self.StrLvl * 0.15) + 5))
        elif(self.StrPotion.lower() == "overload"):
            PotionBonus = 6 + math.floor(self.StrLvl * 0.16)
        elif(self.StrPotion.lower() == "smelling salts"):
            PotionBonus = 11 + math.floor(self.StrLvl * 0.16)

        effStrLvl = math.floor((self.StrLvl + PotionBonus) * prayerMultiplier) + CombatStyleBonus + 8

        if(self.UsingVoid == True):
            effStrLvl = effStrLvl * 1.1

        maxHit = math.floor(((effStrLvl * (64 + self.GearStrBonus)) + 320) / 640)

        if(self.UsingSalve == True):
            maxHit = math.floor(maxHit * 1.2)
        elif(self.UsingSlayHelm == True):
            maxHit = math.floor(maxHit * 1.1667)

        return(maxHit)

    def CalcEffAttkLvl(self):
        prayerMultiplier = 0
        CombatStyleBonus = 0
        PotionBonus = 0

        if (self.Prayer.lower() == "clarity of thought"):
            prayerMultiplier = 1.05
        elif (self.Prayer.lower() == "improved reflexes"):
            prayerMultiplier = 1.1
        elif (self.Prayer.lower() == "incredible reflexes"):
            prayerMultiplier = 1.15
        elif (self.Prayer.lower() == "chivalry"):
            prayerMultiplier = 1.15
        elif (self.Prayer.lower() == "piety"):
            prayerMultiplier = 1.20

        if (self.CombatStyle.lower() == "controlled"):
            CombatStyleBonus = 1
        elif (self.CombatStyle.lower() == "accurate"):
            CombatStyleBonus = 3

        if (self.AtkPotion.lower() == "attack"):
            PotionBonus = math.floor(((self.AtkLvl * 0.1) + 2))
        elif (self.AtkPotion.lower() == "super attack"):
            PotionBonus = math.floor(((self.AtkLvl * 0.15) + 5))
        elif (self.AtkPotion.lower() == "overload"):
            PotionBonus = 6 + math.floor(self.AtkLvl * 0.16)
        elif (self.AtkPotion.lower() == "smelling salts"):
            PotionBonus = 11 + math.floor(self.AtkLvl * 0.16)

        tempAtkLvl = math.floor((self.AtkLvl + PotionBonus) * prayerMultiplier)
        effAtkLvl = math.floor(tempAtkLvl + CombatStyleBonus + 8)

        if(self.UsingVoid == True):
            effAtkLvl = effAtkLvl * 1.1

        return(effAtkLvl)

    def CalcAtkRoll(self):
        temp = self.CalcEffAttkLvl() * (self.GearAtkBonus + 64)
        if(self.UsingSalve == True):
            temp = temp * 1.2
        elif(self.UsingSlayHelm == True):
            temp = temp * 1.1667

        return(math.floor(temp))

    def CalcTargetDefRoll(self):
        return((self.TargetDefLvl + 9) * (self.TargetStyleDef + 64))

    def CalcHitChance(self):
        atkRoll = self.CalcAtkRoll()
        defRoll = self.CalcTargetDefRoll()
        if(atkRoll > defRoll):
            HitChance = 1 - ((defRoll + 2) / (2 * (atkRoll + 1)))
        else:
            HitChance = atkRoll / (2 * (defRoll + 1))

        return(HitChance)

    def CalcDmgOutput(self):
        dmgOutput = (self.CalcMaxHit() * self.CalcHitChance()) / 2
        return(dmgOutput)

    def CalcDPS(self):
        return(self.CalcDmgOutput() / (self.WepSpeed_Ticks * 0.6))

myMeleeClass = meleeDPS()
myMeleeClass.StrLvl = 99
myMeleeClass.Prayer = "Piety"
myMeleeClass.StrPotion = "Super Strength"
myMeleeClass.GearStrBonus = 82
myMeleeClass.CombatStyle = "Controlled"
myMeleeClass.AtkLvl = 99
myMeleeClass.AtkPotion = "Super Attack"
myMeleeClass.GearAtkBonus = 100
myMeleeClass.TargetStyleDef = 100
myMeleeClass.TargetDefLvl = 0
myMeleeClass.WepSpeed_Ticks = 4
myMeleeClass.UsingSalve = False
myMeleeClass.UsingVoid = False
myMeleeClass.UsingSlayHelm = False

print(meleeDPS.CalcMaxHit(myMeleeClass))
print(meleeDPS.CalcEffAttkLvl(myMeleeClass))
print(meleeDPS.CalcAtkRoll(myMeleeClass))
print(meleeDPS.CalcHitChance(myMeleeClass))
print(myMeleeClass.CalcDPS())