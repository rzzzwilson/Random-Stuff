row = 5

column = 5

matrix = [[0]*column for i in range(row)]

for row in matrix:
    for column in row:
        print(column,end = " ")
    print()

print()
matrix[1][2] = 1

for row in matrix:
    for column in row:
        print(column,end = " ")
    print()
