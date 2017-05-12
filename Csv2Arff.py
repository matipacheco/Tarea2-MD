import re
import numpy

csv_file = open('groceries.csv', 'r')
arff_file = open('groceries.arff', 'w')
arff_file.write("@RELATION groceries\n\n")

row = 0
column = 0

order = {}
groceries = {}

for purchase in csv_file:

    for item in purchase.rstrip().split(','):

        if not item in groceries.keys():
            order[column] = item
            groceries[item] = [row]
            column += 1

        else:
            groceries[item].append(row)

    row += 1

matrix = ['?'] * row * column
matrix = numpy.array([matrix])
matrix = numpy.reshape(matrix, (row, column))

for index in order:
    item = order[index]
    arff_file.write("@ATTRIBUTE '" + item + "' {1}\n")

    for row in groceries[item]:
        matrix[row][index] = 1

arff_file.write("\n@DATA\n")

regex = '\[(.*?)\]'
pattern = re.compile(regex)

for row in matrix:
    str_row = str(list(row))
    arff_file.write(re.findall(pattern, str_row)[0].replace("\'", "") + "\n")

csv_file.close()
arff_file.close()