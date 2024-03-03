"""
Progammet nede skal finne ut om det finnes allegener som brukern ikke tåler
i en meny. ved en restaurant. Det som er mulig å konsumere er falafal, kveite og
stiek og det er kun bestemte allergene som kan oppgis.
"""
#advarsel slik at brukern hvet hva som skjer hvis den ikke oppgir en allergener
#som blir akseptert på egenhånd
advarsel = "Du kan bare svare med en av følgende allergene: melk, egg, gluten og nøtter"
#her lages det en liste som blir avhengi av hva som printes ut til slutt.
liste = []
#spørsmål som brukeren for opp og skal svare på i terminalen
allergi = input("Hva er du allergisk mot?")
#her tar det opp i listen hva brukeren svarte på spørsmålet over
liste.append(allergi)
#her er de forskjellig responds brukeren kan få avhengig av hva som står i listen
#etter spørsmålet
if 'melk' in liste:
    print("Du kan bestille falafal")
elif 'egg' in liste:
    print("Du kan bestille kveite")
elif 'gluten' in liste:
    print("Du kan bestille steik")
elif 'nøtter' in liste:
    print("Du kan bestille enten kveite eller steik")
else:
    print(advarsel)

"""
Løsning: programmet kjører for uansett hvilket allergen man oppgir ellers kommer
opp advarselen.
"""
