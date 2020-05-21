

def to_camel_case(line):
    if '-' in line:
        list_line = line.split('-')
    else:
        list_line = line.split('_')
    return list_line[0] + ''.join([i.capitalize() for i in list_line[1:]])


def to_camel_case_(line):
    list_line = line.replace('-', '_').split('_')
    return list_line[0] + ''.join([i.capitalize() for i in list_line[1:]])


if __name__ == "__main__":
    print(to_camel_case("the-stealth-warrior"))
    print(to_camel_case_("the-stealth-warrior"))
    print(to_camel_case("The_Stealth_Warrior"))
    print(to_camel_case_("The_Stealth_Warrior"))
