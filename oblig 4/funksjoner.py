# her lager man en prosedyr slik at det man telle sammen to tall sammen
def adder (tall1, tall2):
    # her kaller man tilbake funksjonen
    return tall1 + tall2
# i de neste to kaller man på funksjonen, med to tall og det skrives ut resultat
# i stedet for {adder(..,..)}
print(f"Summen av 22 og 11 er {adder(22,11)}.")
print(f"Summen av 50 og 99 er {adder(50,99)}.")

# her ber man bruker til å skrive in en tekstreng og deretter et bokstav
tekststreng = input(f"Skriv inn en tekst:")
bokstav = input(f"Skriv en bokstav inn her:")

# her lages det et nytt funksjon som teller hvor mange ganger bokstaven forekommer
# i teksten som brukeren har oppgit i oppfordringen overfor.
def tellForekomst(minTekst, minBokstav):
    forekomster = 0
    for x in list(minTekst):
        if x == minBokstav:
            forekomster += 1
    return forekomster
# i neste steg gjør at funksjonen over kjører riktig, siden denne varabielen
# kaller tilbake på hva brukeren hadde oppgitt.
forekomster = tellForekomst(tekststreng, bokstav)
# her skrives det ut hvor mange ganger en av bokstavene forekom i teksten
print(f"Bokstaven du har oppgitte bokstaven forekommer {forekomster} ganger i teksten.")
