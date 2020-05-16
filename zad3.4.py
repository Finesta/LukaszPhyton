import math

a = int(input("a= "))
b = int(input("b= "))
 
def funkcja(a,b):
    if a>0:
        print(f"y = {a}x + {b},a>0")
        return("funkcja rosnaca")
    elif a<0:
	    print(f"y = {a}x + {b},0>a")
	    return("funkcja malejąca")
    else:
	    print(f"y = {b}")
	    return("funkcja stala,a=0")
 
print(funkcja(a,b))
