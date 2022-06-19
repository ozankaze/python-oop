# Mewariskan kelas inheritance
# Setiap clas bisa mewariskan sifat-sifat ke kelas lain

class MobileLegend(): #template
   
    def __init__(self, nameHero, powerHero):
        self.nameHero = nameHero
        self.powerHero = powerHero

    def getName(self):
        return self.nameHero

    def getPower(self):
        return self.powerHero

class KoreaMobileLegend(MobileLegend):

    def getRole(self, roleHero):
        self.roleHero = roleHero
        return self.roleHero

class ThailandMobileLegend(MobileLegend):

    def getRole(self, roleHero):
        self.roleHero = roleHero
        return self.roleHero

# di luar class

pemainKorea = KoreaMobileLegend("Gita", "400")
pemainThailand = ThailandMobileLegend("Poko", "800")
print(pemainKorea.getName() + " Role Nya " + pemainKorea.getRole("Duelist"))
print(pemainThailand.getName() + " Role Nya " + pemainThailand.getRole("Initiator"))
# object (pemainKorea, pemainThailand) bisa mengambil, getRole()

pemainML1 = MobileLegend("Zexe", "900")
print(pemainML1.getName() + " Role Nya " + pemainML1.getPower())
# object (pemainML1) tidak bisa mengambil, getRole()
