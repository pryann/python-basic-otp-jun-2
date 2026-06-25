matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
]

print(matrix[0][2])

for row in matrix:
    for element in row:
        print(element)

my_matrix = []

for i in range(5):
    row = []
    for j in range(5):
        row.append(j)
    my_matrix.append(row)

print(my_matrix)
