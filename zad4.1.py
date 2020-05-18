plik = open("podzielne.txt","w+")

for liczba in range(21):
    if liczba % 4 == 0:
        lista = [liczba]
        plik.writelines(str(lista))
        print(lista)



