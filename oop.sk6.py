# Private Di OOP Python

class MobileLegend(): #template
   
    def __init__(self, nameHero, powerHero):
        self.nameHero = nameHero
        self.powerHero = powerHero
        # metode private, tidak bisa di wariskan ke kelas lain
        self.__ageHero = "30"

    def getName(self):
        return self.nameHero

    def getPower(self):
        return self.powerHero

    def getRole(self):
        return "Normal"

    # metode private
    def getAge(self):
        return self.__ageHero

class KoreaMobileLegend(MobileLegend):

    # Memanggil Metode Parent Dengan Super
    def __init__(self, nameHero, powerHero):
        # di rekomendasikan
        super().__init__(nameHero, powerHero)
        # kurangdi rekomendasikan
        # MobileLegend.__init__(self, nameHero, powerHero)

        print("Korea Nie Bos")

    def getRole(self):
        return "Initiator"

    def getIseng(self):
        return self.nameHero

class TaiwanMobileLegend(MobileLegend):

    # jika kita tidak menulis code dan menulis (pass) maka secara otomatis akan mengambil yang (parent)
    pass

# di luar class

korea = KoreaMobileLegend("Irine", "89")
taiwan = TaiwanMobileLegend("Zoro", "99")

print(korea.getIseng())

print(korea.getName() + " Role Nya " + korea.getRole())
print(taiwan.getName() + " Role Nya " + taiwan.getRole())

# tidak bisa mengubah nilai yang sudah di tetapkan (vatiable).
MobileLegend.__ageHero = "90"
print(korea.getAge())
