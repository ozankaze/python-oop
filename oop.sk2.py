class MobileLegend():
    nameHero = "Lala"
    power = "400"

    def getName(self, nameHero):
        self.nameHero = nameHero
        return self.nameHero

    def getPower(self):
        return self.power

print(MobileLegend.nameHero)
print(MobileLegend.power)

hero1 = MobileLegend()

print(hero1.getName("Xsuite"))
print(hero1.getPower())

# === Jika Anda mengakses variabel kelas yang tidak ada, Anda akan mendapatkan pengecualian AttributeError. Misalnya:
# MobileLegend.lolo
# === AttributeError: type object 'HtmlDocument' has no attribute 'lolo'

