import re


def error_rate(line):
    error = 0
    for i in line:
        if i < 'a' or i > 'm':
            error += 1
    return f'{error}/{len(line)}'


# def error_rate_(line) -> str:
#     return f'{sum([True for i in line if i < "a" or i > "m"])}/{len(line)}'


def error_rate_(line) -> str:
    return f'{len(re.findall(r"[^a-m]", line))}/{len(line)}'


if __name__ == "__main__":
    print(error_rate("aaabbbbhaijjjm"))
    print(error_rate("aaaxbbbbyyhwawiwjjjwwm"))
    print(error_rate_("aaabbbbhaijjjm"))
    print(error_rate_("aaaxbbbbyyhwawiwjjjwwm"))