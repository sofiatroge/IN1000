# med programet får brukeren opp spørsmåler om den har lyst på en bruse
# den kan besvare den enten med ja, nei eller noe helt annet
# uansett hva svaret blir får brukeren en svar tilbake
Spørsmål = input("Har du lyst på en brus?")

ønsketSvar = "ja"
annetSvar = "nei"

#her er programet for hva kan kommer til å stå på terminale avhengig
#av svaret på spørsmålet overfor
if Spørsmål == ønsketSvar:
    print("Her har du en brus!")
elif Spørsmål == annetSvar:
    print("Den er grei")
else:
    print ("Det forstod jeg ikke helt.")
