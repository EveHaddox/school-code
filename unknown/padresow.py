ok = "hasło wysłane na email: "
blad = "niepoprawny adres email"

name = input("Podaj imię:\n")
surname = input("Podaj nazwisko:\n")

ad1 = name.lower() + "." + surname.lower() + "@gmail.com"
print("Wygenerowany adres e-mail: " + ad1)

ad2 = input("Powtórz adres e-mail:\n")

if ad1 == ad2:
    print(ok + ad1) 
else:
    print(blad)
