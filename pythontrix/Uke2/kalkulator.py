# a) Skriv en prosedyre kalkulator(), som ber brukeren å taste inn et tall, en operasjon 
# (f.eks. +, -, * eller /) og et annet tall. Prosedyren skal skrive ut hvilken beregning som 
# foretas og resultatet av beregningen. Her er et eksempel på hvordan en kjøring av programmet 
# kan se ut:

# Første tall: 4.5
# Operasjon: +
# Andre tall: 7
# 4.5 + 7.0 = 11.5

def kalkulator():
    tall = float(input("Skriv in et tall: "))
    operasjon = input("Skriv in et operasjon (f.eks. +, -, * eller /): ")
    tall2 = float(input("Skriv in et annen tall: "))
    if operasjon == "+":
        tall3 = tall + tall2
        print(tall, operasjon, tall2, "=", tall3)
    elif operasjon == "-":
        tall3 = tall - tall2
        print(tall, operasjon, tall2, "=", tall3)
    elif operasjon == "*":
        tall3 = tall * tall2
        print(tall, operasjon, tall2, "=", tall3)
    elif operasjon == "/":
        tall3 = tall / tall2
        print(tall, operasjon, tall2, "=", tall3)
  
# b) Utvid programmet, slik at det skrives ut en advarsel hvis brukeren taster inn en ulovlig 
# operasjon.
    else:
        print("Operasjoenen som er tastet inn er ulovlig")

    
kalkulator()