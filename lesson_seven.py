import numpy as np
import inspect
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D


def numerical_derivative_2d(func, epsilon=0.00001):
    """
    Функция для приближённого вычисления градиента функции двух переменных.
    :param func: np.ndarray -> float — произвольная дифференцируемая функция
    :param epsilon: float — максимальная величина приращения по осям
    :return: другая функция, которая приближённо вычисляет градиент в точке
    """

    def grad_func(x):
        """
        :param x: np.ndarray — точка, в которой нужно вычислить производную
        :return: приближённое значение производной в этой точке
        """
        # return (func(x + epsilon) - func(x)) / epsilon
        x0 = x[0]
        x1 = x[1]
        x0 = (func([x[0] + epsilon, x[1]]) - func(x)) / epsilon
        x1 = (func([x[0], x[1] + epsilon]) - func(x)) / epsilon
        return [x0, x1]
        # YOUR CODE

    return grad_func


def draw(coordinates, func, low, high):
    plt.figure(figsize=(10, 7))
    x = np.linspace(low, high, 1000)
    y = [func([xn, xn]) for xn in x]
    plt.plot(x, y)
    plt.plot([x[0] for x in coordinates], [func(x) for x in coordinates])
    plt.plot([x[1] for x in coordinates], [func(x) for x in coordinates])
    plt.scatter([x[0] for x in coordinates], [func(x) for x in coordinates])
    plt.scatter([x[1] for x in coordinates], [func(x) for x in coordinates])
    plt.ylabel("Y")
    plt.xlabel("X")
    plt.show()


def draw_3d(x2, func):
    x = [x[0] for x in x2]
    y = [x[1] for x in x2]
    z = [func(x) for x in x2]
    line = np.linspace(-5.0, 5.0, 100)
    fig = plt.figure(figsize=(10, 7))
    ax = fig.add_subplot(111, projection='3d')
    ax.plot(x, y, z)
    i = np.arange(-1, 1, 0.01)
    x, y = np.meshgrid(i, i)
    print(x, y)
    z = [func(x, y) for x, y in zip(x, y)]
    ax.plot(x, y, z)
    ax.scatter(x, y, z)
    plt.show()


def grad_descent_2d(func, low=-5.0, high=5.0, callback=None):
    """
    Реализация градиентного спуска для функций двух переменных
    с несколькими локальным минимумами, но известной квадратной окрестностью
    глобального минимума. Все тесты будут иметь такую природу.

    Обратите внимание, что здесь градиент функции не дан.
    Его нужно вычислять приближённо.

    :param func: np.ndarray -> float — функция
    :param low: левая граница интервала по каждой из осей
    :param high: правая граница интервала по каждой из осей
    """
    if low is None:
        low = -1000
    if high is None:
        high = 1000

    best_estimates = []

    # def grad_descent_v1(func, deriv, start=None):
    #     if start is None:
    #         np.random.seed(179)
    #         start = np.random.randn()
    #     estimate = start
    #
    #
    #     def sign(number):
    #         return 1.0 if number >= 0 else -1.0
    #
    #     def regression(length, estimate, step):
    #         first = estimate
    #         sign_f = sign(first)
    #         for _ in range(length):
    #             if sign(deriv(estimate)) == sign_f:
    #                 estimate = estimate - sign(first) * step
    #             else:
    #                 return estimate
    #         return estimate
    #
    #     step = 2.0
    #     for _ in range(100):
    #         estimate = regression(100, estimate, step)
    #         step /= 1.0005
    #     return estimate
    #
    # estimates = np.linspace(low + 0.000001, high + 1, 300)
    # best_estimate = grad_descent_v1(func, numerical_derivative_2d, start=estimates[0])
    # best_estimates.append(best_estimate)
    # for x in estimates:
    #     temp_estimate = grad_descent_v1(func, numerical_derivative_2d, start=x)
    #     if func(temp_estimate) < func(best_estimate):
    #         best_estimate = temp_estimate
    #         best_estimates.append(temp_estimate)

    # f = open('logs.txt', 'w')

    # def sign(number):
    #     return 1.0 if number >= 0 else -1.0

    epsilon = 0.001
    epsilon2 = 0.001
    assumption = 0.01
    max_steps = 4000
    ordinates = []
    deriv = numerical_derivative_2d(func, epsilon)
    # x = [high, high]
    # steps = 0
    #
    # print(func(x), x[0], x[1])
    linex0 = np.linspace(low, high, 5)
    linex1 = np.linspace(low, high, 5)

    mesh = np.meshgrid(linex0, linex1)

    # for x in linex0:
    #     line.append([np.random.uniform(low, high), np.random.uniform(low, high)])
    # print(np.meshgrid(linex, linex))
    # mesh = np.meshgrid(linex, linex)
    min = [low, low]
    x = [np.array(mesh[0]).flatten()[0], np.array(mesh[0]).flatten()[1]]
    # print(mesh)
    for x[0], x[1] in zip(np.array(mesh[0]).flatten(), np.array(mesh[1]).flatten()):
        steps = 0
        # print('x=', x)
        while assumption < abs(deriv(x)[0]) and assumption < abs(deriv(x)[1]) and x[0] <= high and x[1] <= high and x[0] >= low and x[1] >= low and steps <= max_steps:
            x[0] = x[0] - epsilon2 * deriv(x)[0]
            x[1] = x[1] - epsilon2 * deriv(x)[1]
            if func(x) > func(min):
                min[0] = x[0]
                min[1] = x[1]
                ordinates.append(x)
            d = func(x)
            steps += 1
            # f.write('x0: ' + str(x[0]) + '  \ty1: ' + str(x[1]) + str(
            #     func(x)) + '  \tstep:' + str(steps) + '\n')
        # print(steps)
    # print(min[0], min[1], func(min), deriv(min))
    # f.close()
    # draw_3d(ordinates, func)
    draw(ordinates, func, low, high)
    return np.array(min)


