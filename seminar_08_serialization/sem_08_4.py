"""
📌 Прочитайте созданный в прошлом задании csv файл без использования csv.DictReader.
📌 Дополните id до 10 цифр незначащими нулями.
📌 В именах первую букву сделайте прописной.
📌 Добавьте поле хеш на основе имени и идентификатора.
📌 Получившиеся записи сохраните в json файл, где каждая строка csv файла представлена как отдельный json словарь.
📌 Имя исходного и конечного файлов передавайте как аргументы функции.
"""

import csv
import json


def save_json(path: str, data: list):
    """Функция для записи JSON-файла"""
    with open(path, 'w', encoding='utf-8') as file:
        for item in data:
            json.dump(item, file, indent=4, ensure_ascii=False)


def csv_to_json(filename):
    with open(filename, 'r', encoding='utf-8') as file:
        data = file.readlines()

    json_list = []
    for line in data[1:]:
        man_names = line.split("|")[0].capitalize()
        man_id = line.split("|")[1].zfill(10)
        man_hash = hash(man_names + man_id)
        json_list.append({man_id: [man_names, man_hash]})

    save_json('workers_new.json', json_list)


csv_to_json('workers.csv')