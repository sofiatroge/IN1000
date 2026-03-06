# a) Skriv et program som ber brukeren om å skrive inn favorittfargen sin 
#   i terminalen og lagre svaret i en variabel farge.

farge = input("Hva er din favorittfarge? ")

# b) Utvid programmet slik at hvis brukeren svarer "gul", "oransje" eller "grønn", 
#   skal programmet skrive ut navnet på en frukt som har den fargen.

if farge == "gul":
    print("Banan")
elif farge == "oransje":
    print("Mango")
elif farge == "grønn":
    print ("Avokado")
