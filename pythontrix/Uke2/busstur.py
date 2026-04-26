# Du skal skrive et program som sjekker om det er plass på en buss på en bussrute med tre stopp.

# Det er plass til inntil 30 passasjerer i bussen. For hvert stopp skal bruker taste inn hvor 
# mange passasjerer som venter på å gå på bussen. Dersom bussen er full, kan ingen gå på. Dersom 
# flere ønsker å gå på enn det er gjenværende plasser på bussen, får kun noen nye passasjerer plass.
#  Vi antar at alle passasjerer skal til endestasjonen, så vi behøver ikke ta høyde for at noen går 
# av bussen underveis.

# I tillegg skal programmet skrive ut antall personer som går ombord på bussen ved hvert stopp. 
# Om bussen er full, skal det skrives ut en beskjed og antall personer som må gå til fots. 
# Til slutt skal det skrives ut at bussen har kommet frem til endestasjonen med antall passasjerer.

# Under finner du et eksempel på hvordan kjøringen kan se ut:

# Stasjon 1! Hvor mange venter på bussen?
# > 14
# 14 personer går ombord i bussen.

# Stasjon 2! Hvor mange venter på bussen?
# > 13
# 13 personer går ombord i bussen.

# Stasjon 3! Hvor mange venter på bussen?
# > 5
# Bussen er full. 2 må gå til fots.

# Bussen er fremme med 30 personer ombord!

personer = 0

personer = int(input("Stasjon 1! Hvor mange venter på bussen? "))
if personer < 30:
    print(personer, "personer går ombord i bussen.")
else:
    print("Bussen er full,", (personer-30), "må gå til fots.")

stopp2 = int(input("Stasjon 2! Hvor mange venter på bussen? "))
personer += stopp2
if personer< 30:
    print(stopp2, "personer går ombord i bussen.")
else:
    print("Bussen er full,", (personer-30), "må gå til fots.")

stopp3 = int(input("Stasjon 3! Hvor mange venter på bussen? "))
personer += stopp3
if personer< 30:
    print(stopp3, "personer går ombord i bussen.")
else:
    print("Bussen er full,", (personer-30), "må gå til fots.")



print("Bussen er fremme med 30 personer ombord!")