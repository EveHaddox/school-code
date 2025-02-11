def szyfruj(tekst):
    return tekst[::-1]

def deszyfruj(szyfrogram):
    return szyfrogram[::-1]

tekst = input("Podaj tekst do zaszyfrowania: ")
szyfrogram = szyfruj(tekst)
print("Szyfrogram:", szyfrogram)

print("Odszyfrowany tekst:", deszyfruj(szyfrogram))
