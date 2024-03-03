"""
1. Vil dette programmet kjøre? Begrunn svaret.
Nei, programmet kommer ikke til kjøre, fordi det blir tall plus tekst,
som ikke blir godkjent av python.
2. Hvilke problemer vil vi kunne møte på når vi kjører denne koden?
Om man kjører denne koden vil det komme feilmelding eller bedresagt
typefeil (typeError)siden det er 'int' + 'str' hvis tallet er mindre enn 10,
ellers kommer det til å kun stå "Tast inn et heltall!".
"""


a = input("Tast inn et heltall! ")
b = int(a)
if b < 10:
    print (b + "Hei!")

#Etter å ha kjørt programmet kan det jeg har skrevet over bekreftes.
