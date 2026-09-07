"""
    Точка входа приложения Task manager
    V0.0.3
    --- description ---
- [ ] реализовать редактирование задач
- [ ] реализовать удаление задач
"""
print("спасибо за вход")

is_running = True
collection = []

while is_running  :
    print('1 - посмотреть задачи'
          '\n2 - добавить задачу'
          '\n3 - редактирование'
          '\n4 - снять задачу'
          '\n5 - выход')
    choice_user = input("введите команду: ")

    match choice_user:
        case "1":
            for key, item in enumerate(collection):
                print(key + 1, item)
        case "2":
            task_name = input('введите название задачи: ')
            collection.append(task_name)
        case "3":
            for key,item in enumerate(collection):
                print(key + 1, item)
            select_edit = int(input('введите номер задачи: '))
            edit_name = input("новое имя задачи: ")
            collection[select_edit - 1 ] = edit_name
        case "4":
            for key, item in enumerate(collection):
                print(key + 1, item)
            delete_edit = int(input('введите номер задачи: '))
            collection.pop(delete_edit - 1)
        case "5":
            print("отключение...")
            is_running = False
        case _:
            print('неверная команда')

