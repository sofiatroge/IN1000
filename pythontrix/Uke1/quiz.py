# I denne oppgaven skal du utvikle en quiz.

# Skriv et program som stiller et spørsmål til brukeren og tar inn et 
# svar på ett eller flere spørsmål. Om svaret er riktig, 
# skal programmet skrive ut "Helt rett!". Hvis svaret er feil, skal programmet 
# skrive ut "Beklager, svaret var " etterfulgt av det riktige svaret. Lagre brukerens svar som en tekststreng i en variabel.

spm_svar = input ("Hva er hovedstaden til Peru? ")
rett_svar = "Lima"

if spm_svar == rett_svar:
    print ("Helt rett!")
else:
    print ("Beklager, svaret var", rett_svar)