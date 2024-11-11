print("test")


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
