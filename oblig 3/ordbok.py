# her lages det en ordbok som inneholder en oversikt over varer i
# butikk og pris
varer = {"melk":14.90,"brød":24.90,"yoghurt":12.90,"pizza":39.90}
# her skrives det ut innholdet i ordboken
print(varer)

#deretter inførmerer man bruker om hva som skal skje spør man brukern om
print("Hei, nå skal du legge til en ny vare")
# etterpå spør man brukern om navn og pris til en ny vare
nyvare = input("Oppgi navn til den nye varen:")
pris = float(input("Oppgi pris i kroner med puntum istenfor komma:"))

#deretter legger man den nye varen og prisen inn i ordboken
varer[nyvare] = pris
#slik at man skriver ut den nye ordboken
print(varer)
