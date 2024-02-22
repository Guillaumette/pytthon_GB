"""
Вспоминаем задачу 3 из прошлого семинара. Мы сформировали текстовый файл с псевдо именами и произведением чисел.
📌 Напишите функцию, которая создаёт из созданного ранее файла новый с данными в формате JSON.
📌 Имена пишите с большой буквы.
📌 Каждую пару сохраняйте с новой строки.
"""

import json


def convert_to_json(input_file, output_file):
    data = {}
    with open(input_file, 'r') as file:
        for line in file:
            # Разбиваем строку по разделителю " | '
            # Удаляем пробельные символы и преобразуем имя в формат с заглавной буквы
            name, number = line.strip().split(' | ')
            data[name.strip().capitalize()] = float(number)

    # Записываем данные в формате JSON в выходной файл с отступами для удобочитаемости
    with open(output_file, 'w', encoding='utf-8') as file:
        json.dump(data, file, indent=4)


# Вызов функции для конвертации данных из result.txt в result.json
convert_to_json('result.txt', 'result.json')
