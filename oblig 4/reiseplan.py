# nede finnes det tre forskjellige lister en for steder, en for klesplagg og
# en for avreisedatoer
steder = []
klesplagg = []
avreisedatoer = []

# i neste steg lages det tre for-løkke, slik at hver liste har en for seg selv
# og det er kun mulig for brukeren å legge til fem elementer i hver liste

for x in range(5):
    steder.append(input("Legg til en reisedestinasjon: "))
for x in range(5):
    klesplagg.append(input("Legg til et klesplagg: "))
for x in range(5):
    avreisedatoer.append(input("Legg til en avreisedato: "))

# her lages det en ny list som inneholder de andre tre listene
reiseplan = [steder, klesplagg, avreisedatoer]
# nede finnes det en for-løkke som skriver ut innholdet i den nye listen reiseplan
for x in reiseplan:
    print(x)
# her hentes det en det en av de tre listene som befinner seg i reiseplan
i1 = int(input("Oppgi første indeksen fra 0 til 2: "))
# deretter henter man en av de fem elementene som finnes i den utvalgte listen
i2 = int(input("Oppgi andre indeksen fra 0 til 4: "))

# nede lages det en if-skjekk for å være sikkre at verdiene brukeren har oppgitt
# finnes og dermed skrives det enten ut en av elementen eller skrives det ut
# "Ugyldig input!"
if (i1 >= 0 and i1 <=2) and (i2 >= 0 and i2 <= 4):
    print(reiseplan[i1][i2])
else:
    print("Ugyldig input!")
