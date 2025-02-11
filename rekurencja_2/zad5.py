def NWDRek(a, b):
    if b % a == 0:
        return a 
    return NWDRek(b % a,a)