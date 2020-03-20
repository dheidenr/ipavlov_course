import numpy as np
import itertools

def encode(a):
    elements = np.array([])
    amount = np.array([])
    prev = a[0]
    amt = 0
    for element in a:
        if element == prev:
            amt += 1
            continue
        else:
            elements = np.append(elements, prev)
            amount = np.append(amount, amt)
            amt = 1
            prev = element
    elements = np.append(elements, prev)
    amount = np.append(amount, amt)
    return elements, amount


def optimal_encode(a):
    return (np.array([x for x, y in itertools.groupby(a)]),
            np.array([len(list(y)) for x, y in itertools.groupby(a)]))


a = np.array([1, 2, 2, 3, 3, 1, 1, 5, 5, 2, 3, 3])
print(encode(a))
print(optimal_encode(a))


