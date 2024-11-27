bestellung = [["Duschgel", 10, 4], ["Rasierschaum", 2, 3]]

def steuern_hinzufuegen(bestellung: list) -> list:
    for b in bestellung:
        if b[0].lower().startswith(tuple("abcdefghijk")):
            b[2] = round(b[2]*1.1,2)
        else:
            b[2] = round(b[2]*1.2,2)

    return bestellung