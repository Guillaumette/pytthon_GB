"""
📌 Создайте декоратор с параметром.
📌 Параметр - целое число, количество запусков декорируемой функции.
"""
from functools import wraps


def deco_with_params(count: int):
    result = []

    @wraps
    def outer(func):
        @wraps(func)
        def inner(*args, **kwargs):
            for _ in range(count):
                result.append(func(*args, **kwargs))
            return result
        return inner
    return outer


if __name__ == '__main__':

    @deco_with_params(5)
    def simple_func(message: str):
        return message


    simple_func('Привет!')