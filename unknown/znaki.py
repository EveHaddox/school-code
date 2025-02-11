znak = "Ѐ"
kod = ord(znak)
kod2 = ord("ӿ")

licznik = 0

while kod <= kod2:
    print(znak, end=" ")
    licznik += 1
    if licznik % 5 == 0:
        print()
    kod += 1
    znak = chr(kod)

print()
