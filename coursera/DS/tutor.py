
# Так было бы в 2-й версии python: print 'Hello'
print('Hello')

# Во втором python необходимо самостоятельно привести одно из пременных деления к float
# в третьем автоматически при делении получается тип float
print(10/2)

ll = []
ll.append(1)
print(ll)
ll.insert(0, 3)
print(ll)
ll.pop()
print(ll.pop())

print('Hello, world!'.replace(' ', '_'))


for i in range(10):
    print(i, ) # Во втором питоне можно написать "print 1," - это выведет через пробел не с переносом строки

w = (x for x in range(10)) # Создали генератор
print(type(w))


# my generator
def downist(num):
    w = 10
    print(w)
    while num > 0:

        yield num
        num -= 1

gena = downist(5)

# num = next(gena)
# num = next(gena)
# num = next(gena)

l = [4]

for _ in gena:
    print('downist num:', _)
    pass

# hash(l)

l = []
object_tuple = (l, l)
l.append(666)
# object_set = {(l, l), ('test tuple',), 2}
l.append('asdf')
# print(object_tuple)


def printer(**kwargs):
    # print(kwargs)
    for key, value in kwargs.items():
        # print('{}:{}'.format(key, value))
        print(f'{key} : {value}')


d = dict({
    'hi': 666
})

printer(a=10, b=120)
printer(**d)


def foo(*args, **kwargs): pass


l = [1, 2, 3]


def int_to_str_list(numbers):
    return list(map(str, numbers))


# def squarify(a):
#     return a ** 2
#
# print(list(map(squarify(), range(5))))



print(int_to_str_list(l))

kartej = (1, 'asdf', 3)


print(', '.join({}.get('2')))