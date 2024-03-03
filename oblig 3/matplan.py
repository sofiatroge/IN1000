#Først lager man et orbok med navn og måltider tik beboerne
ordbok = {"Luca Rossi" : ["croissant", "caprese", "pizza"]}
# deretter lages det en prosedyre som først skriver ut navnene til alle beboerne
def prosedyre():
    print("Følgende beboere oppført:")
    for x in ordbok:
        print(x)
#Etterpå spør man brukeren om å skrive et navn til en av beboerne i terminalen
    navn = input("Skriv inn navnet til en av beboere:")
    #hvis navnet er registert skrives dette ut i terminalen
    if navn in ordbok:
        print(f"{navn} har følgende matplan:")
        print(f"Frokost: {ordbok[navn][0]}")
        print(f"Lunsj: {ordbok[navn][1]}")
        print(f"Middag: {ordbok[navn][2]}")
    #om navnet ikke er registert skrives det dette her ut
    else:
        print("Beboeren er ikke regristert")
#her kaller man prosedyren 
prosedyre()

#Deloppgave 3
"""
a. Mengde, siden alle brukernavne på alle IN1000 studentene skal være unike
b. Ordbok, siden alle brukernavne skal være unike og de skal knyttes til hver
sine antall poeng
c.Liste, fordi man det kan hende at man må skrive et navn flere ganger
d. Mengde, siden alle allergener skal være unike
"""
