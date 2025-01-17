import sys
from inspect import ismethod, getmodule
import inspect
from pprint import pprint

class MyClass:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def hello(self):
        return (f'Привет, меня зовут {self.name}, мне {self.age} лет, '
                f'и сейчас я проведу интроспекцию объекта')

def introspection_info(obj):
        return {'type': type(obj), 'attributes': dir(obj),
            'methods': [method for method in dir(obj) if callable(getattr(obj, method))],
            'module': inspect.getmodule(introspection_info),
            'other_properties': [sys.getsizeof(obj), bin(obj), isinstance(obj, int)]}

my_class = MyClass('Иван', 30)
print(my_class.hello())

number_info = introspection_info(42)
pprint(number_info)