
def cude_odd(numbers):
    sum = 0
    for i in numbers:
        if type(i) != int:
            return None
        if i ** 3 % 2 != 0:
            sum += i ** 3
    return sum


def cude_odd_(numbers):
    if sum(map((lambda x: type(x) != int), numbers)):
        return None
    return sum([i ** 3 for i in numbers if i ** 3 % 2 != 0])


if __name__ == '__main__':
    print(cude_odd_(['sadf', 2, 3, 4]))
    print(cude_odd([1, 2, 3, 4]))
