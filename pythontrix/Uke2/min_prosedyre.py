# a) Lag en prosedyre, min_prosedyre, som skriver ut "Hei student!" til terminalen.
def min_prosedyre():
    print("Hei student!")

# b) Endre programmet slik at min_prosedyre også skriver ut "Velkommen til et nytt semester!" 
# på en annen linje.
    print("Velkommen til et nytt semester!")


# c) Lag en ny prosedyre, linjeskift, som skriver ut en tom linje.
def tom_linje():
    print()

# d) Kall på min_prosedyre to ganger. Mellom kallene skal du også kalle på prosedyren linjeskift, 
# slik at det blir et linjeskift mellom hilsenene.
min_prosedyre()
tom_linje()
min_prosedyre()