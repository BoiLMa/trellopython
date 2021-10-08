stutter = input("Typ een zin: ")
if len(set(stutter)) >= 3:
    print(stutter[0:3] + "..." + " " + stutter[0:3] + "..." + " " + stutter)