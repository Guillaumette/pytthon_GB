"""
Напишите функцию для транспонирования матрицы transposed_matrix,
которая принимает в аргументы matrix, и возвращает транспонированную матрицу.
"""


def transpose(matrix):
    transposed_matrix = []
    for j in range(len(matrix[0])):
        row = []
        for i in range(len(matrix)):
            row.append(matrix[i][j])
        transposed_matrix.append(row)
    return transposed_matrix


my_matrix = [[1, 2, 3],
          [4, 5, 6],
          [7, 8, 9]]
transposed = transpose(my_matrix)
print(transposed)
