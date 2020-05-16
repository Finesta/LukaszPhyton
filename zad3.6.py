import math
def okrag(a=0,b=0,x=2,y=2):
  promien = math.sqrt((x-a)**2 - (y-b)**2)
  return promien
 
print(okrag())
