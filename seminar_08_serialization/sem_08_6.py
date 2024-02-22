"""
📌 Напишите функцию, которая преобразует pickle файл, хранящий список словарей, в табличный csv файл.
📌 Для тестирования возьмите pickle версию файла из задачи 4 этого семинара.
📌 Функция должна извлекать ключи словаря для заголовков столбца из переданного файла.
"""


import pickle
import csv

# data = [
#     {'name': 'Stone', 'age': 38, 'work': 'GB'},
#     {'name': 'Игорь', 'age': 28, 'work': 'Дома'},
#     {'name': 'Alex', 'age': 18, 'work': 'Работа'}
# ]
#
# with open('sample.pickle', 'wb') as file_pickle:
#     pickle.dump(data, file_pickle)


def pickle_to_csv(path: str):
    result = []
    with open(path, 'rb') as pickle_file:
        dict_data = pickle.load((pickle_file))
    headers = [header for header in dict_data[0]]
    for header in headers:
        row = []
        for contact in dict_data:
            row.append(contact[header])
        result.append(row)
    with open(path.split('.')[0] + '.csv', 'w', encoding='utf-8') as csv_file:
        csv_writer = csv.writer(csv_file, dialect='excel', delimiter='|', lineterminator='\n')
        csv_writer.writerow(headers)
        csv_writer.writerows(list(zip(*result)))


pickle_to_csv('sample.pickle')