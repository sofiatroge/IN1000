# Lag en prosedyre som ber om og leser inn to heltall. Prosedyren skal deretter regne ut 
# differansen mellom de to tallene og skrive ut svaret. Kjør programmet for å sjekke at alt 
# fungerer som det skal.

# Her er et eksempel på hvordan en kjøring av programmet kan se ut:

# Oppgi verdien til x: 
# > 25
# Oppgi verdien til y: 
# > 19
# Differansen mellom x og y er 6.
# Du behøver ikke tenke på at det første tallet kan være mindre enn det andre. Det er ikke 
# nødvendig å regne ut absoluttverdien av differansen (men prøv gjerne å finne ut hvordan det 
# gjøres, dersom du ønsker en ekstra utfordring).

def differanse():
    x = int(input("Oppgi verdien til x: "))
    y = int(input("Oppgi verdien til y: "))
    
    print("Differansen mellom x og y er ", x - y)

differanse()