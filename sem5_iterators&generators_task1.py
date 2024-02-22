"""
Напишите функцию get_file_info, которая принимает на вход строку - абсолютный путь до файла.
Функция возвращает кортеж из трёх элементов: путь, имя файла, расширение файла.
На входе:
file_path = "C:/Users/User/Documents/example.txt"

На выходе:
('C:/Users/User/Documents/', 'example', '.txt')
"""


# def get_file_info(path):
#     last_slash = path.rfind('/')
#     file_path = path[:last_slash]
#
#     last_dot = path.rfind('.')
#     if last_dot == -1:
#         file_name = path[last_slash + 1:]
#         extension = ''
#     else:
#         file_name = path[last_slash + 1:last_dot]
#         extension = path[last_dot:]
#     return file_path, file_name, extension
#
#
# file_path = "C:/Users/User/Documents/example.txt"
# print(get_file_info(file_path))

# import os
#
#
# def get_file_info(file_path):
#     path, filename = os.path.split(file_path)
#     print("os.path.split(file_path) = ", os.path.split(file_path))
#     print("path, filename = ", path, filename)
#     if path:
#         path += '/'
#     name, extension = os.path.splitext(filename)
#     print(name)
#     print(extension)
#     return path, name, extension
#
#
# file_path = "C:/Users/User/Documents/example.txt"
# print(get_file_info(file_path))

def get_file_info(file_path):
    file_name = file_path.split("/")[-1]
    print(file_name)
    file_extension = file_name.split(".")[-1]
    print(file_extension)
    path = file_path[:-len(file_name)]
    print(len(file_name))
    print(path)
    return path, file_name[:-len(file_extension) - 1], "." + file_extension


file_path = "C:/Users/User/Documents/example.txt"
print(get_file_info(file_path))