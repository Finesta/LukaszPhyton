import sys
print("Podaj pierwsza liczbe: ")
a = sys.stdin.readline()
print("Podaj druga liczbe: ")
b = sys.stdin.readline()
a = int(a)
b = int(b)
c = a*b
print("Wynik mnozenia to: ")
sys.stdout.write(str(c))