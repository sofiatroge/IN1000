#programet nedefor skriver ut "Hei Student" i terminalen og oppfordrer brukeren
#rett etterpå til å skrive sitt egent navn, slik at terminalen hilser brukeren
print ("Hei Student")

navn = input ("Skriv navnet ditt:")
print (f"Hei, {navn}")

#programmet nedenfor her derimot beregner en differens mellom to heltall,
#ved å først vise begge tallene og etterpå hva differansen mellom de er
år = 2021
FøÅr = 2002
Dif = år - FøÅr
print (år)
print (FøÅr)
print (f"Differanse: {Dif}")

# I dette programmet her er det derimot ønsket at brukeren svarer på spørsmålet
#slik at terminalen først printer ut begge navne sammen
#og deretter med en "og" mellom dem
annetNavn = input ("Hva heter din bestevenn?")
Sammen = navn + annetNavn
print(f"{Sammen}")

Sammen = (f"{navn} og {annetNavn}")
print(f"{Sammen}")
