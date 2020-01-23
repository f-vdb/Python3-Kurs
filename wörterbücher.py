# Wörterbücher - Dictionary

alien_0 = {  "color": "green",
             "points": 5  }

print(alien_0["color"])
print(alien_0["points"])

unserBuch = { "Haus": "houser",
              "Schule": "school",
              "Baum": "tree"
              }

meinFussballVerein = { "Name":          "Bayern München",
                       "Stadion":       "Allianz Arena",
                       "Punkte":        24,
                       "Tordifferenz":  17,
                       "Farben": ["blau", "weiss", "rot"]}

print(meinFussballVerein["Farben"])
farben = meinFussballVerein["Farben"]
for farbe in farben:
    print(farbe)


myWife = { "first_name": "claudia",
           "last_name": "van den Boom",
           "age": "26.01.1978",
           "city": "odenthal"}

age = myWife["age"]
lst = age.split(".")
for i in lst:
    print(i)

print(myWife["first_name"])
print(myWife["last_name"])
print(myWife["age"])
print(myWife["city"])

# 6-2
personNumbers = { "david": 16,
                  "jan": 203,
                  "artur": 420,
                  "miles": 23,
                  "frank": 23 }

print(personNumbers["david"])

print("Lieblingszahl von David: " + str(personNumbers["david"]))

for key, value in personNumbers.items():
    print("Schlüssel: " + key + " Wert: " + str(value))

# 6-3
glossar = { "Listen": "Werte in einer Liste/Feld gespeichert.",
            "Dictionary": "Schlüssel-Wert-Paare",
            "Schleife": "for in Schleife"}
for begriff, beschreibung in glossar.items():
    print(begriff + ": " + beschreibung)

## Dictionaries in einer Schleife durchlaufen

# Alle Schlüssel-Wert Paare durchlaufen
# Alle Schlüssel in einem Dictionary durchlaufen
# Die Schlüssel in einem Dictionary geordnet durchlaufen
# Alle Werte in einem Dicrtionary durchlaufen

## Verschachtelung
# Dictinaries in einer Liste
# Listen in einem Dictionary
# Dictionary in einem Dictionary


