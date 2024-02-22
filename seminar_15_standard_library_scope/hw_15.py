import os
import logging
from collections import namedtuple

# Настройка логирования
logging.basicConfig(filename='directory_info.log', level=logging.INFO, format='%(asctime)s - %(message)s')

# Определение объекта namedtuple для хранения информации о файле/каталоге
FileInfo = namedtuple('FileInfo', ['name', 'extension', 'is_directory', 'parent_directory'])

def gather_directory_info(directory_path):
    # Проверка на существование директории
    if not os.path.isdir(directory_path):
        logging.error(f"Директория {directory_path} не существует.")
        return

    # Обход директории
    for root, dirs, files in os.walk(directory_path):
        # Получение имени родительской директории
        parent_directory = os.path.basename(root)

        # Обработка файлов
        for file_name in files:
            file_name_no_ext, file_extension = os.path.splitext(file_name)
            logging.info(f"Имя файла: {file_name_no_ext}, Расширение: {file_extension}, Явл. директорией: False,"
                         f"Родительская директория: {parent_directory}")

        # Обработка поддиректорий
        for dir_name in dirs:
            logging.info(f"Имя директории: {dir_name}, Расширение: None, Явл. директорией: True,"
                         f"Родительская директория: {parent_directory}")


if __name__ == "__main__":
    import sys
    if len(sys.argv) != 2:
        print("Usage: python script.py <directory_path>")
        sys.exit(1)

    directory_path = sys.argv[1]
    gather_directory_info(directory_path)
