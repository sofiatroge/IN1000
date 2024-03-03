"""
først og fremst lages det en prosedyre, hvor brukeren blir spurt om alder som
lagres i variabelen alder som en heltall etterpå lages det en varabiel for
billettpris med tallverdien 0 og deretter ser man om bruker er under 17 eller
akkurat 17, eller om den er over 17 men under 63 eller om brukeren er 63 eller
eldre slik at passende billettprisen printes ut
"""
def info():
    alder = int(input("Hvor gammel er du?\n"))
    billettpris = 0
    if alder <= 17:
        billettpris =30
    elif alder < 63:
        billettpris = 50
    else:
        billettpris = 35
    print(f"Billettprisen blir {billettpris} kroner")
info()
