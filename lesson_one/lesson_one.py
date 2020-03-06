import numpy as np
import math
import os
import pandas as pd
import matplotlib.pyplot as plt
from scipy.optimize import minimize
from scipy.integrate import quad, odeint
from scipy.special import erf
from scipy.interpolate import interp1d

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

a = np.arange(10, -1, -1)
a = np.delete(a, [5, 7])  # Удалены элементы с индексом 5 и 7
print(a)

a = np.insert(a, [2, 3], [-100, -200])
print(a)

a = np.append(a, [6, 6, 6])
print(a)

x = [
    [1, 2, 3],
    [4, 5, 6]
]
a = np.array(x)
print('a.len:', len(a))  # Высота
print('a.shape:', a.shape)  # Фигура

print(list(range(8)))
print(*range(0, 8))  # * - передает в функцию элементы через запятую
print([2, 5])
print(2, 5)

print(np.arange(0, -8, -0.5))

# %time np.arange(0, 50000000)

#######################################################################
# Дополнительные материалы 1.3 продвинутый курс видео:
# "2. Numpy и линейная алгебра: семинар (27.09.19)"
#######################################################################
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

#######################################################################
# Дополнительные материалы "3. Библиотеки Pandas и Matplotlib: семинар"
#######################################################################
# Pandas
print(
    '#######################################################################\n# Дополнительные материалы "3. Библиотеки Pandas и Matplotlib: семинар"\n#######################################################################')
print(os.getcwd())
data = pd.read_csv('lesson_one/AppleStore.csv')
print('-----------------------------------------------------------------------')
print(data)
print('-----------------------------------------------------------------------')
print(data.describe())
# count - сумма по столбцам
# mean - среднее значение
# std - стандартное отклонение
# min,max - минимальное, максимальное значение
# 25%, 50%, 75% - между максимумом и минимумом

print('-----------------------------------------------------------------------')
print(data.columns)
print('type of data:', type(data))
print('data.info :', data.info())
print('data.values', data.values)
print('data.values[0]', data.values[0])

print(data['track_name'])
print(type(data['track_name']))
print(type(data.values[0]))
print('One values in column track_name:', data['track_name'][0])
# Подвыборки
print(data.iloc[0])
print(data.loc[[0, 1, 2], ['track_name', 'id']])
print(data.iloc[5:100, 0:5])
print(len(data[data['user_rating'] >= 4]))

print(np.unique(data['currency']))

print(len(data[data['prime_genre'] == 'Games']))
print(len(data[(data['user_rating'] >= 4) & (data['prime_genre'] == 'Games')]))
print(len(data[(data['user_rating'] >= 4) | (data['prime_genre'] == 'Games')]))
print(len(data[(data['user_rating'] > 4.9999999999999995) & (data['prime_genre'] == 'Games')]['track_name']))
print(len(data[(data['user_rating'] > 4.9999999999999996) & (data['prime_genre'] == 'Games')]['track_name']))
print(np.unique(data['prime_genre']))  # Все жанры

print(np.array(data['size_bytes'].values))

#  Matplotlib
family_ivan = np.random.poisson(5, 5)
family_sid = np.random.poisson(5, 5)

x = np.arange(0, 10, 2)
plt.scatter(x, family_ivan, label='Ивановы')
plt.scatter(x, family_sid, label='Сидоровы')
plt.title('Статистика больных')
plt.ylabel('Кол-во больных')
plt.xlabel('T температура')
plt.legend()
plt.show()

print("Непрерывно")
plt.plot(x, family_ivan, '--', label='Ивановы')
plt.plot(x, family_sid, '--', label='Сидоровы')
plt.title('Статистика больных')
plt.ylabel('Кол-во больных')
plt.xlabel('T температура')
plt.legend()
plt.show()

print('bar')
plt.bar(x, family_ivan, alpha=0.9
        , label='Ивановы', color='r')
plt.bar(x, family_sid, alpha=0.6, label='Сидоровы', color='b')
plt.title('Статистика больных')
plt.ylabel('Кол-во больных')
plt.xlabel('T температура')
plt.legend()
plt.show()

print('Сгладим функции')

f_ivan = interp1d(np.arange(0, 10, 2), family_ivan, kind='quadratic', fill_value="extrapolate")
f_sid = interp1d(np.arange(0, 10, 2), family_sid, kind='quadratic', fill_value="extrapolate")

xnew = np.arange(0, 8.1, 0.1)
ynew_ivan = f_ivan(xnew)
ynew_sid = f_sid(xnew)
plt.plot(xnew, ynew_ivan, label='Ивановы')
plt.plot(xnew, ynew_sid, label='Сидоровы')
plt.title('Статистика больных')
plt.ylabel('Кол-во больных')
plt.xlabel('T температура')
plt.legend()
plt.show()

print('Поиск оптимальной температуры')
from scipy.optimize import minimize

max_ivan = minimize(f_ivan, x0=4)
max_sid = minimize(f_sid, x0=4)
xnew = np.arange(0, 8.5, 0.1)
ynew_ivan = f_ivan(xnew)
ynew_sid = f_sid(xnew)
plt.plot(xnew, ynew_ivan, label='Ивановы')
plt.plot([max_ivan.x[0]] * 14, np.arange(0, 14), label='{}'.format(max_ivan.x[0].round(2)))
plt.plot(xnew, ynew_sid, label='Сидоровы')
plt.plot([max_sid.x[0]] * 14, np.arange(0, 14), label='{}'.format(max_sid.x[0].round(2)))
plt.title('Статистика больных')
plt.ylabel('Кол-во больных')
plt.xlabel('T температура')
plt.legend()
plt.show()
