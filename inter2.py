
def find_even_index(numbers):
    for i in range(len(numbers)):
        if sum(numbers[0:i]) == sum(numbers[i + 1:len(numbers)]):
            return i
    return -1


def find_even_index_(numbers):
    return [i for i in range(len(numbers)) if sum(numbers[:i]) == sum(numbers[i + 1:])][0]


if __name__ == '__main__':
    print(find_even_index([1, 2, 3, 4, 3, 2, 1]))
    print(find_even_index([1, 100, 50, -51, 1, 1]))
    print(find_even_index_([1, 2, 3, 4, 3, 2, 1]))
    print(find_even_index_([1, 100, 50, -51, 1, 1]))
