szyfrogram = ""

jawny = input("podaj tekst\n")
key = int(input("\npodaj klucz\n"))

dl = len(jawny)

for i in range(0, key):
    for j in range(i, dl, key):
        szyfrogram = szyfrogram + jawny[j]

print("\nszyfrogram: " + szyfrogram)