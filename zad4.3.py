with open('tekst', 'w') as file: 
    file.write('Tekst do zadanka') 

with open("tekst", "r") as file:
    for odczyt in file:
        print(odczyt)