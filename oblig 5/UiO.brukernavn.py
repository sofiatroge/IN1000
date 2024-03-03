"""
Programmet nede legger til nye UiO brukernavn til en samling
og fastslå deres e-post
"""
#funksjon nede tar inn fullt navn fra brukeren og returnere en tilsvarlig
#UiO-brukernavn
def lagBrukernavn (fulltNavn):
    #deler opp navnet
    deler = fulltNavn.split()
    # spesifiserer og henter både fornavn og etternavn
    fornavn = deler[0]
    etternavn = deler[1]
    #legrer brukernavn
    brukernavn = str.lower(fornavn) + str.lower(etternavn[0])
    #returnerer brukernavnet
    return brukernavn

#neste funksjon tar imot prefix og suffix, og returnerer epostadressen
def lagEpost (prefix, suffix):
    email = prefix + "@" + suffix
    return email

#prosedyre nede tar inn en ordbok med prefix som nøkkelverdi og suffix som
# innholdsverdi. Disse blir sendt til funksjonen lagEpost og tilslutt printes eposten
def skrivUtEposter(ordbok):
    for prefix in ordbok:
        print(lagEpost(prefix, ordbok[prefix]))

ordbok = {}
#tester om lagBrukernavn fungerer
print(lagBrukernavn("Sofia Ibn El Moujdi Troger"))
#tester om skrivUtEposter fungerer
testordbok = {"olan": "ifi.uio.no", "karian": "student.matnat.uio.no"}
skrivUtEposter(testordbok)


#neste program lar brukeren benytte både prosedyren og funksjonene over
kommando = ""
# i while-løkken ser man at hvis brukeren taster inn "s" slutter programet
while kommando != "s":
    #henter kommando fra brukeren
    kommando = input("Kommando: ")
    #kommando i legger til en bruker i ordboken
    if kommando == "i":
        print("Du får nå en bruker")
        #henter navn og sufiksen som trenges for at programet skal kjøre riktig
        fulltNavn = input("Fullt navn: ")
        suffix = input("Suffix, det bak @: ")
        #lager brukernavn
        brukernavn = lagBrukernavn(fulltNavn)
        #legger den til i ordbok
        ordbok[brukernavn] = suffix
    #p printer epostadressen til brukeren i ordboken
    elif kommando == "p":
        skrivUtEposter(ordbok)
