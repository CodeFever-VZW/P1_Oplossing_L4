# Schrijf een programma genaamd “Score bijhouden”.
# De gebruiker kan:
# - Scores toevoegen
# - De hoogste score bekijken
# - Het gemiddelde berekenen
# - Het programma beëindigen

scores = []


def vraag_keuze():
    print("Score bijhouden:")
    print("1. Score toevoegen")
    print("2. Hoogste score bekijken")
    print("3. Gemiddelde score berekenen")
    print("4. Exit")

    return input("Kies een optie: ")


def voeg_score_toe():
    score = int(input("Voer een score in: "))
    scores.append(score)
    print("Score toegevoegd.")


def bekijk_hoogste_score():
    if scores:
        hoogste_score = max(scores)
        print("Hoogste score: ", hoogste_score)
    else:
        print("Er zijn nog geen scores ingevoerd.")


def bereken_gemiddelde_score():
    if scores:
        gemiddelde_score = sum(scores) / len(scores)
        print("Gemiddelde score: ", gemiddelde_score)
    else:
        print("Er zijn nog geen scores ingevoerd.")


def score_bijhouden():
    while True:
        keuze = vraag_keuze()
        if keuze == '1':
            voeg_score_toe()
        elif keuze == '2':
            bekijk_hoogste_score()
        elif keuze == '3':
            bereken_gemiddelde_score()
        elif keuze == '4':
            break
        else:
            print("Ongeldige keuze. Probeer opnieuw.")

    print("Bedankt voor het gebruik van het score programma. Tot ziens!")


score_bijhouden()