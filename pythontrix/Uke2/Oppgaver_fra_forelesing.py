# Oppgave:
# Les inn en fart. Dersom fart er 60 eller mindre, skal
# man lage en streng som består av "fart:" og selve
# farten (f.eks. "fart:56"). Dersom fart er høyere enn 60,
# skal skal man lage strengen "fart:over 60".

fart = int(input())
if fart <= 60:
 svar1 = print("Fart: ", fart)
else:
 svar2 = print("Fart: over 60.")

#  Spør brukeren om alder (bruk input):
# •Dersom mindre enn 6: skriv ut "Lek i skogen"
# •Dersom mindre enn 3: skriv ut "Lek i lekegrinda"
# •(ikke skriv ut noe ellers)
# •Skal uansett skrive ut maksimalt én setning

alder = int(input("Hvor gammel er du? "))
if alder < 6:
 if alder < 3:
  print("Lek i lekegrinda")
 else:
  print ("Lek i skogen")