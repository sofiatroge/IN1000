# Skriv et program som ber brukeren gi svaret på enkle matteoppgaver.

# For eksempel:   1 + 1   5 * 4   10 / 2

# Hvis brukeren gir det riktige svaret, skriv ut "Riktig!" og still det neste spørsmålet.
# Hvis brukeren gir et feil svar, skriv ut "Beklager, det var feil! Spillet er over." 
# Hvis brukeren svarer på alle spørsmålene riktig, skriv ut "Gratulerer, du vant!"

# Programmet skal bestå av minst 3 spørsmål og avslutte hvis brukeren svarer feil.

svar = int(input ("Hva er 1 + 1? "))

if svar == 2:
    print ("Riktig!")
    svar = int (input ("Hva er 5 * 4? "))
    if svar == 20:
        print ("Riktig!")
        svar = int (input ("Hva er 10 / 2? "))
        if svar == 5:
            print ("Gratulerer, du vant!")
        else:
            print ("Beklager, det var feil! Spillet er over.")
    else:
            print ("Beklager, det var feil! Spillet er over.")
else:
            print ("Beklager, det var feil! Spillet er over.")