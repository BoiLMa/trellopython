print("stotter sim")
while True:
    a = input("Antwoord hier ")
    userlist = a.split()
    for x in userlist:
        if len(x) > 2:
            print(x[0:2] + "...", x[0:2]+ "..." ,x )
        else:
            print(x)

