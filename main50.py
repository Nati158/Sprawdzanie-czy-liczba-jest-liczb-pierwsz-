def czy_liczba_pierwsza(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

liczba = 17
if czy_liczba_pierwsza(liczba):
    print(liczba, "jest liczbą pierwszą.")
else:
    print(liczba, "nie jest liczbą pierwszą.")
