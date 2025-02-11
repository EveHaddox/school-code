def szukaj_wzorca(tekst, wzorzec):
    wzorzec = wzorzec.upper()
    pozycje = []
    
    for i in range(len(tekst) - len(wzorzec) + 1):
        if tekst[i:i+len(wzorzec)].upper() == wzorzec:
            pozycje.append(i)
    
    return pozycje

tekst = "Bohater bożyszcze Bolka i Lolka"
wzorzec = input("Podaj wzorzec do wyszukania: ")
pozycje_wzorcow = szukaj_wzorca(tekst, wzorzec)

print(f"Wzorzec '{wzorzec}' znaleziono na pozycjach: {pozycje_wzorcow}")
