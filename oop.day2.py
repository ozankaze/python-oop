class Hero(): # template

    # init ini akan di eksekusi ketika pertama kali si object itu di buat
    # self -> ini adalah si (valorant1) = sama saja
    def __init__(self, inputName, inputDemage, inputRole):
        self.name = inputName
        self.demage = inputDemage
        self.role = inputRole
        # print("Hello", angka)
        # ==== init akan di letakan dan di eksekusi. objeck ini di buat


valorant1 = Hero("Fade", 3000, "Initiator") #object
valorant2 = Hero("Neon", 5000, "Duelist") #object
valorant3 = Hero("Jett", 8000, "Duelist") #object

# print(valorant2.demage)
# print(valorant3.name)
print(valorant1.__dict__)
print(valorant2.__dict__)
print(valorant3.__dict__)
