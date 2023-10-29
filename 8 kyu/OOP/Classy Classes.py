class Person:
    def __init__(self, name: str, age: int):
        self._name = name
        self._age = age
        self.info = f'{self._name}s age is {self._age}'


person = Person("John", 16)
print(person.info)