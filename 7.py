liczby = input("Ile liczb wczytać ")
liczby = int(liczby)

print("Podaj liczby")
a = []
 
for i in range(0, liczby):
  b = input()
  b = int(b)
  b *= b
  a.append(str(b))
print(a)