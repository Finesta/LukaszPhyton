wysokosc = input("Wysokosc wiezy? ")
wysokosc = int(wysokosc) 
if wysokosc > 0 and wysokosc <= 10:
  for x in range(wysokosc):
    print("A"*(x+1))
else:
    print("Wpisana zła wartość.")
