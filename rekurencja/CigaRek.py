def CigaRek(n):
    if n == 1:
        return 1
    return 3 * CigaRek(n-1)

n = int(input("Podaj liczbę n (większą lub równą 1): "))
if n < 1:
    print("Liczba n musi być większa lub równa 1.")
else:
    wynik = CigaRek(n)
    print(f"Wynik funkcji CigaRek({n}) = {wynik}")