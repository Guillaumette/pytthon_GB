"""
Напишите функцию, которая ищет json файлы в указанной директории и сохраняет
их содержимое в виде одноимённых pickle файлов.
"""

from sem_08_2_teacher import load_json
import pickle
import os
import json


def save_pickle(filename, data):
    with open(filename, 'wb') as pickle_file:
        pickle.dump(data, pickle_file)


def search_json(dir_name):
    for obj in os.listdir(os.path.join(os.getcwd(), dir_name)):
        file_name, file_ext = obj.split('.')
        if file_ext == 'json':
            json_dict = load_json(obj)
            save_pickle(file_name + '.PICKLE', json_dict)


search_json('test')