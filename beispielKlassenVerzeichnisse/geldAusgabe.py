
class GeldAusgabe():
    def __init__(self, oberKategorie, unterKategorie, kommentar, tag, monat, jahr, betrag):
        self.oberKategorie = oberKategorie
        self.unterKategorie = unterKategorie
        self.kommentar = kommentar
        self.tag = tag
        self.monat = monat
        self.jahr = jahr
        self.betrag = betrag

    def zeigeAusgabe(self):
        print("Oberkategorie: " + self.oberKategorie)
        print("Unterkategorie: " + self.unterKategorie)
        print("Kommentar: " + self.kommentar)
        print("Datum: " + str(self.tag) + "." + str(self.monat) + "." + str(self.jahr))
        print("Betrag: ", end="")   # lasse das newline am Ende der Zeile weg, da der Betrag z.B. 7,50
                                    # hinter "Betrag: " stehen soll
        print("%.2f" % self.betrag, "€")  # zeige zwei Dezimalstellen, damit 7.50 angezeigt wird anstatt 7.5
        print("----------------------------------------------------------")

    def getBetrag(self):
        return self.betrag




