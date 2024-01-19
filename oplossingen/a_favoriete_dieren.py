# Maak een programma dat:
# - een lege lijst aanmaakt
# - drie dieren vraagt aan de user
# - deze dieren toe voegt aan de lijst
# - de lijst met dieren toont aan de user

favoriete_dieren = []

def vraag_dier():
    return input("Geef één van je favoriete dieren: ")

for _ in range(3):
    favoriete_dieren.append(vraag_dier())

print("Jouw favoriete dieren:")
print(favoriete_dieren)