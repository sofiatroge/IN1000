"""
Progammet nede skal regne ut totalprisen for en bruker ved en restaurant. Det
som er mulig å konsumere i restauranten er pizza, spaghetti, dessert, øl, brus
og kaffe.Brukeren kan også velge hvor mye den vil ha av hver og programmet kommer
med betaling/totalprisen på slutten.
"""
#Dette er varebilene som kommer til å bli brukt i programmet ned
sum = 0
pizza = 200
spaghetti = 150
dessert = 40
øl = 98
brus = 45
kaffe = 35
a = "ja"
b = "nei"
p = "pizza"
s = "spaghetti"
br = "brus"
ø = "øl"

#dette printes ut på begynnelse av programmet
print("Hei! Velkommen til Fifa-Restaurant.")
print("Her kan man spise pizza, spaghetti og dessert,")
print("og kose seg med en øl, brus eller kaffe")

#her kan brukeres enten svare med pizza eller spaghetti slik at programmet kjører
spørsmål = input("Hva har du lyst å spise? pizza eller spaghetti?")
#etter svaret kan brukeren angi hvor mange de vil ha før neste spørsmålet
if spørsmål == p:
    spør = input("Hvor mange pizza skal du ha?\n>")
    sum = sum + (int(spør)*(pizza))
elif spørsmål == s:
    spør = input("Hvor mange spaghetti skal du ha?\n>")
    sum = sum + (int(spør)*(spaghetti))

#her kan brukeren angi hva den vil drikke om det enten er brus eller øl
spørs = input("Hva vil du drikke ved siden av? brus eller øl?")
#deretter kan brukeren igjen angi hvor mange de vil ha
if spørs == br:
    spør = input("Hvor mange brus skal du ha?\n>")
    sum = sum + (int(spør)*(brus))
elif spørs == ø:
    spør = input("Hvor mange øl skal du ha?\n>")
    sum = sum + (int(spør)*(øl))

#her er nest siste spørsmålet for brukeren hvor den kan svare med enten ja eller nei
sisteSpørsmål = input("Skal du ha dessert?")
#hvis svaret blir ja da kjører programmet her og spør hvor mange dessert den vil
#ha og om den vil ha kaffe slik at det kommer ut hvor mye brukeren skal betale
#etter å ha angitt om den skal ha kaffe og eventuell hvor mange den skal ha.
if sisteSpørsmål == a:
    spør = input("Hvor mange dessert skal du ha?\n>")
    sum = sum + (int(spør)*dessert)
    inp = input("Vil du ha kaffe ved siden av?")
    if inp == a:
        spør = input("Hvor mange kaffe skal du ha?\n>")
        sum = sum + (int(spør)*kaffe)
        print(f"Du skal betale: {sum} kr.")
    elif inp == b:
        print(f"Du skal betale: {sum} kr.")
#hvis svaret blir nei da kjører programmet her og spør om den vil ha kaffe
#slik at det kommer ut hvor mye brukeren skal betale etter å ha angitt om den
#skal ha kaffe og eventuell hvor mange den skal ha.
elif sisteSpørsmål == b:
    spør = input("Vil du ha en kaffe?")
    if spør == a:
        spør = input("Hvor mange kaffe skal du ha?\n>")
        sum = sum + (int(spør)*kaffe)
        print(f"Du skal betale: {sum} kr.")
    elif spør == b:
        print(f"Du skal betale: {sum} kr.")

"""
Løsning: programmet kjører som den skal uavhengi hvor mye man skal ha, den kommer
med korrekt sum på slutten.
"""
