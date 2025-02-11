def FibRek(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    return FibRek(n-1) + FibRek(n-2)