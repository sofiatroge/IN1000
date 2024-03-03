#det første er å definere klassen Hund
class Hund:
    #nest steg instansierer objektet
    def __init__(self, alder, vekt):
        self._alder = alder
        self._vekt = vekt
        self._metthet = 10
    #en metode for å hente vekten
    def hentVekt(self):
        return self._vekt
    #en metode for å hente alderen
    def hentAlder(self):
        return self._alder
    #en metode for å springe
    def spring(self):
        #nest er om mettheten til hunden er under 5
        if self._metthet < 5:
            #hunden hunden går 1 ned i vekt
            self._vekt -= 1
        #hunden går uansett ned 1 i metthet
        self._metthet -= 1
    #en metode for å spise
    def spis(self, heltall):
        #denne øker mettheten med heltall
        self._metthet += heltall
