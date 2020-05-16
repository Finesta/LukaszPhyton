a1 = int(input("pierwszy wyraz = "))
r = int(input("o ile ma sie zwiekszac = "))
ile = int(input("ile elementów ma sie sumowac =  "))


def funkcja(a1=1, r=1, ile=10):
  XD = ((2*a1+(ile-1)*r)/2)*ile
  return XD
 
print("suma okreslonrgo ciagu = ", funkcja())
print("suma ciągu podanego przez uzytkownika = ", funkcja(a1,r,ile))
