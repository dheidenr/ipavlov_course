from __future__ import annotations
from typing import Optional


class SingletonMeta(type):
    """
    В Python класс Одиночка можно реализовать по-разному. Возможные способы
    включают в себя базовы класс, декоратор, метакласс. Мы воспользуемся
    метаклассом, поскольку он лучше всего подходит для этой цели.
    """

    _instance: Optional[Singleton] = None

    def __call__(cls) -> Singleton:
        if cls._instance is None:
            cls._instance = super().__call__()
        return cls._instance


class Singleton(metaclass=SingletonMeta):
    def some_business_logic(self):
        """
        Наконец, любой одиночка должен содержать некоторую бизнес-логику,
        которая может быть выполнена на его экземпляре.
        """
        print('Заглушка для некоторой бизнес логики Singleton')
        pass


if __name__ == "__main__":

    s1 = Singleton()
    s2 = Singleton()

    if id(s1) == id(s2):
        print("Singleton works, both variables contain the same instance.")
    else:
        print("Singleton, failed, variables contain different instances.")
