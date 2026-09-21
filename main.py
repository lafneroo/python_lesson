"""
    Точка входа приложения Task manager
    V0.0.5
    --- description ---
- [ ] уменьшить долю структурного кода
- [ ] сделать систему сохранений
"""



"""основной цикл"""
def main():
    collection = load_collection([])
    name_file = "saves.txt"
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
                ShowCollection(collection)
                ShowMassage(collection)
            case "2":  # добавление в список
                task_name = input('введите название задачи: ')
                collection.append(task_name)
                save_collection(collection, name_file)
                ShowMassage(task_name, 'добавлена')
            case "3":  # изменение элемента
                edited_task(collection)
                save_collection(collection, name_file)
            case "4":  # удаление элемента
                ShowCollection(collection)
                deleated_task(collection)
                save_collection(collection, name_file)
            case "5":  # завершение цикла
                is_running = chek_confirm('отключение...')
            case _:  # неверная команда
                print('неверная команда')
                ShowMassage()

"""выводит список в консоль"""
def ShowCollection(task_list):
    print("=" * 30)
    for i, j in enumerate(task_list):
        print(i + 1, j)
    print("=" * 30)

"""показывает список и ждёт завершение"""
def ShowMassage(task_list = None,  Massage = None, mess_action = None ):
    if Massage is not None:
        print(f"задача {Massage} {mess_action}")
        ShowCollection(task_list)
    input("нажмите любую кнопу для продолжени")

"""подтверждение действия"""
def chek_confirm(action: str ):
    confirm = input("точно?"
                    "\n Y/N")
    if (confirm.capitalize().startswith('') == "Y"
            or 'Д'):
        print(action)
        return False
    else:
        print("отмена")
        return True
""""""

"""содзание задач"""
def create_task(task_list):
    name_task = input("введите имя задачи")
    if name_task != name_task not in task_list and name_task is not None:
        content_task = input("введите описание задачи") 



"""изменение задачи"""
def edited_task(task_list):
    ShowCollection(task_list)
    select_edit = int(input('введите номер задачи: '))
    edit_name = input("новое имя задачи: ")
    task_list[select_edit - 1] = edit_name
    ShowMassage(edit_name, 'измененна')

"""удаление элемента"""
def deleated_task(task_list):
    delete_edit = int(input('введите номер задачи: '))
    if not chek_confirm('удаление выполненно'):
        task_list.pop(delete_edit - 1)
    ShowCollection(task_list)
    ShowMassage(delete_edit, "удалена")

"""загрузка"""
def load_collection(task_list, file_name):
    task_list = []
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