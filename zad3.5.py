a1 = int(input("a1= "))
a2 = int(input("a2= "))
b1 = int(input("b1= "))
b2 = int(input("b2= "))

def funkcja(a1,a2):
    if a1==a2:
        return("proste sa rownolegle,a1=a2")
    elif a1*a2==-1:
        return("proste sa prostopadle,a1*a2=0")
    else:
        return("proste nie sa ani rownolegle,ani prostopadle")


print("y1 = ",a1,"x + ",b1)
print("y2 = ",a2,"x + ",b2)
print(funkcja(a1,a2))
