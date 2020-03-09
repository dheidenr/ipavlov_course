import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import minimize
from scipy.integrate import quad, odeint
from scipy.special import erf

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

print('worked in windows 10')

np.arange(0, 50000000)

a = np.linspace(0, 8, 8)  # Начало конец и количество элементов которые нужны в масиве, функция сама определяет шаг

print(a)

b = np.eye(5)  # Создается единичная матрица

print('Единичная матрица', b, '\n\n\n\n')
#  Создадим матрицу 4 на 5 с -1 по диоганали и 0.5 все остальные элементы
print('Создадим матрицу 4 на 5 с -1 по диоганали и 0.5 все остальные элементы')
print(0.5 * np.ones((4, 5)) - 1.5 * np.eye(4, 5))

a = np.array([
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12]
])
print("слайс по оси матрицы")
# Выведет с нулевой по вторую не включительно строку
# и с первого по третий не включительно символ в каждой строке
print(a[0:2, 1:3])
print('world'[::-1])

print(a)
print('Изначальная размерность:', a.shape)  # Аналогично будет, если вместо np.newaxis поставить None
print('Вектор а с newaxis -> вектор-строка:\n', a[np.newaxis, :])  # Добавляем размерность
print('Полученная размерность:', a[np.newaxis, :].shape)  # Аналогично будет, если вместо np.newaxis поставить None

z = np.array([[1, 2], [3, 4]])
print(z)
print(z[[0, 1], [0, 1]])

a = np.arange(0, 4, 1)
print(a)

print('Маска True False True True:', a[[True, False, True, True]])
print('Маска a > 1:', a[a > 1])

z = np.eye(5)
print(z[::-1])  # Сверху вниз
print(z[:, ::-1])  # Слева направо

a = np.array([1, 2, 3])
b = np.array([2, 3, 4])
print(a, b)

print(np.dot(a, b))  # Скалярное умножение
print(a @ b)  # это метод matmul он отличается от dot в некоторых случаях разной формой ввиду получение матрицы как
#  стека состоящего из элементов то есть с конца в отличае от dot.

a = np.array([[1, 2], [3, 4]])
b = np.transpose(a)
c = a.T
print("Матрица:\n", a)
print("Транспонирование функцией:\n", b)
print("Транспонирование методом:\n", c)


def f(x):
    return x ** 2


x = np.arange(-3, 3, .1)
y = f(x)

plt.plot(x, y)
plt.show()

res = minimize(f, x0=100)

print(res)


def f(x):
    return np.exp(-x ** 2)  # Ненормированное распределение Гауса


x = np.arange(-3, 3, .1)
y = f(x)

plt.plot(x, y)
plt.show()

res, err = quad(f, 0, np.inf)
print(np.sqrt(np.pi) / 2, res, err)

res, err = quad(f, 0, 1)
print(np.sqrt(np.pi) / 2 * erf(1), res, err)


