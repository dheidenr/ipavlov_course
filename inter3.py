
def error_rate(line):
    error = 0
    for i in line:
        if i < 'a' or i > 'm':
            error += 1
    return f'{error}/{len(line)}'


def error_rate_(line):
    return f'{sum([1 for i in line if i < "a" or i > "m"])}/{len(line)}'


if __name__ == "__main__":
    print(error_rate("aaabbbbhaijjjm"))
    print(error_rate("aaaxbbbbyyhwawiwjjjwwm"))
    print(error_rate_("aaabbbbhaijjjm"))
    print(error_rate_("aaaxbbbbyyhwawiwjjjwwm"))