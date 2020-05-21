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
