#importerer klassen Motorsykkel
from motorsykkel import Motorsykkel
#neste steg definerer hovedprogrammet
def hovedprogram():
    #så oppretter tre ulike motorsykkel-objekter
    førsteSykkel= Motorsykkel("BMW","BS9264", 1550 )
    andreSykkel= Motorsykkel("Kawasaki","BK2492", 1400)
    tredjeSykkel= Motorsykkel("Harley Davidson","BI6725", 960 )
    #da skrives de tre objektene ut
    førsteSykkel.skrivUt()
    andreSykkel.skrivUt()
    tredjeSykkel.skrivUt()
    #så øker km på første sykkel med 10
    førsteSykkel.kjor(10)
    #skriver ut første sykkel
    førsteSykkel.skrivUt()

#tilslutt kaller man på hovedprogrammet
hovedprogram()
