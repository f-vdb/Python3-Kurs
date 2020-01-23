import geldAusgabe

ausgabeA = geldAusgabe.GeldAusgabe("Frank", "Aldi", "", 21, 1, 2020, 75.23)
ausgabeB = geldAusgabe.GeldAusgabe("Sabine", "Kino", "", 22, 1, 2020, 7.50)

ausgaben = []
ausgaben.append(ausgabeA)
ausgaben.append(ausgabeB)

for ausgabe in ausgaben:
    ausgabe.zeigeAusgabe()

sum = 0.0

for ausgabe in ausgaben:
    sum = sum + ausgabe.getBetrag()

print("Summe aller Ausgaben: ", end="")
print("%.2f" % sum, "€")