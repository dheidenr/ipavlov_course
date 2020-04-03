def bread(func):
    # print(3)

    def wrapper():
        # print(5)
        print("кусочек хлеба")
        func()
        # print(10)
        print("кусочек хлеба")

    # print(4)
    return wrapper


def ingredients(func):
    # print(1)
    def wrapper():
        # print(6)
        print("#помидоры#")
        func()
        # print(9)
        print("~салат~")
    # print(2)
    return wrapper


@bread
@ingredients
def sandwich(food="--ветчина--"):
    # print(7)
    print(food)
    # print(8)


# test = bread(ingredients(sandwich))
# test()
sandwich()

