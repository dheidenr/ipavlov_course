

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


if __name__ == "__main__":
    print(string_expansion('3D2a5d2f'))
    print(string_expansion('3d332f2a'))
    print(string_expansion('abcde'))
    print('|', string_expansion(''), '|', sep='')

