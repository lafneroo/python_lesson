"""
======================================================
    модуль вывода информации в консоль
======================================================
"""


from storage import load_collection, save_collection
from wiew import show_message, show_collection
from core import create_task, edited_task, deleted_task
from utils import check_confirm, get_base_dir, insure_save_file
import os.path
"""основной цикл"""

def app():
    name_file = os.path.join(get_base_dir(), "saves.txt")
    insure_save_file(name_file)
    collection = load_collection([], name_file)
    is_running = True

    while is_running:
        print('1 - посмотреть задачи'
              '\n2 - добавить задачу'
              '\n3 - редактирование'
              '\n4 - снять задачу'
              '\n5 - выход')
        choice_user = input("введите команду: ")

        match str(choice_user):
            case "1":  # просмотр списка
                show_collection(collection)
            case "2":  # добавление в список
                create_task(collection, name_file)
            case "3":  # изменение элемента
                edited_task(collection)
                save_collection(collection, name_file)
            case "4":  # удаление элемента
                show_collection(collection)
                deleted_task(collection)
                save_collection(collection, name_file)
            case "5":  # завершение цикла
                is_running = check_confirm('отключение...')
            case _:  # неверная команда
                print('неверная команда')
                show_message()

app()