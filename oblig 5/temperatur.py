# funksjon nede tar inn en fil og returnerer en ordbok
def maxTempTilOrdbok(fil):
    # leager en ny ordbok
    ordbok = {}
    # for hver linje
    for linje in open(fil):
        # del opp linjen med en komma
        deler = linje.split(",")
        # putt inn delene i ordboken
        ordbok[deler[0]] = float(deler[1])
    # returnerer ordboken
    return ordbok

# kaller maxTempTilOrdbok()
høyesteTemp = maxTempTilOrdbok("max_temperatures_per_month.csv")
# printer ordboka
print(høyesteTemp)

# funksjon nede tar imot en ordbok med varmeste temperaturer og en fil med
# daglige temperaturer, leser de daglige temperaturer linje for linje, printer
# en beskjed dersom det blir funnet en ny høyeste temperatur, og returnerer en
# oppdatert ordbok
def nyMaxTemp(ordbok,fil):
    # for hver linje, vil i dette tilfelle si for hver dag
    for linje in open(fil):
        # deler opp linjen
        deler = linje.split(",")
        # gir bedre navn til delene
        måned = deler[0]
        dager = int(deler[1])
        temperatur = float(deler[2])
        # I tilfelle temperatur er større enn den forige høyeste temperatur for
        # måneden
        if temperatur > ordbok[måned]:
            # print og si ifra om en ny temperatur ble funnet
            print(f"Ny varmerekord ble funnet den {dager}. {måned} på {temperatur} grader Celsius. Forrige rekord var {ordbok[måned]} grader.")
            # oppdater ordboka
            ordbok[måned] = temperatur
    # returnerer den oppdaterten ordbok
    return ordbok
# kaller nyMaxTemp()
nyhoyesteTemperaturer = nyMaxTemp(høyesteTemp,"max_daily_temperature_2018.csv")
#printer den oppdaterte ordboka
print(nyhoyesteTemperaturer)

# neste prosedyren tar imot en ordbok og et filnavn, og skriver ordboken til en
# ny fil med det angitte filnavnet
def eksportOrdbok(ordbok,filnavn):
    #lager ny en fil for skriving
    fil = open(filnavn, "w")
    #for hver måned
    for måned in ordbok:
        #skriv ny linje med måned og grader
        fil.write(måned + "," + str(ordbok[måned]) + "\n")

#kaller eksportOrdbok
eksportOrdbok(hoyesteTemperaturer, "test.csv")
