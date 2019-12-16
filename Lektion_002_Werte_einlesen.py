

zahlA = input("Bitte gib eine ganze Zahl ein: ")
zahlB = input("Bitte gib eine zweite ganze Zahl ein: ")
summe = zahlA + zahlB
print(summe)    # Ausgabe: "2342"


# Das ist nicht das was ich wollte. Ich wollte doch die Summe der beiden Zahlen ausrechnen.
# Eine Idee, was hier schief geht?

# Passen vlt. die Datentypen nicht mit dem zusammen, was ich möchte?

# Zweiter Versuch
zahlA = int(input("Bitte gib eine ganze Zahl ein: "))
zahlB = int(input("Bitte gib eine zweite ganze Zahl ein: "))
summe = zahlA + zahlB
print(summe)

# Jetzt funktioniert es. Aber was passiert wenn ich anstatt einer ganzen Zahl,
# einen String eingebe, z.B. Hallo?
# Teste mal das Programm!

# Fehlermeldung: ValueError: invalid literal for int() with base 10: 'Hallo'
# Ok, invalid literal for int. "Hallo" ist kein int, sondern ein String.
# Aber das Programm soll auf keinen Fall abstürzen.

# Es wird es etwas kompliziert:

while(True):
    try:
        zahlA = int(input("Bitte eine Zahl eingeben: "))
        break
    except:
        print("Du hast keine Zahl eingeben! Versuche es nochmal.\n")


while(True):
    try:
        zahlB = int(input("Bitte eine zweite Zahl eingeben: "))
        break
    except:
        print("Du hast keine Zahle eingeben! Versuche es nochmal.\n")

summe = zahlA + zahlB
print("Die Summe von " + str(zahlA) + " und " + str(zahlB) + " ist " + str(summe) + ".")

# Oha, dass muss man am Anfang auswendig lernen.........



