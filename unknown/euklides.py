# Program znajdujący NWD metodą odejmowania
a = int(input("Podaj pierwszą liczbę: "))
b = int(input("Podaj drugą liczbę: "))

while a != b:
    if a > b:
        a = a - b
    else:
        b = b - a

print(f"NWD: {a}")
