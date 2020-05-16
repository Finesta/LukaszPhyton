def lista(** itemki):
    if len(itemki) == 0:
        return 0
    else:
        suma = 0
        for ile in itemki.values():
            suma += ile
        return suma
 
print(lista())
print(lista(monsterki=44,papier=2,piwko=6,ćwiartka=3,chlebdladziecka=0.5))