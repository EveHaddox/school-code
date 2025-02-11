NOMINALY = (5, 2, 1, 0.50, 0.20, 0.10, 0.05, 0.02, 0.01)
N = len(NOMINALY)
def WydajReszte(reszta):
   i = 0
   while reszta > 0 and i < N:
       if reszta >= NOMINALY[i]:
           print(NOMINALY[i])
           reszta = round(reszta - NOMINALY[i], 2)  # zaokrąglenie do 2 miejsc po przecinku
       else:
           i += 1
reszta = float(input("Podaj kwotę reszty: "))
WydajReszte(reszta)