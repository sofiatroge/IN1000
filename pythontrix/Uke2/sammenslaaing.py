# Dette er en oppgave om kodeforståelse. Løs derfor deloppgavene uten å kjøre kodesnuttene først!

# Hvilke av kodesnuttene under vil gi en feilmelding? Begrunn svarene dine.

# a)

a = 10
b = "hei!"
c = a + b
print(c)

# Denne her vill gi en feilmelding, fordi man prøver å pluse sammen et tall og en string 
# i variabel c, som er noe som ikke er lov.

# b)

x = "10"
y = "hei!"
print(x + y)

# Denne her vill ikke gi en feilmelding, den vill printe ut "10hei!", den vill bare slå sammen
# strengene.

# c)

i = 10
j = "12"
print(i + j)

# Denne her vill gi en feilmelding, fordi man prøver å pluse sammen et tall og en string 
# i print, som er noe som ikke er lov, da 12 er antatt til å være en string her.

# d) Forsøk å kjøre de tre kodesnuttene hver for seg, og sjekk om du hadde rett.
# Antagelsene jeg har gjort er riktig.

# e) Bruk str() for å konvertere variabel a i oppgave a). Konverter variabel j fra oppgave c) til 
# et heltall på samme måte med funksjonen int() og kjør programmet på nytt. Hva skrives ut nå?

a = 10
b = "hei!"
c = str(a) + b
print(c)
# Nå skrives det ut "10hei!" i terminalen

i = 10
j = "12"
print(i + int(j))
# Nå plusses 10 og 12 sammen, som printer ut "22" i terminalen
