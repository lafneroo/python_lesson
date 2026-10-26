"""
==============================
    модуль с функциями сохранения и загрузки
==============================
"""
import json
import os

"""загрузка"""


def load_collection(task_list, file_name):
    with open(file_name, "r", encoding="utf-8") as file:
        data = json.load(file)
        task_list.append(data)
        file.close()
    return task_list


"""сохранение"""


def save_collection(task_list, file_name):
    with open(file_name, 'w', encoding='utf-8') as file:
        json.dump(task_list, file, ensure_ascii=False, indent=4)