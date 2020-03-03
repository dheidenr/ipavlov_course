import numpy as np

print('Hello iPavlov')

a = np.array(
    [
        [1, 3],
        [3, 4],
        [5, 6],
        [7, 8]
    ]
)

b = np.array(
    [
        [0, 0],
        [0, 1]
    ]
)

print(np.dot(a, b))

b = np.arange(9, -1, -1)
print('new argsorted b: ', np.argsort(b))
print('original b:      ', b)
b.sort()
print('sorted b:        ', np.sort(b))
