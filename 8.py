liczby = input("Długość: ")
liczby = int(liczby)

a = []
c = 0

while c < liczby:
  c += 1
  b = input("Wczytaj liczbę: ")
  b = int(b)
  a.append(str(b))
print(a)