# Override fungsi parent

class MobileLegend(): #template
   
    def __init__(self, nameHero, powerHero):
        self.nameHero = nameHero
        self.powerHero = powerHero

    def getName(self):
        return self.nameHero

    def getPower(self):
        return self.powerHero

    def getRole(self):
        return "Normal"

class KoreaMobileLegend(MobileLegend):

    def getRole(self):
        return "Initiator"

class ThailandMobileLegend(MobileLegend):

     def getRole(self):
        return "Duelist"

class TaiwanMobileLegend(MobileLegend):

    # jika kita tidak menulis code dan menulis (pass) maka secara otomatis akan mengambil yang (parent)
    pass

# di luar class

korea = KoreaMobileLegend("Miya", "89")
thailand = ThailandMobileLegend("Yuyu", "67")
taiwan = TaiwanMobileLegend("Zoro", "99")

print(korea.getName() + " Role Nya " + korea.getRole())
print(thailand.getName() + " Role Nya " + thailand.getRole())
print(taiwan.getName() + " Role Nya " + taiwan.getRole())



















# pemainKorea = KoreaMobileLegend("Gita", "400")
# pemainThailand = ThailandMobileLegend("Poko", "800")
# print(pemainKorea.getName() + " Role Nya " + pemainKorea.getRole("Duelist"))
# print(pemainThailand.getName() + " Role Nya " + pemainThailand.getRole("Initiator"))
# # object (pemainKorea, pemainThailand) bisa mengambil, getRole()

# pemainML1 = MobileLegend("Zexe", "900")
# print(pemainML1.getName() + " Role Nya " + pemainML1.getPower())
# # object (pemainML1) tidak bisa mengambil, getRole()
