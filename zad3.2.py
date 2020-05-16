import numpy
 
matrix = numpy.random.randint(0,5, size=(4,4))
list = [x for x in matrix.diagonal()]
print(matrix)
print(list)
