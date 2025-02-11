def czy_palindrom(kodon):
    return kodon == kodon[::-1]

def sprawdz_kodony():
    kodony_fenyloalaniny = ["TTT", "TTC"]
    kodony_cysteiny = ["TGT", "TGC"]

    print("Fenyloalanina:")
    for kodon in kodony_fenyloalaniny:
        if czy_palindrom(kodon):
            print(f"Kodon {kodon} jest palindromem.")
        else:
            print(f"Kodon {kodon} nie jest palindromem.")

    print("\nCysteina:")
    for kodon in kodony_cysteiny:
        if czy_palindrom(kodon):
            print(f"Kodon {kodon} jest palindromem.")
        else:
            print(f"Kodon {kodon} nie jest palindromem.")

sprawdz_kodony()

kodon = input("Podaj kodon: ").upper()
if czy_palindrom(kodon):
    print(f"Kodon {kodon} jest palindromem.")
else:
    print(f"Kodon {kodon} nie jest palindromem.")
