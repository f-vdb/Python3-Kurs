
# Seite 41 Listen
bicycles = ["trek", "cannondale", "redline", "specialized"]

print(bicycles[0])
print(bicycles[3])
# trick das letzte Element einer Liste anzusprechen
print(bicycles[-1])
print(bicycles[len(bicycles)-1])
# das vorletzte Element einer Liste ausgeben
print(bicycles[-2])
# ersten Buchstaben groß schreiben
print(bicycles[1].title())

motorcycles = ["honda", "yamaha", "ducati"]
# Element in der Liste ändern
motorcycles[0] = "bmw"
print(motorcycles)

# Element an das Ende der Liste hängen
motorcycles.append("ktm")
print(motorcycles)

# Anlegen einer leeren Liste
footballClubs = []
footballClubs.append("1. FC")
footballClubs.append("Leverkusen")
footballClubs.append("Dormtund")
footballClubs.append("Schalke")
print(footballClubs)
# Element in eine Liste einfügen
footballClubs.insert(1, "Freiburg")
print(footballClubs)
footballClubs.insert(0, "Bayern")
print(footballClubs)

# Elemente aus einer Liste entfernen
del footballClubs[0]
print(footballClubs)
del footballClubs[3]
print(footballClubs)

# manchmal möchte man den Wert den man aus der Liste
# entfernt hat, noch benutzen....
lastClub = footballClubs.pop()
print(lastClub)
print(footballClubs)
lastClub = footballClubs.pop(1)
print(lastClub)
print(footballClubs)

# Element anhand des Wertes entfernen
footballClubs.remove("Leverkusen")
print(footballClubs)
footballClubs.append("Leverkusen")
footballClubs.append("Leverkusen")
print(footballClubs)
footballClubs.remove("Leverkusen")
print(footballClubs)

for club in footballClubs:
    print("Hallo " + club + " toll.")

# Hausaufgaben Seite 50 und 51 alle Aufgaben










