"""
📌 Напишите декоратор, который сохраняет в json файл параметры декорируемой функции и результат, который она возвращает.
При повторном вызове файл должен расширяться, а не перезаписываться.
📌 Каждый ключевой параметр сохраните как отдельный ключ json словаря.
📌 Для декорирования напишите функцию, которая может принимать как позиционные, так и ключевые аргументы.
📌 Имя файла должно совпадать с именем декорируемой функции.
"""

import json
import os.path
from functools import wraps


def json_decor(func):
    @wraps(func)
    def inner(*args, **kwargs):
        file_name = f'{func.__name__}.json'
        if os.path.exists(file_name):
            with open(file_name, 'r', encoding='utf-8') as file:
                result = json.load(file)
        else:
            result = {}
        primary_key = func(*args, **kwargs)
        primary_value = {}
        primary_value['args'] = args
        primary_value['kwargs'] = {}

        for key, value in kwargs.items():
            primary_value['kwargs'][key] = value
        result[primary_key] = primary_value
        with open(file_name, 'w', encoding='utf-8') as file:
            json.dump(result, file, indent=4, ensure_ascii=False)

    return inner


if __name__ == '__main__':
    @json_decor
    def some_func(a, b):
        return a + b


    some_func(5, 2)
    some_func(2, 2)
    some_func(8, 2)
