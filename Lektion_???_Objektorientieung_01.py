

class Dog():
    """ Ein einfacher Versuch, einen Hund abzubilden."""

    def __init__(self, name, age, color):
        self.name = name          # Eigenschaft
        self.age = age             # Attribut
        self.color = color          # Property

    def sit(self):                  # Methode
        """Simuliere das Sitzen des Hundes."""
        print(self.name + " sitzt.")

    def rollOver(self):             # Methode
        """Simuliere eine Hunderolle."""
        print(self.name + " dreht sich einmal vor Freude.")

    def getCommand(self, command):
        if command == "Sitz":
            print(self.name + " sitzt.")
        elif command == "BeiFuss":
            print(self.name + " kommt zu Dir.")
        else:
            print("Hund versteht Dich nicht.")


myDog = Dog("Rudolf", 2, "braun")           # myDog ist eine Instanz der Klasse Dog
yourDog = Dog("Günther", 7, "schwarz")      # yourDog ist eine Instanz der Klasse Dog

myDog.getCommand("Sitz")
myDog.getCommand("BeiFuss")
myDog.getCommand("Hol mir die Zeitung")

x = myDog.age
print("################   " + str(x))

myDog.rollOver()
myDog.sit()
yourDog.rollOver()
yourDog.sit()
# Übung: ergänze die Klasse Hund um zwei Attribute und um zwei Methoden.
# Eine Klasse ausdenken mit 5 Attributen (Eigenschaften) und zwei Methoden.