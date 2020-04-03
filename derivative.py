#  6.2 Лекция: Производная, градиентная оптимизация.
import numpy as np
import matplotlib.pyplot as plt
import math
import sys


def f(x):
    return x**4 + 5*x**3 - 10*x


x = np.linspace(-5, 2, 100)
y = list(map(f, x))

plt.figure(figsize=(10, 7))
plt.plot(x, y)
plt.ylabel("Y")
plt.xlabel("X")
plt.scatter([-3.5518, -0.9439, 0.7457], [f(-3.5518), f(-0.9439), f(0.7457)], lw=5)

plt.show()


def f(x):
    return x**4


x = np.linspace(1, 15, 100)
y = list(map(f, x))

print(len(x))

plt.plot(x, y)
plt.ylabel("Y")
plt.xlabel("X")
plt.show()


# Нахождение экстремума
def f(x):
    return 4*x**2 - 3*x + 5


def f(x):
    return abs(x)


def plot_function(f):
    plt.figure(figsize=(10, 7))
    x = np.linspace(-1, 1, 1000)
    y = list(map(f, x))

    plt.plot(x, y)
    plt.ylabel("Y")
    plt.xlabel("X")
    plt.scatter([3 / 8], [f(3 / 8)], lw=5)
    plt.show()


plot_function(f)


print((math.exp(2.718)) * (math.log(2.718) + 1))

print(sys.float_info.epsilon)
print(math.log(2)/1)

