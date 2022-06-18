class Hero(): # template

    def __init__(self, inputName, inputDemage, inputRole):
        # Instance variable
        self.name = inputName
        self.demage = inputDemage
        self.role = inputRole

    # methods tanpa return
    def nameInput(self):
        print("Ini adalah hero valorant " + self.name)
    
    # methods dengan argument
    def nameDemage(self, up):
        self.demage += up
        return self.demage

    # methods dengan return
    def nameRole(self):
        return self.role

valorant1 = Hero("Fade", 3000, "Initiator") #object
valorant2 = Hero("Neon", 5000, "Duelist") #object
valorant3 = Hero("Jett", 8000, "Duelist") #object

print(valorant2.nameInput())
print(valorant3.nameDemage(3000))
print(valorant1.nameRole())