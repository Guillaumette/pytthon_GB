"""
📌 Создайте функцию-замыкание, которая запрашивает два целых числа:
○ от 1 до 100 для загадывания,
○ от 1 до 10 для количества попыток
📌 Функция возвращает функцию, которая через консоль просит угадать загаданное число за указанное число попыток.
"""
from random import randint as ri

MIN_LIMIT = 1
MAX_LIMIT = 100
MIN_COUNT = 1
MAX_COUNT = 10


def guess_number(number: int, count: int):
    user_number = number if MIN_LIMIT <= number <= MAX_LIMIT else ri(MIN_LIMIT, MAX_LIMIT)
    user_count = count if MIN_COUNT <= count <= MAX_COUNT else ri(MIN_COUNT, MAX_COUNT)

    def inner():
        nonlocal user_count
        while user_count:
            guess_num = int(input(f'Угадайте число от {MIN_LIMIT} до {MAX_LIMIT}: '))
            if guess_num == user_number:
                print(f'Ура, ты победил! Это число {user_number}')
                return
            elif guess_num < user_number:
                print('Загаданное число больше!')
            else:
                print('Загаданное число меньше!')
            user_count -= 1
        print(f'Увы, ты проиграл! Это было число {user_number}!')

    return inner


if __name__ == '__main__':
    game = guess_number(165, 7)
    game()
