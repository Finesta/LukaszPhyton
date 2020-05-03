import math

try:
    liczba = input("Podaj liczbę: ")
    liczba = int(liczba)
    if liczba < 0:
        raise ValueError
    else:
        print("Pierwiastek wynosi: ", math.sqrt(liczba))
except ValueError:
    print("Liczba miała być większa od 0.")

