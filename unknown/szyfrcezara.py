# zapisz kod z str 123

def Cezar(klucz,tekst):
    szyfrogram =''
    dl = len(tekst)

    for i in range(0,dl):
        if tekst[i]==' ':
            kod=ord(' ')
        else:
            kod = ord(tekst[i]) + klucz
            if (kod > ord('Z')):
                kod = kod - 26
        szyfrogram = szyfrogram + chr(kod)
    return szyfrogram

jawny = input('Podaj tekst: ')
klucz = int(input('Podaj klucz szyfrowanie: '))

print('\nSzyfrogram:', Cezar(klucz, jawny))