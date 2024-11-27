bestellung = [["Duschgel", 10, 4], ["Rasierschaum", 2, 3]]

def steuern_hinzufuegen(bestellung: list) -> list:
    for b in bestellung:
        if b[0].lower().startswith(tuple("abcdefghijk")):
            b[2] = round(b[2]*1.1,2)
        else:
            b[2] = round(b[2]*1.2,2)

<<<<<<< HEAD




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
=======
    return bestellung
>>>>>>> 4f0e54c13e0a0d8367118801576cdb7ab892ad22
