def Cezar(k, txt):
    szyfrogram = ""
    dl = len(txt)

    for i in range(0, dl):
        if txt[i] == " ":
            kod = ord(" ")
        else:
            kod = ord(txt[i]) + k
            if (kod > ord("Z")):
                kod = kod - 26
        szyfrogram = szyfrogram + chr(kod)

    return szyfrogram

jawny = input("podaj txt\n")
k = int(input("\nPodaj Klucz\n"))

print("\n Szyfr:", Cezar(k, jawny))