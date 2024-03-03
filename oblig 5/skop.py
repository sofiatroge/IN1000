
"""
Første ting som skjer er at funksjonen defineres som minFunksjon og deretter
defineres det prosedyren hovedprogram. Så kalles det på hovedprogram, der inne
oppretters det en variabela med verdien 42 og en variabelb med verdien 0. Da skrives
varabielen b (verdien 0) ut. I neste steg for variabelen b tilordnet a, som
fører til at b for verdien til variabelen a, det vil si 42. Etterpå kaller man
funksjonen minFunksjon, hvor det etterpå stater den for-løkke som bør kjører to
ganger, men blir stoppet når den kommer til linjen med 'b += a'.

Uanset før den krasjer skjer følgende: inn i minFunksjonopprettes det variblenen
c med verdien 2, som i neste linje blir printet ut i teminalen. Så legges blir 1
til varabielen c, slik at verdien til variabelen c blir 3. I neste steg for
varabielen b tilordnet verdien 10. Deretter forsøkes det å legge til verdien til
varabielen a til variabelen b, men siden variabelen a ikke er definert på innsiden
av funksjonen minFunksjon, så vil programmet krasjer når den kommer til linjen 'b += a'

Konklusjon etter å ha kjørt programmet i pythontutor:
Koden oppfører seg slik jeg hadde forventet med, siden den krasjer når den
kommer til 'b += a', da a ikke er definert.

"""
