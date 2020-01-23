'''
Inhalte der Arbeit:
- Werte einlesen mit try except block
- if-Verzweigungen
- for-Schleifen (for in ....)
    for i in lst:
    for i in range(10):
- Listen: anhängen, sortieren, löschen, ist etwas in einer Liste
- Wörterbücher: auf die Schlüssel zugreifen
                auf die Werte zugreifen
                auf Schlüssel und Werte zugreifen
- Dateien:  lesen
            schreiben

Übungsprogramm:
- wie viele Namen möchtest Du eingeben?
- dann fragt das Programm die Namen und das Alter ab
- Name und Alter in einem Wörterbuch speichern
Name ist der Schlüssel(Key) Alter ist der Wert(Value)
- Namen und Alter in eine Datei speichern
Frank:26
Sabine:24
Tom:18
- Datei lesen
- und die gelesen Namen und Alter in ein neues Wörterbuch speichern
- Werte aus dem neuen dict schön ausgeben
'''

while True:
    try:
        print("Wie viele Namen wollen Sie eingeben.")
        count = int(input("Bitte geben Sie als Anzahl eine ganze Zahl ein: "))
        break
    except:
        print("Das war keine ganze Zahl.")

#print(count)

namesAndAges = {}  # leeres Dictinary anlegen

for i in range(count):
    name = input("Bitte geben Sie den " + (str(i + 1)) + " Namen ein: ")
    age = input("Bitte geben Sie das Alter von " + name + " ein: ")
    #print(name, age)
    namesAndAges[name] = age

for name, age in namesAndAges.items():
    print(name + " ist " + age + " Jahre alt.")

with open("nameAndAges.txt", "w") as fd:
    for name, age in namesAndAges.items():
        fd.write(name + ":" + age + "\n")


with open("nameAndAges.txt", "r") as fd:
    namesAndAgesLst = fd.readlines()

newDict = {}

for i in namesAndAgesLst:
    i = i[0:-1] # newline Zeichen \n am Ende der Zeile löschen
    lst = i.split(":")
    name = lst[0]
    age = lst[1]
    #print(name, age)
    newDict[name] = age

for name, age in newDict.items():
    print(name + " " + age)

# Guckt Euch bitte alle bisher erstellten Programme als Übung an!
# Einen schönen zweiten Advent
# Frank van den Boom