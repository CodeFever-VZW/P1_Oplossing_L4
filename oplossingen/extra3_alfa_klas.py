# Maak een programma dat:
# - De gebruiker één voor één een naam van een klasgenoot laat intypen. Het programma blijft vragen tot er eens een lege string wordt ingevuld.
# - Je gaat dan deze lijst met namen alfabetisch sorteren.
# - Deze gesorteerde namen ga je dan printen.
klasgenoten = []

while True:
    naam = input("Voer de naam van een klasgenoot in (of druk op Enter om te stoppen): ")
    if naam == "":
        break
    klasgenoten.append(naam)

klasgenoten.sort()

for naam in klasgenoten:
    print(naam)