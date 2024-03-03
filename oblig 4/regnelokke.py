adversel = print(f"For å stoppe programmet tast inn tallet 0")

liste = [] #en tom liste som kommer i bruk i linje 10
svar = -1
# Programet nede er lsget med en while-løkke slik at "Skriv inn et tall" printes
# ut so mange ganger helt til brukeren taster inn 0
while svar != 0:
    svar = int(input("Skriv inn et tall"))
    # i neste steg lager programet alle svarene inn i et liste
    liste.append(svar)
# nede finnes det en for løkke som skriver ut hver element i listen
for x in liste:
    print(x)

minSum = 0
# løken nede går igjen gjennom listen og legger verdien til minSum
for x in liste:
    minSum += x
    # nede skrives det ut summen til brukeren
print(f"Summen din blir:{minSum} ")

# neste stegene finner ut hvilken av veriden i listen er minst og hvilen størst
# her finner programtet ut hvilket av tallene er minst i listen og printer den ut
minst = liste[0]
for x in liste:
    if x < minst:
        minst = x

print(f"Din min:{minst}")

# her finner programtet ut hvilket av tallene er størst i listen og printer den ut

størst = liste[0]
for x in liste:
    if x > størst:
        størst = x

print(f"Din max:{størst} ")
