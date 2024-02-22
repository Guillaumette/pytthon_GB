"""
Из созданных на уроке и в рамках домашнего задания функций, соберите пакет для работы с файлами.

Создайте файл __init__.py и запишите в него все функции:
get_dir_size,
save_results_to_json,
save_results_to_csv,
save_results_to_pickle, traverse_directory.
"""


my_file = open("__init__.py", "w+")
my_file.write("all = ['def get_dir_size', 'def save_results_to_json', 'def save_results_to_csv',"
              "'def save_results_to_pickle', 'def traverse_directory']")
my_file.close()