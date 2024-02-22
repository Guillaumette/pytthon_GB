"""
Из созданных на уроке и в рамках домашнего задания функций, соберите пакет для работы с файлами.

Создайте файл __init__.py и запишите в него все функции:
save_to_json,
find_roots,
generate_csv_file.
"""

my_file = open("__init__.py", "w+")
my_file.write("all = ['def save_to_json', 'def find_roots', 'def generate_csv_file',']")
my_file.close()
