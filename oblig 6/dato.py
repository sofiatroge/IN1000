#det første er å definere klassen Dato
class Dato:
    #neste steg er skrive instansierings objektet
    def __init__(self, nyDag, nyMaaned, nyttAar):
        self._dag= nyDag
        self._maaned=nyMaaned
        self._aar=nyttAar
    #neste steg er en metode som leser av året for datoen, som vill si at den returneer året
    def lesAar(self):
        return self._aar
    #en metode som lager en brukervennlig streng av datoen
    def brukervennligStr(self):
        brukervennligStr = f"Datoen din er følgende {self._dag}. {self._maaned}.{self._aar}."
        return brukervennligStr
    #en metode som sjekker om datoen er en spesifikk dag i måneden og dermed
    # skriver ut True eller False
    def sjekkDag(self, spesifikkDag):
        return self._dag == spesifikkDag
