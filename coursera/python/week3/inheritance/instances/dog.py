import json
from coursera.python.week3.inheritance.abstract.pet import Pet


class Dog(Pet):
    def __init__(self, name="Собака", breed=None):
        super().__init__(name)
        self.breed = breed

    def say(self):
        return f'{self.name}'


class ExportJSON:
    def to_json(self):
        return json.dumps({
            "name": self.name,
            "bread": self.breed
        })


class ExDog(Dog, ExportJSON):
    def __init__(self, name, breed=None):
        super().__init__(name, breed)


class WoolenDog(Dog, ExportJSON):
    def __init__(self, name, breed=None):
        super(Dog, self).__init__(name)
        self.breed = f"Шерстяная собака порода {breed}"


# dog = Dog("Шарик", "Доберман")
dog = ExDog("Белка", breed="Дворняга")
wdog = WoolenDog("Бешаная", "Пакса")
print(wdog.breed)
print(dog.name)
print(dog.say())
print(dog.breed)
print(dog.to_json())
print(issubclass(Dog, object))

print(isinstance(Dog(), Dog))
print(isinstance(Dog(), Pet))
print(isinstance(Dog, Dog))
print(isinstance(Pet(), object))
print(isinstance(Pet(), Dog))
