a = int(input("Podaj pierwszą liczbę (a): "))
b = int(input("Podaj drugą liczbę (b): "))

while b != 0:
    c = a % b
    a = b
    b = c

print(f"NWD: {a}")
