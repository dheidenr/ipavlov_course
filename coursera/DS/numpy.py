import numpy
import numpy as np


f = numpy.arange(1, 2, 0.3, dtype=float)
f1 = numpy.arange(1, 2, 0.3, dtype=float)
c = numpy.array([False, False, True])
b = numpy.array([1, 2, 3, 4, 5], dtype=float)


numpy.dot(f, f1) / numpy.linalg.norm(f) / numpy.linalg.norm(f1)

print(f, c, b, f.dot(f1), f * f1, numpy.dot(f, f1))
print(numpy.dot(f, f1) / numpy.linalg.norm(f) / numpy.linalg.norm(f1))
# b = numpy.array(1, 2, 3, 4, 5, dtype=float)


a = numpy.array([8, 10, -1, 0, 0])
print(a.reshape((1, 5)))
a = numpy.array([8, 10, -1, 0, 0])
print(a.reshape((5, 1)))
a = numpy.array([8, 10, -1, 0, 0])
print(a[numpy.newaxis, :])
a = numpy.array([8, 10, -1, 0, 0])
print(a[:, numpy.newaxis])

# c = np.eye((4, 5))
d = np.ones((10, 10))
b = np.eye(2, 3)
e = np.arange(1, 13, 2).reshape((3, 2))
# a = np.array([4, 3, 2], [2, 9, 1], [3, 1, 9])
a = np.eye(4, 5)
print('итог:', a[[0, 3], [1, 3]])

print(np.inv())
