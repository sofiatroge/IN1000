# programmet nedfor for opp spørsmålet om når juleaften er som brukeren
# bør besvare med 24.12
juleaften = input ("Når er juleaften? (DD.MM)")
ønsketSvar = "24.12"
if juleaften == ønsketSvar:
    print("24.desember er helt riktig")
    # om brukeren ikke besvarer med 24.11 for den opp meldingen nedefor
    # om hva som kan ha godt feil, og deretter for man et ny mulighet
    # til å besvare spørsmålet
else:
    print ("Sjekk at du skrev DD.MM (eksempel 31.08 for 31 august)")
    prøvigjen= input ("Når er juleaften? (DD.MM)")
    ønsketSvar = "24.12"
    if prøvigjen == ønsketSvar:
        print("24.desember er helt riktig!")

# programmet nedfor for opp spørsmålet om hva siste dag er i året som
# bør besvare med 31.12
sisteDag = input("Hva er siste dag i året? (DD.MM)")
annetSvar = "31.12"
if sisteDag == annetSvar:
    print("31.desember er helt riktig!")
    # om brukeren ikke besvarer med 31.11 for den opp meldingen nedefor
    # om hva som kan ha godt feil denne gangen, og for et ny mulighet
    # til å besvare spørsmålet
else:
    print ("Sjekk at du skrev DD.MM (eksempel 31.08 for 31 august)")
    andreførsøk = input("Hva er siste dag i året? (DD.MM)")
    annetSvar = "31.12"
    if andreførsøk == annetSvar:
        print("31.desember er helt riktig!")

# programmet nedefor er som en liten test hvor brukeren skal skrive inn
# tre forskjellige datone
print ("Nå skal vi gjennomføre en liten test :)")
a = input("Skriv inn en dato fra sommeren (DD.MM)")
b = input("Skriv inn en dato fra våren (DD.MM)")
c = input("Skriv inn en dato fra høsten (DD.MM)")

# deretter skal de sette inn i riktig rekkefølge,
# med utganspunktet på hva brukere svarte på
# Det som bør komme ut er at datoen fra våren kommer før sommer datoen
# ellers får brukere andre svar, men datone må vare ut fra de tre som ble
# spurt om på overfor
Spørsmål = input(f"Hvilket av disse datone kommer før {a}?")
if Spørsmål == b:
    print("Riktig rekkefølge!")
elif Spørsmål == c:
    print("Feil rekkefølge!")
elif Spørsmål == a:
    print ("Samme dato!")
