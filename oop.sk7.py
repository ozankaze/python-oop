# Staticmethod dan Classmethod

class MobileLegend(): #template
    
    jobPertandingan = "Main PMPL Bos"

    def __init__(self, nameHero):
        self.nameHero = nameHero

    def getName(self):
        return self.nameHero

    # Staticmethod dan Classmethod
    @staticmethod
    def getTahun(age):
        return str(5 - age)

    # classmethod ini hanya bisa mangambil dari staticmethod 
    @classmethod
    def getJob(cls, age):
        return cls.jobPertandingan + " Akan pensiun dalam " + cls.getTahun(age) + " Tahun"

# print staticmethod
# gak usah atau bikin objeck kaya yang (korea dan taiwan) langsung ajah
print("Anda akan ikut turnament " + MobileLegend.getTahun(3) + " Tahun")

# print classmethod
print(MobileLegend.getJob(2))
