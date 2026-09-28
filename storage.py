"""
==============================
    модуль с функциями сохранения и загрузки
==============================
"""



"""загрузка"""


def load_collection(task_list, file_name):
    with open(file_name, "r", encoding="utf-8") as file:
        for line in file:
            task_list.append(line.strip())
        file.close()
    return task_list


"""сохранение"""


def save_collection(task_list, file_name):
    with open(file_name, 'w', encoding='utf-8') as file:
        for task in task_list:
            file.writelines(f"{task}\n")
        file.close()