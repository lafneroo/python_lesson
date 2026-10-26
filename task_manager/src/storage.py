"""
==============================
    модуль с функциями сохранения и загрузки
==============================
"""
import json
from config import FILE_NAME_SAVES

save_file = FILE_NAME_SAVES
"""загрузка"""


def load_collection(task_list):
    with open(save_file, "r", encoding="utf-8") as file:
        data = json.load(file)
        task_list.append(data)
    return task_list


"""сохранение"""


def save_collection(task_list):
    with open(save_file, 'w', encoding='utf-8') as file:
        json.dump(task_list, file, ensure_ascii=False, indent=4)