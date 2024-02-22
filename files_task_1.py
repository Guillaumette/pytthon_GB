"""Напишите функцию группового переименования файлов в папке test_folder под названием rename_files. Она должна:

a. принимать параметр желаемое конечное имя файлов. При переименовании в конце имени добавляется порядковый номер.
b. принимать параметр количество цифр в порядковом номере.
c. принимать параметр расширение исходного файла. Переименование должно работать только для этих файлов внутри каталога.
d. принимать параметр расширение конечного файла.
e. принимать диапазон сохраняемого оригинального имени. Например для диапазона [3, 6] берутся буквы
с 3 по 6 из исходного имени файла. К ним прибавляется желаемое конечное имя, если оно передано. Далее счётчик
файлов и расширение.
f. Папка test_folder доступна из текущей директории"""

import os


def rename_files(source_ext: str,
                 target_ext: str,
                 path: str = './test_folder',  # Заменить на './test_folder' для автотестов
                 desired_name='',
                 num_digits=None,
                 limits: tuple = (),
                 ):
    count = 0
    for file in os.listdir(path):
        if file.endswith(source_ext):
            count += 1
            name = file.rsplit('.')
            if limits:
                re_name = f'{name[0][limits[0]:limits[1]]}{desired_name}{count:0>{num_digits}}.{target_ext}'
            else:
                re_name = f'{desired_name}{count:0>{num_digits}}.{target_ext}'

            os.rename(os.path.join(path, file), os.path.join(path, re_name))


rename_files(desired_name="new_file_", num_digits=3, source_ext="txt", target_ext="doc")

