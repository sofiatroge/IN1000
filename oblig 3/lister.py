#her lager jeg en liste med 3 tall som jeg valgte selv
førsteListe = [2,4,6]
#på neste kode legger jeg et nytt tall på sluten av listen
førsteListe.append(8)
# deretter printer programmet første og tredje elemente i listen
print(førsteListe[0])
print(førsteListe[2])

#lager en ny og tom liste
liste = []
#på neste steg ber programmet brukeren å oppgi 4 navn som bli lagt inn i listen
#alt dette i skjer ved at man kaller denne følgende prosedyre
def liste1():
    navn = input("Skriv inn et navn:")
    liste.append(navn)
#her kaller man prosedyren 4 ganger
liste1()
liste1()
liste1()
liste1()

#deretter sjekker programmet om brukern har skrevet inn navnet mitt eller ikke
# slik at det printes ut passende responds
if 'Sofia' in liste:
    print("Du husket meg!")
else:
    print("Glemte du meg?")

#her lages en ny liste
nyListe = []
#deretter beregnes det summen av første listen og deretter produktet
sum = (førsteListe[0]+førsteListe[1]+førsteListe[2]+førsteListe[3])
produkt = (førsteListe[0]*førsteListe[1]*førsteListe[2]*førsteListe[3])

#etterpå legges summen av tallene og produktet av tallene inn i den ny listen
nyListe.append(sum)
nyListe.append(produkt)

#her legges første listen og den nye listen sammen i en ny liste
sammenliste = førsteListe + nyListe

#rett etter printes den sammesatte liste
print(sammenliste)
#men etterpå sletter man de to siste elementen i listen
sammenliste.pop()
sammenliste.pop()
#og da skrives listen ut en gang til
print(sammenliste)
