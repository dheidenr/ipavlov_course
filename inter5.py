import re


def pig_it(line):
    list_line = line.split(' ')
    for i in range(len(list_line)):
        list_line[len(list_line) - 1] += list_line[i][0]
        list_line[i] = list_line[i][1:] + 'ay'
    return ' '.join(list_line)


def pig_it_(line):
    words = re.findall(r'\b\w+\b', line)
    return ' '.join([i[1:] + i[0] + 'ay' for i in words])


if __name__ == "__main__":
    print(pig_it('Pig , latin is cool ! '))
    print(pig_it_('Pig, latin is cool!'))