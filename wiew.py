"""
======================================================
    модуль вывода информации в консоль
======================================================
"""

"""выводит список в консоль"""

def show_collection(task_list):
    print("=" * 30)
    full_task_list = []
    for number, task in enumerate(task_list):
        task_temp = task.split(" | ")
        print(number + 1, task_temp[0])
        full_task_list.append(task_temp[1])
    selected_task = input("выберите номер задачи для просмотра или ENTER для пропуска")
    print("=" * 30)
    if selected_task.isdigit():
        print("~" * 30)
        print(f"{full_task_list[int(selected_task)-1]}")
        print("~" * 30)
    else:
        if selected_task == "":
            print("~" * 30)
        else:
            print('задачи с таким номером нет ')
    print("=" * 30)


"""показывает список и ждёт завершение"""

def show_message(message=None, mess_action=None):
    if message is not None:
        print(f"задача {message} успешно {mess_action}")
    input("нажмите любую кнопу для продолжени")