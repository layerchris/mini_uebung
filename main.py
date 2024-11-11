bestellung = [["Duschgel", 10, 4], ["Rasierschaum", 2, 3], ["Zahnpasta", 2, 3], ["Turnschuhe", 1, 50] ,["Cola", 15, 1], ["Bier", 20, 1.2]]

def berechne_gesamtpreis_mit_rabatt(bestellung):
    gesamtpreis = 0

    for artikel in bestellung:
        name, menge, preis_pro_stueck = artikel

        if menge >= 10:
            rabatt = 0.10
        elif menge >= 5:
            rabatt = 0.05
        else:
            rabatt = 0.0

        preis_nach_rabatt = preis_pro_stueck * (1 - rabatt)
        gesamtpreis_artikel = menge * preis_nach_rabatt

        gesamtpreis += gesamtpreis_artikel
    print(gesamtpreis)
    return gesamtpreis


def steuern_hinzufuegen(bestellung: list) -> list:
    for b in bestellung:
        print(b[0])
        if b[0].lower().startswith(tuple("abcdefghijk")):
            b[2] = round(b[2]*1.1,2)
        else:
            b[2] = round(b[2]*1.2,2)

    return bestellung


def berechne_bestellungssumme(artikel_liste):
    gesamtbetrag = 0
    for artikel in artikel_liste:
        artikel_name = artikel['name']
        preis_pro_artikel = artikel['preis']
        anzahl_artikel = artikel['anzahl']

        # Rabattberechnung
        preis_mit_rabatt = berechne_rabatt(preis_pro_artikel, anzahl_artikel)

        # Steuerberechnung
        steuer = berechne_steuer(artikel_name, preis_mit_rabatt)

        # Portokostenberechnung
        portokosten = berechne_portokosten(artikel_name, anzahl_artikel)

        # Gesamtsumme für diesen Artikel
        artikel_summe = preis_mit_rabatt + steuer + portokosten
        gesamtbetrag += artikel_summe

    return gesamtbetrag


steuern_hinzufuegen(bestellung)
#berechne_gesamtpreis_mit_rabatt(bestellung)
#berechne_bestellungssumme(bestellung)

print(bestellung)
