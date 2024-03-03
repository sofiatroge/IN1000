#funksjon som returnerer summen av to tall
def addisjon (tall1, tall2):
        return tall1 + tall2
#kaller og printer funksjonen med to heltall
print(addisjon(6,2))
#funksjon som trekker det andre tallet fra det første
def subtraksjon (tall1, tall2):
        return tall1 - tall2
#funksjon som deler det første tallet med det andre
def divisjon (tall1, tall2):
        return tall1 / tall2

#tester funksjonen subtraksjon ved hjelp av assert
assert subtraksjon(2,6) == -4
assert subtraksjon(-2,-6) == 4
assert subtraksjon(-2,6) == -8
#tester funksjonen divisjon ved hjelp av assert
assert divisjon(22,2) == 11
assert divisjon(-6,-3) == 2
assert divisjon(-64,2) == -32

#funksjon som konverterer fra tommer til centimeter
def tommerTilCm(antallTommer):
    assert antallTommer >0
    return antallTommer * 2.54
#tester funksjonen tommerTilCm
print(tommerTilCm(2))

#prosedyre som tar for seg beregninger
def skrivBeregninger():
    #henter inn noen verdier fra brukeren
    print("Nå ber jeg deg til å skrive inn to valgfrie tall.")
    tall1 = float(input("Skriv inn din første tall: "))
    tall2 = float(input("Skriv inn din andre tall: "))
    #kaller funksjonene og viser resultatene
    print("Utregninger:")
    print(f"Summen av tallene blir: {addisjon(tall1,tall2)}")
    print(f"Differens av tallene blir (første - andre tallet): {subtraksjon(tall1,tall2)}")
    print(f"Kvotient av tallene blir (første/andre tallet): {divisjon(tall1,tall2)}")
    #henter en verdi fra brukeren igjen
    print("Konvertering fra tommer til cm:")
    tall3 = float(input("Skriv inn et tall for tommer: "))
    #kaller og viser resultat
    print(f"Din antall tommer blir {tommerTilCm(tall3)} i centimeter")
#tester funksjonen tommerTilCm
print(tommerTilCm(5))

skrivBeregninger()
