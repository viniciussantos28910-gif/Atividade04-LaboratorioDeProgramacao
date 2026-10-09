import numpy
import random
list = []

for i in range(3):
    row = []
    for j in range(3):
        row.append(random.randint(-99, 99))
    list.append(row)

matrix = numpy.array(list)

print(len(matrix[matrix >= 0]))