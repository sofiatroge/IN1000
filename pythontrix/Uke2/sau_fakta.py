# I denne oppgaven skal du printe ut 5 fakta om sauer i en prosedyre. Dette skal skje på 
# 5 forskjellige linjer. Gi prosedyren navnet skriv_ut_sauefakta.

# a) Skriv prosedyren som skriver ut faktaene.

# Forslag til sauefakta:

# Sauer er dumme dyr.
# Sauer er myke dyr.
# Sauer kan løfte 12 ganger sin egen vekt.
# Sauer lukter litt som geiter.
# Sauen er din venn.

def sau_fakta():
    print("Sauer er dumme dyr.\nSauer er myke dyr.\nSauer kan løfte 12 ganger sin egen vekt.\n" \
    "Sauer lukter litt som geiter.\nSauen er din venn.")

# b) Hvordan kan vi nå skrive ut følgende linjer effektivt?

# Sauer er dumme dyr.
# Sauer er myke dyr.
# Sauer kan løfte 12 ganger sin egen vekt.
# Sauer lukter litt som geiter.
# Sauen er din venn.
# *** En gang til! ***
# Sauer er dumme dyr.
# Sauer er myke dyr.
# Sauer kan løfte 12 ganger sin egen vekt.
# Sauer lukter litt som geiter.
# Sauen er din venn.

sau_fakta()
print("*** En gang til! ***")
sau_fakta()