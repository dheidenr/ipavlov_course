import re

print(re.match(r'\d+', '1234560789'))
print(re.match(r'\s+', '1234560789'))


def float_regexp() -> str:
    optsign = r'[+\-]?'
    int_opt_frac = r'\d+(\.\d*)?'
    just_frac = r'\.\d+'
    mantissa = fr'{optsign}({int_opt_frac}|{just_frac})'
    order = fr'[Ee]{optsign}\d+'
    return fr'{mantissa}({order})'


def float_regexp_cool_text() -> str:
    floatpoint_v = r'''
    [+\-]?              # optional sign
    (                   # mantissa value
        \d+ (\. \d*?)   # integral part with optional fraction
    | \. \d+            # no integral part with mandatory fraction
    )
    '''


print(float_regexp())
regexp_instance = re.compile(float_regexp())

print(type(regexp_instance))
print(regexp_instance)
print()
print(regexp_instance.match('123.45e+67'))
print(re.match(float_regexp(), '123.45e+67'))
print()
print(regexp_instance.match('kjsakjfdk'))
print(float_regexp())

print(re.sub(r'\be\b', 'Pollo', 'hello the world'))
print(re.match(r'\b\w+\b', 'hello the world'))
print(re.search(r'\b\w{3}\b', 'held the wor'))
print(re.search(r'\b\w{4,}\b', 'hello the world'))

mytext = "asdasdfadfasdf sad Аas df hello sdf v asdf Фsd fa sdf sdf sd f Aasdf asd Zasdf 324230 23423 823y 47234 2y3472 325745745 24172127 sdfa sdf, ssss@asdfas.ru asdfasdf@asdf.gov"

"""
\d   = Any Digit
\D   = Any non DIGIT
\w   = Any Alphabet symbol [A-Z a-z]
\W   = Any non Alphabet symbol
\s   = breakspace
\S   = non breakspace

[0-9]{3}
[\w]


"""
text_look_for = r"hell"
allresults = re.findall(text_look_for, mytext) # найти все вхождения mytext
text_look_for = r'\d\d\d'
text_look_for = r'[0-9]{3}' # аналог
text_look_for = r'\d{3}' # аналог
allresults = re.findall(text_look_for, mytext) # найти все вхождения трех цифр
text_look_for = r'\w{6}\s' # любые 6 потряд символов, после которых стоит пробел
text_look_for = r'[A-Z][a-z]+' # слова начинающиеся с большой буквы например имена
text_look_for = r'\w+@\w+\.\w+' # mail
allresults = re.findall(text_look_for, mytext) # найти все вхождения трех цифр


print(allresults)
