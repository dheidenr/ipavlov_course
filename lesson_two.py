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

def almost_double_factorial_rec(num):
    num -= 0 if num % 2 != 0 else 1
    return 1 if num <= 2 else num * almost_double_factorial_rec(num - 2)

print('Test 100...')
for i in range(0, 100, 1):
    print(almost_double_factorial_rec(i), '=', almost_double_factorial(i))
    if almost_double_factorial_rec(i) != almost_double_factorial(i):
        print('ERROR: i = ', i)

