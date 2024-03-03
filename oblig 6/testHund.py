#det første er det å importere klassen Hund
from hund import Hund
#deretter skal man definere hovedprogrammet
def hovedprogram():
    #neste steg er å opprette et hundeobjekt
    doberman = Hund(5,40)
    #etterpå kalle på spring() og printe vekt
    doberman.spring()
    print(doberman.hentVekt())
    #så kalle på spis() og printe vekt
    doberman.spis(-7)
    print(doberman.hentVekt())
    #deretter kalle på spring() og printe vekt igjen
    doberman.spring()
    print(doberman.hentVekt())
    #så kaller man på spis() som printer vekt
    doberman.spis(3)
    print(doberman.hentVekt())
#tilslutt kaller man på hovedprogrammet
hovedprogram()
