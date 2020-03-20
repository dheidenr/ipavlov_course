import numpy as np


def dot_row_column(a, b, row, column, n):
    result = 0
    for i in range(n):
        result += a[row][i] * b[i][column]
    return result


def no_numpy_mult(first, second):
    string = []
    result = []
    for row in range(len(first)):
        for column in range(len(second[0])):
            string.append(
                dot_row_column(first, second, row, column, len(first[0])))
        result.append(string)
        string = []
    return result


def numpy_mult(first, second):
    result = np.dot(first, second)
    return result


a = [
    [1, 3],
    [3, 4],
    [5, 6],
    [7, 8]
]

b = [
    [0, 0],
    [0, 1],
]

# print(numpy_mult(np.array(a), np.array(b)))
print('a:', 'Количество сток:', len(a[0]), '\nКоличество столбцов', len(a))
print('b:', 'Количество сток:', len(b[0]), '\nКоличество столбцов', len(b))

# result = []
row_temp = []
sum = 0
row = 0
column = 0
n = 0


def dot_row_column(a, b, row, column, n):
    result = 0
    for i in range(n):
        result += a[row][i] * b[i][column]
    return result


temp_row = []
result = []
for row in range(len(a)):
    for column in range(len(b[0])):
        temp_row.append(dot_row_column(a, b, row, column, len(a[0])))
    result.append(temp_row)
    temp_row = []

# a[i][n] * b[n][k]


# print(result)
print(numpy_mult(np.array(a), np.array(b)))
print(no_numpy_mult(a, b))
print(a[0][0])
print(a[1][0])
