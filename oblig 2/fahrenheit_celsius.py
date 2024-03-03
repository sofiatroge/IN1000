"""
Ned skrives det ut varabiele temperaturFahrenheit inn i settning under, og
deretter regnes det ut varabielen temperaturCelsius ved å bruke
temperaturFahrenheit varabiel og det skrives ut i settningen som følger.
"""
temperaturFahrenheit = 77
print(f"Temperaturen ligger på {temperaturFahrenheit} grad Fahrenheit")

temperaturCelsius = ((temperaturFahrenheit) - 32)*(5/9)
print(f"Temperatu ligger på {temperaturCelsius} grad Celsius")

"""
Her nede ser man en definisjon for temperaturCelsius hvor brukern skriver inn en
temperatur i Fahrenheit som blir omgjort til Celsius.
"""
def temperaturCelsius():
    gradFahrenheit = input("Oppgi temperatur i Fahrenheit:")
    gradF = int(gradFahrenheit)

    print("Temperaturen ligger på", (gradF - 32)*(5/9),"grad Celsius")

temperaturCelsius()
