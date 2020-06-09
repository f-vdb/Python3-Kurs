'''
Inhalte Arbeit:
- Werte einlesen mit try except block
- if - Verzweigungen
- for - Schleifen (for in ....)
for i in lst:
for i in range(10):
- list - anhängen, sortieren, löschen, ist etwas in einer Liste
- dict - keys zugreifen - values zugreifen und auf beide zugreifen
- files - lesen und schreiben


Übungsprogramm:
- wie viele Namen möchtest Du eingeben?
- dann fragt das Programm die Namen und das Alter ab
- Name und Alter in einem dict speichern
(Name ist der Key; Alter ist der Value)
- die Namen und Alter in einer Datei speichern
Frank:26
Sabine:24
Tom:18
- Datei lesen
- und die gelesen Namen und Alter in ein neues dict speichern
- Werte aus dem neuen dict schön ausgeben



'''















alterNamen = {44: "Frank",
              28: "Jan",
              44: "Toll"}

for i in alterNamen.keys():
    print(i)

namenAlter = {"Frank": 44,
              "Jan": 38,
              "Peter": 16,
              "Timmy": 12}

for name, alter in namenAlter.items():
    print("Hallo " + name)
    if alter < 14:
        print("Du junger Mensch " + str(alter) + " Jahr alt.")
    elif alter > 14 and alter < 40:
        print("mmhh")
    else:
        print("oho....")

for name in namenAlter.keys():
    print(name)

for alter in namenAlter.values():
    print(alter)

print(sorted(namenAlter.values()))





primeNumber = "1,3,5,7,11,17,19,23"


with open("primeNumberString.txt", "w") as fd:
    fd.write(primeNumber)

with open("primeNumberString.txt", "r") as toll:
    numbersAsString = toll.read()

print(numbersAsString)

numbers = numbersAsString.split(",")

for number in numbers:
    print(number)

primeNumbers = [1,3,5,7,11,13,17,19,23]

with open("primeNumbersList.txt", "w") as fd:
    for primeNumber in primeNumbers:
        fd.write(str(primeNumber)+"\n")

with open("primeNumbersList.txt", "r") as fd:
    tmp = fd.read()

print(type(tmp))
print(tmp)

with open("primeNumbersList.txt", "r") as fd:
    lst = fd.readlines()

print(lst)
for i in lst:
    print(i)

for i in lst:
    print(i[0:-1])
