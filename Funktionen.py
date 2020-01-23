print('Hallo')
print("Guten Tag wie geht es Dir?")


# 1) Wie heisst die Funktion: printHello
# Funktionsname klein am Anfang und mit Verb
# 2) Wie viele Parameter/Argumente bekommt die Funktion: keinen
# 3) Was gibt die Funktion für einen Datentyp zurück?
# Datentypen kennt Ihr: string, int, bool, float, list, dict, map, tupple
# string    Zeichenkette
# int       ganze Zahl
# float     Fließkommazahl 3.14
# bool      Wahrheitswert True oder False
# list      Liste [1, 2, "Hund"]
# Antwort auf Frage 3: keine
def printHello():
    print("\nHallo in der Funktion\n")

printHello()

def calcSum(a, b, c):
    return a + b + c
# 1: Wie heisst die Funktion: calcSum
# 2: Wie viele Argumente/Parameter: 3
# 3 Welchen Datentyp gibt die Funktion zurück: int, float oder string

print(calcSum(1,2,3))

print(calcSum('a', 'b', 'c'))

#print(calcSum('a', 1, 2))

print(calcSum([1,2,3], [4,5,6], [1,1,1,1,1,1]))
