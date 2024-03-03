from sang import Sang

class Spilleliste:
    def __init__(self, listenavn):
        self._sanger = []
        self._navn = listenavn

    #i neste steg lages en metode som leser inn data fra fil i formatet:
    # tittel;artist per linje, og legger dem til i spillelisten
    def lesFraFil(self, fil):
        for linje in open(fil):
            alleData = linje.strip().split(";")
            artist = alleData[0]
            tittel = alleData[1]
            self._sanger.append(Sang(artist, tittel))
            
    #en metode som legger til en oppgitt sangobjekt i spillelisten
    def leggTilSang(self, nySang):
        self._sanger.append(nySang)
    #en metode som fjerner en oppgitt sangobjekt i spillelisten
    def fjernSang(self, sang):
        self._sanger.remove(sang)
    #en metode som spiller av den oppgitte sangobjekt
    def spillSang(self, sang):
        sang.spill()
    #en metode som spiller av alle sangene som ligger i spillelisten
    def spillAlle(self):
        for x in self._sanger:
            x.spill()
    #en metode som returnerer første sangobjekt i spillelisten som har en tittel
    def finnSang(self, tittel):
        for x in self._sanger:
            if x.sjekkTittel(tittel) == True:
                return x
        return None
    #en metode som returnerer en liste med sangene i spillelisten som har en artist
    def hentArtistUtvalg(self, artistnavn):
        artistutvalg = []
        for x in self._sanger:
            if x.sjekkArtist(artistnavn):
                artistutvalg.append(x)
        return artistutvalg
