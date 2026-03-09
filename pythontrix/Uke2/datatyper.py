# a) Skriv et program som tar inn tre verdier – en streng, et heltall og et flyttall – og lagrer dem i tre variabler.
bil = input("Hva slags bil har du? ")
alder = int(input("Hvor gammel er den? "))
liter = float(input("Hvor mye drifstoff tenger du? Antall i liter: "))


# b) Utvid programmet, slik at det skriver ut hver verdi og typen til verdien. Sjekk at datatypen som skrives ut er som forventet.
#  Hvis resultatene ikke stemmer, gå tilbake til a).

print(type(bil), bil)
print (type(alder), alder)
print (type(liter), liter)


# c) For hvert av de fire tilfellene nedenfor, avgjør om programmet i b) vil kjøre og hva som blir resultatet av kjøringen. 
# Hvis du mener programmet ikke vil kjøre, forklar hvorfor. Du skal ikke kjøre programmet før du har et svar for hvert tilfelle.
# Husk at rekkefølgen på verdiene i alle tilfellene er streng, heltall og flyttall (som beskrevet i deloppgave a).

# Tilfelle 1: "", 0, 3.8 - vil kjøre
# Tilfelle 2: 1, 2, 3 - vil kjøre
# Tilfelle 3: 1, -0, 3.8 - vil kjøre, -0 bare blir til 0
# Tilfelle 4: 3.8, 3.8, 3.8 - vil ikke kjøre, da 3.8 ikke kan gjøres om til en int


# d) Utvid programmet for hvert av tilfellene nedenfor. Skriv ut typen til resultatet. Forklar hva som skjer i programmet. 
# Hvis ikke programmet kjører, forklar hvorfor.

# Tilfelle 1: Gang heltallet med strengen
print(3 * "Hei") # Output blit en str, bestående av feler Hei ved siden av hverandre "HeiHeiHei"
# Tilfelle 2: Gang heltallet med flyttallet
print (3 * 0.5) # Output blit en float: 1.5
# Tilfelle 3: Gang strengen med flyttallet
# print ("Hei" * 4.5)  # Output blir en feilmelding TypeError siden en sting ikke kan ganges med en float


# e) Hva skjer hvis programmet prøver å konvertere et flyttall til et heltall?
print (int(3.4)) # Tallet blir rundet ned til heltalet før komma, 3 i dette tilfelle