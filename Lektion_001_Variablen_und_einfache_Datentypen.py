
print("Hallo Python-Welt")

# Kommentarzeile
'''
Kommentarblock
'''

'''
Datentypen (Datenarten) in Python:

Bezeichnung       | Fachbegriff    | Abkürzung      | Beispiele
============================================================================================================
Ganzzahl          | Integer        | int            | 23, 42, -10, 0
------------------------------------------------------------------------------------------------------------
Fließkommazahlen  | Float          | float          | 3.14, -1.6, 0.0, 23.0, 1.666
------------------------------------------------------------------------------------------------------------
Zeichenketten     | String         | str            | "Hallo", "23", "0.0", "Du bist ein guter Mensch."  
'''

message = "Guten Tag, wie geht es Dir?"

print(message)

message = "Super, dass Du die Motivation hast, Python zu lernen."

print(message)

print(type(message)) # gibt den Datentyp von message aus - str (String)

x = 23          # Variablenname: x      Variablenwert: 23       Variablentyp: Int (Integer)
y = 42          # Variablenname: y      Variablenwert: 42       Variablentyp: Int (Integer)

# Variablenname immer mit einem Kleinbuchstaben beginnen.

sum = x + y
print(sum)
print(x + y)
print(sum + sum)
x = 0
y = 13
sum = x + y
print(sum)

firstName = "ada"
lastName = "lovelace"
fullName = firstName + " " + lastName   # hier werden drei Strings aneinander gehängt
                                        # Das + Zeichen ist hier keine Addition. Sondern die Strings werden
                                        # aneinander gehängt.
print(fullName)
print("Ada Lovelace schrieb in den 40er-Jahren des 19. Jahrhunderts das erste Computerprogramm der Welt.")
print("Gemessen an dem Stand der Forschung der damaligen Zeit ist ihr Werk visionär.")
print(fullName.upper())     # fullName in Grossbuchstaben ausgeben
print(fullName.lower())     # fullName in Kleinbuchstaben ausgeben

x = 3.14                    # Variablenname: x      Variablenwert: 3.14     Variablentyp: float
print(type(x))
print(x)

# Warum ist das ein Fehler:
# print("Hallo " + 23)
# Warum ist das kein Fehler:
print("Hallo " + str(23))
#Hilfe
print(type(23))
print(type(str(23)))

# addieren
x = 1 + 2
# subtrahieren
x = 10 - 5
# multiplizieren
x = 4 * 4
# potenzieren
x = 3 ** 3
print(x)
# dividieren
x = 20 / 10
x = 10.0 / 3.0
print(x)    # 3.3333333
x = 10 / 3
print(x)    # 3.3333333 Python wandelt die Ganzzahlen (int) in Fließkommazalen (float) um
            # Fachausdruck für Typumwandlung: "casten"

# Was passiert wenn ich eine float-Zahl wie 3.14 in eine int-Zahl umwandle (caste)?
print("Achtung:")
print(int(3.9))
print("Hier wird aus der float-Zahl 3.14 die Ganzahl 3.")
print("Der Teil links hinter den Komma wir einfach abgeschnitten. - Es wird nicht gerundet!!!")

print(2 + 3 * 4)    # Punkt vor Strichrechnung
print((2 + 3) * 4)  # Klammerrechnung


# Sonderzeichen
# Tabulator \t      Newline \n
print("/tHallo\n\n")
message = "\n\n\t1.Zeile\n2.Zeile\n\t3.Zeile\n4.Zeile"
print(message)
print("\n\n\t" + "1.Zeile" + "\n" + "2.Zeile" + "\n\t" + "3.Zeile" + "\n" + "4.Zeile")

message = "1.Zeile\n\t2.Zweile\n\t\t2.Zeile\n\t\t\t3.Zeile\n\t\t\t\t4.Zeile"
print(message)