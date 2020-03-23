import numpy as np


def no_numpy_scalar(v1, v2):
    result = 0
    for i, j in zip(v1, v2):
        result += i*j
    return result


def numpy_scalar(v1, v2):
    result = np.dot(v1, v2)
    return result


def optimal_no_numpy_scalar(v1, v2):
    return sum(x * y for x, y in zip(v1, v2))


v1 = [3, 4, 5]
v2 = [-1, 0.4, 2]
print(numpy_scalar(np.array(v1, float), np.array(v2, float)))
print(numpy_scalar(np.array(v1), np.array(v2)))
print(no_numpy_scalar(v1, v2))

