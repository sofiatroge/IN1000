# Lag et programm som regner ut totalprisen for en bruker etter å ha vært på handletur. 
# De varene det er mulig å kjøpe er brød, melk, ost og yoghurt.

# Prisene er som følger:
# Brød: 20 kr.
# Melk: 15 kr.
# Ost: 40 kr.
# Yoghurt: 12 kr.

# Eksempel på interaksjon med programmet:

# Hei! Velkommen til IFI-butikken.
# Hvor mange brød vil du ha?
# > 2
# Hvor mange melk vil du ha?
# > 1
# Hvor mange ost vil du ha?
# > 1
# Hvor mange yoghurt vil du ha?
# > 3
# Du skal betale: 131 kr.

print("Hei! Velkommen til IFI-butikken.")
brød = int(input("Hvor mange brød vil du ha? "))
melk = int(input("Hvor mange melk vil du ha? "))
ost = int(input("Hvor mange ost vil du ha? "))
yoghurt = int(input("Hvor mange yoghurt vil du ha? "))
print("Du skal betale: ", (brød * 20) + (melk * 15) + (ost * 40) + (yoghurt * 12), "kr")
