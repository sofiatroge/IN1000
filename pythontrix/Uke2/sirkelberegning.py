# a) Les om formatering av utskrift på side 54-57 i læreboken (Python for Everyone) eller 
# i Python-dokumentasjonen.
import math
# b) Skriv et program som tar imot et flyttall radius fra bruker.
radius = float(input("Oppgi radiusen: "))

# c) Beregn så diameter, areal og omkrets av sirkelen i tre nye variabler.
diameter = 2 * radius
areal = math.pi * radius**2
omkrets = 2 * math.pi * radius

# d) Skriv ut verdiene du beregnet i c), men vis kun 2 desimaler. Sørg også for at tallene blir 
# plasserte like langt til høyre. Eksempel på utskrift:
print(f'Diameter: {diameter:.2f}')
print(f'Areal: {areal:.2f}')
print(f'Omkrets: {omkrets:.2f}')

# Diameter:    12.00
# Areal:      113.10
# Omkrets:     37.70

