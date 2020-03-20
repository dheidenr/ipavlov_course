import numpy as np


def diag_2k(a):
    return sum((sum(i) if sum(i) % 2 == 0 else 0) for i in a * np.eye(len(a)))


# def optimal_diag_2k(a):
#     diag = a.diagonal()
#     return np.sum(diag[diag % 2 == 0])


def optimal_diag_2k(a):
    return sum(x for x in a.diagonal() if x % 2 == 0)

a = np.array(
    [
        [3, 4, 5, 5],
        [1, 2, 7, 0],
        [3, 1, 1, 7],
        [5, 8, -10, 4]
    ]
)
b = np.eye(len(a))
print(len(a))
print(np.eye(4))
print(a * b)

print(diag_2k(a))
print(optimal_diag_2k(a))
