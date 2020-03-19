import math

# base python

print('test')
print(-15 // 4)  # Получиться -4 поскольку -4*4 = -16
print(-15 % 4)  # Остаток всегда положительное число поэтому тут будет 1
# print(5 * 1000000000 * 1000000000 * 10**9999 + 1)

print(len('чего-то'))
print(True + 4)

# list(range(3))[3]

text = 'hello'

print(text[4:100])


def g(x):
    return x[::-1]


s = ['31', '22', '59', '1c']
print(list(map(g, s)))
print(list(map(lambda x: x[::-1], s)))

for i in range(10):
    print(i)


# Правильный вариант решения первой задачи
def almost_double_factorial(number):
    result = 1
    for factor in range(1, number + 1, 2):
        result *= factor
    return result


def fractal(number):
    if number <= 1:
        return 1
    return number * fractal(number - 1)


# Тоже правильный вариант решения первой задачи, но ломается на сервере из-за
# превышения стека вызовов.
def almost_double_factorial_rec(num):
    num -= 0 if num % 2 != 0 else 1
    return 1 if num <= 2 else num * almost_double_factorial_rec(num - 2)


print('Test 100...')
for i in range(0, 100, 1):
    # print(almost_double_factorial_rec(i), '=', almost_double_factorial(i))
    if almost_double_factorial_rec(i) != almost_double_factorial(i):
        print('ERROR: i = ', i)

# 3.1.9
# Пусть у нас есть следующий список, в котором элементы -- tuple из строк:
#
items = [('one', 'two'), ('three', 'four'), ('five', 'six'), ('string', 'a')]
# Мы хотим отсортировать этот список по последней букве второго элемента каждого
# tuple, т.е. получить такой список:
sorted_items = [('string', 'a'), ('one', 'two'), ('three', 'four'), ('five', 'six'), ]
#
# Что нужно вставить вместо "<...>" в следующем выражении,
# чтобы получить верную сортировку?
#
# sorted_items = sorted(items, key=lambda x: <...>)
# P.S.: в ответе не должно фигурировать слово len

# code
# items объявлять не нужно
sorted_items2 = sorted(items, key=lambda x: x[1][-1])

print(items)
print(sorted_items2)
print(sorted_items)

# b = [(5, 3.6, "квадрат", 15, 'В')]
# print(b[0])
# print(('one', 'two')[1][-1])
# print(items[0:10][:1][-1])
# print(b[0][1:3])

x = [1, 2, 3, 4, 5]
x[::-2] = [-1, -3, -5]
print([-5, 2, -3, 4, -1])
print(x)


def cumsum_and_erase(A, erase=1):
    element = 0
    B = []
    for number in A:
        element += number
        if erase != element:
            B.append(element)
    return B


a = "lsj94ksd231 9"
b = [int(i) for i in a if '0' <= i <= '9']


def cumsum_and_erase_optimal(A, erase=1):
    return [sum(A[:i]) for i in range(1, len(A) + 1) if sum(A[:i]) != erase]


A = [5, 1, 4, 5, 14]
# B = cumsum_and_erase(A, erase=10)
# assert B == [5, 6, 15, 29], "Something is wrong! Please try again"
print([5, 6, 15, 29])
print(cumsum_and_erase(A, erase=10))
print(cumsum_and_erase_optimal(A, erase=10))


def process(sentences):
    result = []
    for token in sentences:
        words = []
        for word in token.split(' '):
            if word.isalpha():
                words.append(word)
        words = ' '.join(words)
        result.append(words)
    return result


def process_optimal(s):
    result = [" ".join([j for j in i.split() if j.isalpha()]) for i in s]
    return result


sentences = ['1 thousand devils', 'My name is 9Pasha', 'Room #125 costs $100']

final = ['thousand devils', 'My name is', 'Room costs']

print(' '.join(('Hello', 'world!')))
print(sentences)
print(final)
print(process(sentences))


class Neuron:
    x = []

    def __init__(self, w, f=lambda x: x):
        self.w = w
        self.f = f

    def forward(self, x):
        self.x = x
        return self.f(sum([self.w[element] * x[element] for element in range(0, len(x))]))
        # Оптимально использовать zip, который позволяет прыгать по нескольким итерируемым объектам:
        # return self.f(sum([i * j for i, j in zip(self.w, x)]))

    def backlog(self):
        return self.x


## Тесты из jupiter домашнего задания

w = [0.5, 1., -1., 2.]

neuron = Neuron([0.5, 1., -1., 2.], lambda x: 1. / (1 + math.exp(x)))

x = [1, 2, 3, 4]

assert abs(neuron.forward(x) - 0.0005527) < 1e-6, "Something is wrong! Please try again"

assert neuron.backlog() == x, "Something is wrong! Please try again"

y = [0, 0, 0, 0]

assert abs(neuron.forward(y) - 0.5) < 1e-6, "Something is wrong! Please try again"
