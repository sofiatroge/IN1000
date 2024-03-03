"""
Nede finner man en definisjon for funskjonen info, omdannet til en prosedyre,
hvor bukeren kan skrive inn et navn og deretter et bosted slik at der skrives ut
"Hei, (navnet som ble skrevet inn av bruker)! Du er fra (bosted som ble skrevet
inn). Programmet skal kjøres tre ganger, dermed kan man bruke prosedyren istenfor 
å skrive kodene flere ganger.
"""
def info():
    Navn = input("Skriv inn navn:")
    Bosted = input("Hvor kommer du fra?")

    print (f"Hei,{Navn}! Du er fra {Bosted}")
info()
info()
info()
