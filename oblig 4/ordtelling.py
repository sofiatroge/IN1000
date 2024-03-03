# funksjonen teller og retutnerer hvor mange bokstaver det er i ordet
def antallBokstaver(ord):
    return len(ord)
# funksjonen returnerer ei ordbok hvor hvert ord i setningen er en nøkkelverdi
# og hvor ofte ordet dukker opp i setningen
def antallOrd(setning):
    ord = setning.split()
    antallOrd = {}
    for x in ord:
        if x in antallOrd:
            antallOrd[x] += 1
        else:
             antallOrd[x] =1
    return antallOrd

# i neste steg skal programet spørre etter en setning fra brukeren
setning = input("Skriv en setning: ")
# deretter lages det en ny varabiel som gjør hvert ord i setningen til en nøkkelverdi
totalOrd = len(setning.split())
# dermed kan man skrive ut hvor mange ord setningen består av
print(f"Setningen du skrev inn består av {totalOrd} ord.")
# her hentes det funksjonen som ble skrevet in i linje 6
antallOrd = antallOrd(setning)
# og til slutt skrives det ut hvor ofte hver ord forekomer i setningen
for x in antallOrd:
    print(f"Ordet {x} forekom {antallOrd[x]} ganger, og den består av {antallBokstaver(x)} bokstaver.")
