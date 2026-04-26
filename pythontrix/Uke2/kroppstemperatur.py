# Hos friske mennesker varierer kroppstemperaturen vanligvis mellom 36.5 og 37.5 grader. 
# Lag et program som avgjør om en persons kroppstemperatur ligger henholdsvis under, innenfor 
# eller over normal kroppstemperatur og skriver ut en passende melding. Programmet skal lese 
# kroppstemperaturen fra terminal.

def kroppstemperatur():
    temperatur = float(input("Hva er kroppstemperaturen din? "))
    if temperatur < 36.5:
        print("Kroppstemperaturen diin ligger henholdsvis under normal kroppstemperatur. ")
    elif temperatur > 37.5:
        print("Kroppstemperaturen diin ligger henholdsvis over normal kroppstemperatur. ")
    else:
        print("Kroppstemperaturen diin ligger henholdsvis under innenfor kroppstemperatur. ")

kroppstemperatur()