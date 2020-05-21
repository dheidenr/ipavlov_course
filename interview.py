import re


# task 1
def cube_odd(numbers):
    if sum(map((lambda x: type(x) != int), numbers)):
        return None
    return sum([i ** 3 for i in numbers if i ** 3 % 2 != 0])


# task 2
def find_even_index(numbers) -> int:
    try:
        return next(i for i in range(len(numbers))
                    if sum(numbers[:i]) == sum(numbers[i + 1:]))
    except StopIteration:
        return -1


# task 3
def error_rate(line) -> str:
    return f'{len(re.findall(r"[^a-m]", line))}/{len(line)}'


# task 4
def to_camel_case(line) -> str:
    words = line.replace('-', '_').split('_')
    return words[0] + ''.join([i.capitalize() for i in words[1:]])


# task 5
def pig_it(line):
    words = re.findall(r'\b\w+\b[,!]?', line)
    return ' '.join([i[1:] + i[0] + 'ay' if i[-1] != ',' and i[-1] != '!' else
                     i[1:-1] + i[0] + 'ay' + i[-1] for i in words])


# task 6
def string_expansion(line: str) -> str:
    number = 0
    if line == '':
        return line
    result_line = ''
    for letter in line:
        if letter.isdigit():
            number = int(letter)
        else:
            result_line += letter * number if number else letter
    return result_line


def tests_cude_odd():
    assert cube_odd([1, 2, 3, 4]) == 28, "It's not 28"
    assert cube_odd([-3, -2, 2, 3]) == 0, "It's not 0"
    assert cube_odd(["a", 12, 9, "z", 42]) is None, "It's not None"


def tests_find_even_index():
    assert find_even_index([1, 2, 3, 4, 3, 2, 1]) == 3, "It's not 3"
    assert find_even_index([1, 100, 50, -51, 1, 1]) == 1, "It's not 1"
    assert find_even_index([0, 0, 0, 0]) == 0, "It's not 0"
    assert find_even_index([1, 2, 3, 4]) == -1, "It's not -1"


def tests_error_rate():
    assert error_rate("aaabbbbhaijjjm") == "0/14", "It's not 0/14"
    assert error_rate("aaaxbbbbyyhwawiwjjjwwm") == "8/22", "It's not 8/22"


def tests_to_camel_case():
    assert to_camel_case("the-stealth-warrior") == "theStealthWarrior", "Error-"
    assert to_camel_case("The_Stealth_Warrior") == "TheStealthWarrior", "Error_"


def tests_pig_it():
    assert pig_it('Pig, latin is cool!') == 'igPay, atinlay siay oolcay!', \
        "Error in function tests_pig_it"


def tests_string_expansion():
    assert string_expansion('3D2a5d2f') == 'DDDaadddddff', \
        "It's not DDDaadddddff"
    assert string_expansion('3abc') == 'aaabbbccc', "It's not aaabbbccc"
    assert string_expansion('3abc') != 'aaabc', "It's not aaabc"
    assert string_expansion('3abc') != 'abcabcabc', "It's not abcabcabc"
    assert string_expansion('3d332f2a') == 'dddffaa', "It's not dddffaa"
    assert string_expansion('abcde') == 'abcde', "It's not abcde"
    assert string_expansion('') == '', "It's not ''"


if __name__ == "__main__":
    print('-' * 10 + 'tests' + '-' * 10)
    tests_cude_odd()
    tests_find_even_index()
    tests_error_rate()
    tests_to_camel_case()
    tests_pig_it()
    tests_string_expansion()
    print("Everything passed")
