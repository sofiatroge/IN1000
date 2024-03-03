#det første er å definere klassen Motorsykkel
class Motorsykkel:
    #nest steg instansierer objektet
    def __init__ (self,merke,registreringsnummer,km):
        self._merke = merke
        self._registreringsnummer = registreringsnummer
        self._km = km
    #en metode som øker km
    def kjor(self,km):
        self._km += km
    #en metode som henter km
    def hentKilometerstand(self):
        return self._km
    #en metode som skriver ut merke, registreringsnummer og km i terminalen
    def skrivUt(self):
        print(f"Merke:{self._merke}")
        print(f"Registreringsnummer: {self._registreringsnummer} ")
        print(f"Kilometeravstand: {self._km}")
