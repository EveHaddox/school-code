def lam_czekolade(wiersze, kolumny):

    if wiersze == 1 and kolumny == 1:
        print("Kostka 1x1 gotowa.")
        return

    if wiersze >= kolumny:
        print(f"Łamię tabliczkę {wiersze}x{kolumny} poziomo na {wiersze // 2}x{kolumny} i {wiersze - wiersze // 2}x{kolumny}.")
        lam_czekolade(wiersze // 2, kolumny)
        lam_czekolade(wiersze - wiersze // 2, kolumny)
    else:
        print(f"Łamię tabliczkę {wiersze}x{kolumny} pionowo na {wiersze}x{kolumny // 2} i {wiersze}x{kolumny - kolumny // 2}.")
        lam_czekolade(wiersze, kolumny // 2)
        lam_czekolade(wiersze, kolumny - kolumny // 2)

lam_czekolade(4, 4)



16/2=8
8/2=4
8/2=4
4/2=2
4/2=2
4/2=2
4/2=2
2/2=1
2/2=1
2/2=1
2/2=1
2/2=1
2/2=1
2/2=1
2/2=1
2/2=1

odp.15
