# Metode Init ( __init__ )
# Instance atribut Adalah fungsi yang akan otomatis di jalankan, 
# atau kan di eksekusi ketika pertama kali si object itu di buat.

class MobileLegend(): # template
    
    nameHero = " "
    powerHero = " "

    def __init__(self, nameHero, powerHero):
        # Instance variable
        self.nameHero = nameHero
        self.powerHero = powerHero

    def getName(self):
        return self.nameHero

    def getPower(self):
        return self.powerHero
    
player1 = MobileLegend("Axe", "900") #object
player2 = MobileLegend("Miya", "650") #object
player3 = MobileLegend("Lord", "480") #object

print(player1.getName() + " Powernya " + player1.getPower())
print(player2.getName() + " Powernya " + player2.getPower())
print(player3.getName() + " Powernya " + player3.getPower())
