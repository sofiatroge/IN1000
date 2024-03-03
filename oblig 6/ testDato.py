#importerer klassen Dato
from dato import Dato
#neste steg definerer hovedprogrammet
def hovedprogram ():
    #så opprettes et objekt
    dato = Dato(12,11,1997)
    #etterpå skrives ut datoens år på terminalen
    print(dato.lesAar)
    #i neste steg skriver programmet ut "Loenningsdag" hvis dagen er 15
    #ellers skriver den ut "Ny maaned, nye muligheter" om dag er 1
    if dato.sjekkDag(15):
        print("Loenningsdag!")
    else:
        print("Ny maaned, nye muligheter")
    #så lagres datoen som en brukervennlig streng
    datoBrukervennlig = dato.brukervennligStr()
    #og deretter skriver programmet ut den brukervennlige strengen i terminalen
    print(datoBrukervennlig)

hovedprogram()
