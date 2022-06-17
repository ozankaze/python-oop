class Hero(): # template
    # class variable
    jumlah = 0

    def __init__(self, inputName, inputDemage, inputRole):
        # Instance variable
        self.name = inputName
        self.demage = inputDemage
        self.role = inputRole
        Hero.jumlah += 1
        print("Hello " + inputName)

valorant1 = Hero("Fade", 3000, "Initiator") #object
print(Hero.jumlah)
valorant2 = Hero("Neon", 5000, "Duelist") #object
print(Hero.jumlah)
valorant3 = Hero("Jett", 8000, "Duelist") #object
print(Hero.jumlah)

class MobileLegend():
    # nameHero = "Miya"
    nameHero = " "
    powerHero = " "

    def getName(self, nameHero, powerHero):
        self.nameHero = nameHero
        self.powerHero = powerHero
        return self.nameHero, self.powerHero

# di luar class

mobillegend1 = MobileLegend()
mobillegend2 = MobileLegend()
# print(mobillegend1.nameHero) #cara pertama
print(mobillegend1.getName("Miya", "300"))
print(mobillegend2.getName("Nana", "800"))