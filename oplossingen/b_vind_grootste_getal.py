# Maak een lijst met getallen.
# Schrijf een functie vind_grootste_getal die de grootste waarde uit een lijst teruggeeft.
# Gebruik een for-loop om de grootste waarde te vinden.
getallen = [5, 2, 9, 13, 4, 42, 8, 1]

def vind_grootste_getal(lijst):
    grootste_getal = lijst[0]  # Neem het eerste getal als het grootste
    for getal in lijst:
        if getal > grootste_getal:
            grootste_getal = getal
    return grootste_getal

resultaat = vind_grootste_getal(getallen)
print("Het grootste getal is:", resultaat)

# of met een ingebouwde functie
resultaat = max(getallen)
print("Het grootste getal gevonden met een ingebouwde functie is:", resultaat)