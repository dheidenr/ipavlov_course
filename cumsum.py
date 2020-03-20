import numpy as np


def cumsum(A):
    return np.cumsum(A, axis=1)


a = np.array(
    [
        [3, 4, 5, 5],
        [1, 2, 7, 0],
        [3, 1, 1, 7],
        [5, 8, -10, 4]
    ]
)

print(cumsum(a))
