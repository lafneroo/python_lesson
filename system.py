import os
import sys
import platform


os_name = platform.system()
os_version = platform.version()
os_arch = platform.architecture()[0]
processor = platform.processor()
py_ver = platform.python_version()
login = os.getlogin()
cur_dir = os.getcwd()

build = os_version[5:]

list_tasks = [os_name, os_version, os_arch, build, processor, py_ver]
list_os = []
is_running = True

sys.stdout.write("добро пожаловать в 'syscheker'\n")
while is_running:
    for task in range(len(list_tasks)):
        list_os.append(list_tasks[task])

    choice_user =  input("варианты проверки: \n"
                              "1 - Операционная система\n"
                              "2 - версия системы\n"
                              "3 - архитектура системы\n"
                              "4 - билд\n"
                              "5 - процессор\n"
                              "6 - версия python\n"
                              "7 - <UNK> <UNK>\n")
    match choice_user:
        case "1":
            sys.stdout.write(f"{list_os[0]}\n")
        case "2":
            sys.stdout.write(f"{list_os[1]}\n")
        case "3":
            sys.stdout.write(f"{list_os[2]}\n")
        case "4":
            sys.stdout.write(f"{list_os[3]}\n")
        case "5":
            sys.stdout.write(f"{list_os[4]}\n")
        case "6":
            is_running = False
        case _:
            sys.stdout.write("неверная команда ")
