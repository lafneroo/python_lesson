"""
    Точка входа приложения Task manager
    V0.0.4
    --- description ---
- [х] создать разделение меню/ответ
- [ ] оптимизировать код
"""
print("спасибо за вход")

is_running = True
collection = [1234]

"""выводит список в консоль"""
def ShowCollection(task_list):
    print("=" * 30)
    for key, item in enumerate(task_list):
        print(key + 1, item)
    print("=" * 30)

"""показывает список и ждёт завершение"""
def ShowMassage(Massage = None, mess_action = None  ):
    if Massage is not None:
        print(f"задача {Massage} {mess_action}")
        ShowCollection(collection)
    input("нажмите любую кнопу для продолжени")

"""подтеврждение действия"""
def chek_confirm(action: str):
    confirm = input("точно?"
                    "\n Y/N")
    if (confirm.capitalize().startswith('') == "Y"
            or 'Д'):
        print(action)
        return False
    else:
        print("отмена")
        return True


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
            ShowMassage()
        case "2":  #добавление в список
            task_name = input('введите название задачи: ')
            collection.append(task_name)
            ShowMassage(task_name, 'добавленна')
        case "3":  #изменение элемента
            ShowCollection(collection)
            select_edit = int(input('введите номер задачи: '))
            edit_name = input("новое имя задачи: ")
            collection[select_edit - 1 ] = edit_name
            ShowMassage(edit_name, 'измененна')
        case "4":  #удаление элемента
            ShowCollection(collection)
            delete_edit = int(input('введите номер задачи: '))
            if not chek_confirm('удаление выполненно'):
                collection.pop(delete_edit - 1)
            ShowMassage(delete_edit, 'удалена')
        case "5":  #завершение цикла
            is_running = chek_confirm('отключение...')
        case _:  #неверная команда
            print('неверная команда')
            ShowMassage()