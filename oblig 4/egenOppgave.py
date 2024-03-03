"""
Progammet nede skal sortere obligene de neste fem en student har slik at den som
skal leveres først står først osv.
"""
adversel = print("Skriv inn dato for de neste fem Obligene")
# først lages det en liste med navn obligDato
obligDato = []
# deretter lages det en for-løkke som gir brukeren mulighet til å skrive inn
# fem datoer og emner som blir etterpå lagret inn i listen obligDato
for x in range(5):
    obligDato.append(input("Legg til måned, dag og emne til obligene du har (eks. 10.04 IN1020) "))
# i neste steg sorteres datoene som brukeren har skrivet inn og nå ligger i listen
obligDato.sort()
# deretter skrives det følgende setning:
print("Obligene er sortert etter dato, slik at nærmeste oblig står først")
# og til slutt skrives den sorterte listen "obligDato" ut
print(obligDato)

"""
Løsning: programmet kjører som den skal og sorterer datone til obligen.
"""
