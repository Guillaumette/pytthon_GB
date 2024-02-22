"""Напишите функцию, которая сохраняет созданный в прошлом задании файл в формате CSV."""
import csv
import json


def json_to_csv(filename: str):
    with open(filename, 'r', encoding='utf-8') as file:
        json_dict = json.load(file)

        # Создаем список кортежей (имя, айди, уровень доступа), который будем превращать в csv
        user_list = []
        for user_lvl, user in json_dict.items():
            for user_id, user_name in user.items():
                user_list.append((user_name, user_id, user_lvl))

        with open(filename.split('.')[0] + '.csv', 'w', encoding='utf-8', newline='') as csv_file:
            csv_write = csv.writer(csv_file, dialect='excel', delimiter='|')
            csv_write.writerow((['Имя', 'ID', 'Уровень']))
            for row in user_list:
                csv_write.writerow(row)


json_to_csv('workers.json')


