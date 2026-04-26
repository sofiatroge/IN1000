# I det fiktive landet Ruritania er skattereglene slik at hvis en person har inntekt < 10000, 
# så betaler man 10% skatt på hele inntekten, og hvis inntekten >= 10000, så betaler man 10% skatt 
# på de første 10000 kronene og 30% skatt på resten av inntekten.

# a) Lag et program som regner ut og skriver ut hvor mange kroner som skal betales i skatt, 
# gitt inntekten. Programmet skal lese inntekten fra terminal. Anta at inntekten oppgis som et 
# flyttall.

inntekt = float(input("Hva er din inntekt?"))

if inntekt < 10000:
    skatt = inntekt * 0.1
    print(skatt)
else:
    først = 10000 * 0.1
    inntekt = inntekt - 10000
    skatt = (inntekt * 0.3) +først
    print (skatt)

# b) Kjør programmet ditt og sjekk at du får riktig resultat. Under ser du et eksempel på en 
# kjøring av programmet.

# Tast inn din inntekt:
# > 5000
# Skatt: 500.0
# Tast inn din inntekt:
# > 20000
# Skatt: 4000.0

# Hva er din inntekt?5000
# 500.0
# Hva er din inntekt?20000
# 4000.0
