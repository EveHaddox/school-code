NOMINALY = (50000, 20000, 10000, 5000, 2000, 1000, 500, 200, 100, 50, 20, 10, 5, 2, 1)

def WydajReszte(reszta):

    i = 0

    while reszta > 0:

        if reszta >= NOMINALY[i]:

            print(NOMINALY[i] / 100)

            reszta = reszta - NOMINALY[i]

        else:

            i += 1


reszta_zlote = int(input("Podaj liczbę złotych reszty: "))
reszta_grosze = int(input("Podaj liczbę groszy reszty: "))


WydajReszte(reszta_zlote * 100 + reszta_grosze) 