result = []
for _ in range(1):
    print('step:', _)
    result.append(grad_descent_2d(lambda x: (-1 / ((x[0] - 1) ** 2 + (x[1] - 1.5) ** 2 + 1)
                                 * np.cos(
            2 * (x[0] - 1) ** 2 + 2 * (x[1] - 1.5) ** 2)
                                 ), low=1.0, high=2.0))


func = lambda x: (-1 / ((x[0] - 1) ** 2 + (x[1] - 1.5) ** 2 + 1)
                                 * np.cos(
            2 * (x[0] - 1) ** 2 + 2 * (x[1] - 1.5) ** 2)
                                 )
minimum = min(result, key= lambda x: func(x))
print('min:', minimum,'func(min):', func(minimum))



    # print(grad_descent_2d(lambda x: (-1 / ((x[0] - 1) ** 2 + (x[1] - 1.5) ** 2 + 1)
    #                              * np.cos(
    #         2 * (x[0] - 1) ** 2 + 2 * (x[1] - 1.5) ** 2)
    #                              ), low=1.0, high=2.0))

# print ('{},{}, low={}, high={}'.format(inspect.getsource(func), inspect.getsource(deriv), low, high))

# np.random.seed(123)




# x = np.cos(u)*np.sin(v)
# y = np.sin(u)*np.sin(v)
# z = np.cos(v)
# fig = plt.figure()
# ax = fig.add_subplot(111, projection='3d')
# ax.plot_wireframe(x, y, z)
# ax.legend()
# plt.show()


# print(np.random.uniform(-5.0, 5.0))


x = np.array([1, 2, 3])
y = np.array([4, 5, 6])

for i in y:
    x0 = i
    for d in x:
        x1 = d
        print(x1, end=' ')
        print(x0)

mesh = np.meshgrid(x, y)
print('x=', x)
print('y=', y)
print('mesh')
print(mesh)
print('meshgrid[0]=', mesh[0])
print('meshgrid[1]=', mesh[1])

for x, y in zip(np.array(mesh[0]).flatten(), np.array(mesh[1]).flatten()):
     print('x=', x, 'y=', y)

print('combo', np.array(mesh[0]).flatten())
print('combo', np.array(mesh[1]).flatten())

linex0 = np.linspace(-5.0, 5.0, 4)
linex1 = np.linspace(-5.0, 5.0, 4)

mesh = np.meshgrid(linex0, linex1)
print(linex0)
print(linex1)
print(mesh)
print(mesh[1][1][1])



