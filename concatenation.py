import numpy as np


def transform(X, a=1):
    """
    param X: np.array[batch_size, n]
    """
    result = []
    string = []
    for row in X:
        for n in range(len(row)):
            if n % 2 == 0:
                string.append(row[n] ** 3)
            else:
                string.append(a)
        string = string[::-1]
        result.append(string)
        string = []
    return np.concatenate((X, np.array(result)), axis=1)


def optimal_transform(X, a=1):
    Y = np.copy(X)
    Y[:, 1::2] = a
    Y[:, 0::2] **= 3
    return np.hstack((X, Y[:, ::-1]))


x = np.array(
        [
            [1, 2, 3, 4, 5],
            [1, 2, 3, 4, 5]
        ]
)

a = 1

# print(np.array([n for row in x for n in row]))
# print(np.array([row for row in x]))


# result = x + np.array(result)
# print(x)
print(x)
print(transform(x, 666))
print(optimal_transform(x, 666))
print([[ 1, 2, 3, 4, 5, 125, 1, 27, 1, 1], [ 1, 2, 3, 4, 5, 125, 1, 27, 1, 1]])
# print(np.concatenate(np.array(result), x))

