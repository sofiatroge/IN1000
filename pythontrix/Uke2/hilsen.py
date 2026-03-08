# a) Skriv et program som ber brukeren om å skrive inn navnet sitt og lagrer svaret i en variabel kalt navn.
navn = input("Skriv navnet ditt her: ")
# b) Skriv en prosedyre si_hei() som skriver ut "hei"
def si_hei():
    print ("hei")

# c) Kall prosedyren si_hei() tre ganger, og etterpå skriv ut brukerens navn
si_hei()
si_hei()
si_hei()
print (navn)


# Output: 
# Skriv navnet ditt her: Sofia
# hei
# hei
# hei
# Sofia