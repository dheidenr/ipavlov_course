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


def f(x):
    return x*x


def numerical_derivative_1d(func, epsilon=0.00001):

    def deriv_func(x):
        # YOUR CODE
        result = (func(x + epsilon) - func(x))/epsilon
        return result # YOUR CODE

    return deriv_func

deriv = numerical_derivative_1d(f, 0.00001)
print(deriv(1.0)) # 2  ОК. Производная  для х*х = 2*х = 2*1 = 2


def grad_descent_v1(func, deriv, start=None, callback=None):
    """
    Реализация градиентного спуска для функций с одним локальным минимумом,
    совпадающим с глобальным. Все тесты будут иметь такую природу.
    :param func: float -> float — функция
    :param deriv: float -> float — её производная
    :param start: float — начальная точка
    """
    if start is None:
        # Если точка не дана, сгенерируем случайную
        # из стандартного нормального распределения.
        # При таком подходе начальная точка может быть
        # любой, а не только из какого-то ограниченного диапазона
        np.random.seed(179)
        start = np.random.randn()

    estimate = start
    # callback(estimate, func(estimate))  # не забывайте логировать шаги!

    # YOUR CODE
    # r = p(estimate)
    print(deriv(estimate))
    while abs(deriv(estimate)) > 0.01:
        if deriv(estimate) <= 0:
            estimate = estimate + 0.001
        else:
            estimate = estimate - 0.001
        # estimate += 0.001 if deriv(estimate) <= 0 else -0.001
        # callback(estimate, func(estimate))  # не забывайте логировать шаги!
    print('estimate =', estimate)
    print('p =', round(deriv(estimate), 4))
    return estimate


def grad_descent_v1(func, deriv, start=None, callback=None):
    """
    Реализация градиентного спуска для функций с одним локальным минимумом,
    совпадающим с глобальным. Все тесты будут иметь такую природу.
    :param func: float -> float — функция
    :param deriv: float -> float — её производная
    :param start: float — начальная точка
    """
    if start is None:
        # Если точка не дана, сгенерируем случайную
        # из стандартного нормального распределения.
        # При таком подходе начальная точка может быть
        # любой, а не только из какого-то ограниченного диапазона
        # np.random.seed(179)
        start = np.random.randn()

    def sign(number):
        return 1.0 if number >= 0 else -1.0

    def regression(length, estimate, step):
        first = estimate
        sign_d = deriv(first)
        sign_f = sign(first)
        for i in range(length):
            if sign(deriv(estimate)) == sign_f:
                estimate = estimate - sign(first) * step
            else:
                return estimate
        return estimate





    def plot_function(f, x_points, y_points):
        plt.figure(figsize=(10, 7))
        x = np.linspace(-1, 1, 100)
        # y = list(map(f, x))
        y = [f(xn) for xn in x]

        plt.plot(x, y)
        plt.plot(x_points, y_points)
        plt.ylabel("Y")
        plt.xlabel("X")
        plt.scatter(x_points, y_points, lw=5)
        plt.show()

    if start > 1: start = 1
    estimate = start
    # # callback(estimate, func(estimate))  # не забывайте логировать шаги!
    #
    # # YOUR CODE
    # # r = p(estimate)
    #
    print('estimate =', estimate)
    print('deriv(estimate) =', deriv(estimate))
    x_points_func = []
    y_points_func = []
    x_points_deriv = []
    y_points_deriv = []
    # x = estimate
    # y = func(estimate)
    # dx = estimate
    # dy = func(x + dx) - func(x)
    # dy_prev = dy + 00000000000.1
    # for i in range(100):
    # # while abs(dy_prev > dy):
    #     dy_prev = dy
    #     dx = dx - dx / 2
    #     dy = (func(x + dx) - func(x))
    #     # print('dx =', dx)
    #     # print('dy =', dy)
    #     dfy = func(dx)
    #     print('dx =', dx)
    #     print('dy =', dy)
    #     print('dfy =', dfy)
    #     print('dy_prev =', dy_prev)
    #     x_points_func.append(dx)
    #     y_points_func.append(dy)
    # print('dx =', dx)
    # print('dy =', dy)
    # print('x_points', x_points_func, 'y_points', y_points_func)
    # plot_function(func, x_points_func, y_points_func)

    step = 2.0
    for i in range(100):
        estimate = regression(100, estimate, step)
        step /= 1.1
        x_points_func.append(estimate)
        y_points_func.append(func(estimate))
    print('dx =', estimate)
    print('dy =', func(estimate))
    print('x_points', x_points_func, 'y_points', y_points_func)
    plot_function(func, x_points_func, y_points_func)

    # step = 1
    # prev_d = deriv(estimate)
    # while abs(deriv(estimate)) > 0.01:
    #     if deriv(estimate) <= 0:
    #         estimate = estimate + 0.001
    #     else:
    #         estimate = estimate - 0.001
        # estimate += 0.001 if deriv(estimate) <= 0 else -0.001
        # callback(estimate, func(estimate))  # не забывайте логировать шаги!
    # print('estimate =', estimate)
    # print('p =', round(deriv(estimate), 4))
    # if dx < 9.353056857089389e-16:
    #     dx = 0.0
    return estimate


# print('grad_descent_v1:\n', grad_descent_v1(lambda x: x * x, lambda x: 2 * x))

print('grad_descent_v1:\n', grad_descent_v1(lambda x: math.log10(x ** 2) + 1, lambda x: 2 / x))

print('grad_descent_v1:\n', grad_descent_v1(
    lambda x:
    x ** 8 + x ** 7 + x ** 6 + x ** 5 + x ** 4 + x ** 3 + x ** 2 + x + 2,
    lambda x:
    8 * (x ** 7) + 7 * (x ** 6) + 6 * (x ** 5) + 5 * (x ** 4) + 4 * (x ** 3) +
    3 * (x ** 2) + 2 * (x ** 1) + x))

# "func" : lambda x: np.log((x + 1)**2 + 1),
#         "deriv" : lambda x: 2 * (x + 1) / (x**2 +1),
# print(11/2)

