
# wiederholung dictionaries
# Schlüssel-Wert-Paare
eineBekanntePerson = { "firstName": "claudia",
                       "lastName": "van den Boom",
                       "age": "26.1.78",
                       "favoriteNumber": 1818,
                       "favoriteColors": ["green", "yellow", "black"],
                       }

dateOfBirth = eineBekanntePerson["age"]
lst = dateOfBirth.split(".")
dayOfBirth = lst[0]
monthOfBirth = lst[1]
yearOfBirth = lst[2]
# Hausaufgabe Seite 122 6-5 und Seite 123 6-6

print("Hallo " + eineBekanntePerson["firstName"].title())
print("Deine Lieblingszahl ist die " + str(eineBekanntePerson["favoriteNumber"]))
print("Deine Lieblingsfarben sind: " + str(eineBekanntePerson["favoriteColors"]))


for k, v in eineBekanntePerson.items():
    print("Key: " + str(k) + " value: " + str(v))

for k in eineBekanntePerson.keys():
    print(k)

for v in eineBekanntePerson.values():
    print(v)

