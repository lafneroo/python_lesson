""" Приложение Task Manager
    =============================================================
        консольное приложение - менеджер управления заметок,
        пользователь может создать заметку, редактировать,
        посмотреть все заметки или удалить выбранную.
    =============================================================
    ~~~~~~~~~~~~~~~~~~~~~
    | version app 0.0.7 |
    ~~~~~~~~~~~~~~~~~~~~~

    v(0.0.1)
    разработан цикл приложения - структурное программирование

    v(0.0.2)
    внедрен  i/o функционал для ввода задачи

    v(0.0.3)
    разработаны функции для цикла - функциональное программирование

    v(0.0.4)
    добавлены проверки и подтверждения

    v(0.0.5)
    созданы методы сохранения и загрузки - файловые сохранения

    v(0.0.6)
    созданы методы для удаления, редактирования и создания задач - логика вынесена из цикла

    v(0.0.7)
    основной цикл помещен в отдельный метод - def main

    v(0.0.8)
    реализован функционал добавления контента задачи - имя + содержание
"""

"""основной цикл"""


def main():
    name_file = "saves.txt"
    collection = load_collection([], name_file)
    is_running = True

    while is_running:
        print('1 - посмотреть задачи'
              '\n2 - добавить задачу'
              '\n3 - редактирование'
              '\n4 - снять задачу'
              '\n5 - выход')
        choice_user = input("введите команду: ")

        match choice_user:
            case "1":  # просмотр списка
                show_collection(collection)
            case "2":  # добавление в список
                create_task(collection, name_file)
            case "3":  # изменение элемента
                edited_task(collection)
                save_collection(collection, name_file)
            case "4":  # удаление элемента
                show_collection(collection)
                deleated_task(collection)
                save_collection(collection, name_file)
            case "5":  # завершение цикла
                is_running = check_confirm('отключение...')
            case _:  # неверная команда
                print('неверная команда')
                show_message()


"""выводит список в консоль"""


def show_collection(task_list):
    print("=" * 30)
    for i, j in enumerate(task_list):
        print(i + 1, j)
    print("=" * 30)


"""показывает список и ждёт завершение"""


def show_message(message=None, mess_action=None):
    if message is not None:
        print(f"задача {message} успешно {mess_action}")
    input("нажмите любую кнопу для продолжени")


"""подтверждение действия"""


def check_confirm(action: str):
    confirm = input("точно?"
                    "\n Y/N")
    if (confirm.capitalize().startswith('') == "Y"
            or 'Д'):
        print(action)
        return False
    else:
        print("отмена")
        return True


"""содзание задач"""


def create_task(task_list, file):
    name_task = input("введите имя задачи")
    if len(name_task) > 0 and name_task not in task_list and name_task is not None:
        content_task = input("введите описание задачи")
        if content_task is not None and len(content_task) >= 1:
            full_task = f"{name_task} {content_task}"
            task_list.append(full_task)
            save_collection(task_list, file_name=file)
            show_message(message=name_task, mess_action='добавлена')


"""изменение задачи"""


def edited_task(task_list):
    show_collection(task_list)
    select_edit = int(input('введите номер задачи: '))
    edit_name = input("новое имя задачи: ")
    task_list[select_edit - 1] = edit_name
    show_message(message=edit_name, mess_action='измененна')


"""удаление элемента"""


def deleated_task(task_list):
    delete_edit = int(input('введите номер задачи: '))
    if not check_confirm('удаление выполненно'):
        task_list.pop(delete_edit - 1)
    show_collection(task_list)
    show_message(message=delete_edit, mess_action="удалена")


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


print("спасибо за вход")
main()
