bestellung = [["Duschgel", 10, 4], ["Rasierschaum", 2, 3]]

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


berechne_gesamtpreis_mit_rabatt(bestellung)



