"""
    Точка входа приложения Task manager
    V0.0.4
    --- description ---
- [х] создать разделение меню/ответ
- [ ] оптимизировать код
"""
print("спасибо за вход")

is_running = True
collection = []

"""выводит список в консоль"""
def ShowCollection(task_list):
    print("=" * 30)
    for key, item in enumerate(task_list):
        print(key + 1, item)
    print("=" * 30)
"""показывает список и ждёт завершение"""
def ShowMassage(flag = bool, Massage = None):
    if flag:
        print(f"задача {Massage} добавлена")
        ShowCollection(collection)
    input("нажмите любую кнопу для продолжени")


while is_running  :
    print('1 - посмотреть задачи'
          '\n2 - добавить задачу'
          '\n3 - редактирование'
          '\n4 - снять задачу'
          '\n5 - выход')
    choice_user = input("введите команду: ")

    match choice_user:
        case "1":  #просмотр списка
            ShowCollection(collection)
            input("нажмите любую кнопу для продолжени")
        case "2":  #добавление в список
            task_name = input('введите название задачи: ')
            collection.append(task_name)
            print(f"задача {task_name} добавлена")
            ShowCollection(collection)
            input("нажмите любую кнопу для продолжени")
        case "3":  #изменение элемента
            ShowCollection(collection)
            select_edit = int(input('введите номер задачи: '))
            edit_name = input("новое имя задачи: ")
            collection[select_edit - 1 ] = edit_name
            input("нажмите любую кнопу для продолжени")
        case "4":  #удаление элемента
            ShowCollection(collection)
            delete_edit = int(input('введите номер задачи: '))
            collection.pop(delete_edit - 1)
            input("нажмите любую кнопу для продолжени")
        case "5":  #завершение цикла
            print("отключение...")
            is_running = False
        case _:  #неверная команда
            print('неверная команда')
            input("нажмите любую кнопу для продолжени")