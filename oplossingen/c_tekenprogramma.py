# We gaan aan de gebruiker een aantal instructies vragen en op basis daarvan tekenen.
# - Maak eerst een lege lijst waar de stappen in zullen komen.
# - Maak een oneindige lus:
#     - Vraag een stap aan de gebruiker
#     - Als het gelijk is aan “stop”, breek uit de lus.
#     - Anders, voeg het toe aan de lijst met stappen.
# - Itereer over de stappenlijst om te tekenen.

import turtle

stappen = []


while True:
    stap = input("Zeg l, r, b of o. Zeg stop als je klaar bent: ")
    if stap == "stop":
        break
    else:
        stappen.append(stap)

for stap in stappen:
    if stap == "l":
        turtle.setheading(180)
    elif stap == "r":
        turtle.setheading(0)
    elif stap == "b":
        turtle.setheading(90)
    elif stap == "o":
        turtle.setheading(270)
    turtle.forward(50)

turtle.done()