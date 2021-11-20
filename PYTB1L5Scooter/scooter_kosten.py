verzekering_per_maand = 23
benzine_kosten_per_liter = 1.54
liter_per_kilometer = float(0.2)

def bereken_maandkosten():
    maandkosten = (km_per_maand * liter_per_kilometer * benzine_kosten_per_liter) + verzekering_per_maand
    print("€" + str(maandkosten))
     

km_per_maand = ""

while not isinstance(km_per_maand, float):

    try:
        km_per_maand = input("hoeveel km per maand rij je: ")

        km_per_maand = float(km_per_maand)

        bereken_maandkosten()

    except:
        print(km_per_maand + " is geen getal")
