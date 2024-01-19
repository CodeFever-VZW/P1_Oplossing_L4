# Maak een uitbreiding op de oefening favoriete dieren (a).
# - Na het printen van de lijst vraag je welk dier uit de lijst moet.
# - Nadien toon je de lijst opnieuw maar deze keer zonder het gekozen dier.
favoriete_dieren = []


def vraag_dier():
    return input("Geef één van je favoriete dieren: ")


def print_favoriete_dieren(mededeling="Jouw favoriete dieren:"):
    print(mededeling)
    print(favoriete_dieren)


def verwijder_dier_en_print():
    dier = input("Welk dier moet weg?")
    favoriete_dieren.remove(dier)
    print_favoriete_dieren("Jouw favoriete dieren met 1 diertje minder:")


for _ in range(3):
    favoriete_dieren.append(vraag_dier())

print_favoriete_dieren()
verwijder_dier_en_print()