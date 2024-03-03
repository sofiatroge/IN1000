#importerer klassen Sang
class Sang:
    #konstruktør som instansierer objektet
    def __init__(self,artist,tittel):
        self._tittel = tittel
        self._artist = artist
    #en metode som printer ut en melding som gjør oppmerksom om at et bestemt sang
    # spilles av og av hvem den er
    def spill(self):
        print(f"Spiller {self._tittel} av {self._artist}")

    #en metode som returnerer True om en av artistene til sangen gis som argument
    def sjekkArtist(self, navn):
        #hvert ord i navn sjekkes om den finnes i _artist, om det er tilfelle return True
        for x in navn.split(" "):
            if x in self._artist.split(" "):
                return True
        #om ingen ord gir True, return False
        return False
    #en metode som returnerer True dersom tittelen til sangen er brukt som argument
    def sjekkTittel(self, tittel):
        return tittel.lower() == self._tittel.lower():

    #neste metode returnerer True dersom både en av artistene til sangen og
    # tittelen til sangen blir angitt som argument
    def sjekkArtistOgTittel(self, artist, tittel):
        return self.sjekkTittel(tittel) and self.sjekkArtist(artist)
