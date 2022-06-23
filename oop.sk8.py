# Staticmethod dan Classmethod

class MobileLegend(): #template

    def __init__(self, nameHero, powerHero):
        self.nameHero = nameHero
        self.powerHero = powerHero

    @property
    def infoHero(self):
        return self.nameHero + " powernya adalah " + self.powerHero

    @infoHero.setter
    def infoHero(self, data):
        nameHero, powerHero = data.split(" ")
        self.nameHero = nameHero
        self.powerHero = powerHero
    
korea = MobileLegend("Miya", "300")
korea.infoHero = 'Wekobo 25'
print(korea.infoHero)

