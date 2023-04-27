import shutil
import os
import platform

def create_folder(name):
    name = input('Please give name to the folder you would like to create: ')
    return os.mkdir(name)

def remove_folder():
    name = input('Please specify name  of the folder you would like to delete: ')
    os.rmdir(name)

def copy_folder():
    source_path = input('Please specify name  of the folder or file you would like to copy: ')
    destination_path = input('Please specify destination path: ')
    shutil.copy2(source_path, destination_path)

def list_folder_content():
    # print(os.listdir(os.getcwd()))
    return os.listdir(os.getcwd())

# 5
def dirs_only():
    directory = os.getcwd()
    with os.scandir(directory) as files:
        list_dirs = [file for file in files if file.is_dir()]
    print(list_dirs)

# 6
def files_only():
    with os.scandir() as files:
        list_files = [file for file in files if file.is_file()]
    print(list_files)


# 7
def sys_info():
    print(platform.platform())
    return platform.platform()

sys_info()
# 8
def app_creator():
    creators_name = 'Пицуков Михаил'
    print(f"Этот код выполнил {creators_name}.")
    return  creators_name

# 9
def play_victory():
    from victory import victory as vc
    vc()

# 11
def cd_dir():
    path = input("Please enter your desired path: ")
    os.chdir(path)
    print(os.getcwd())

def play_menu():
    print('Hi! Welcome to our project menu.',
    '\n1 - создать папку;',
    '\n2 - удалить файл/папку;',
    '\n3 - копировать файл/папку;',
    '\n4- просмотр содержимого рабочей директории;',
    '\n5- посмотреть только папки;',
    '\n6- посмотреть только файлы;',
    '\n7- просмотр информации об операционной системе;',
    '\n8- создатель программы;',
    "\n9- играть в викторину;",
    "\n10- мой банковский счет;",
    "\n11- смена рабочей директории *необязательный пункт;",
    "\n12- выход.\n")

#
# choice = int(input('Please chose your action from the list below: '))
#
# if choice == 1:
#     create_folder()
#
# elif choice == 2:
#     remove_folder()
#
# elif choice == 3:
#     copy_folder()
#
# elif choice == 4:
#     list_folder_content()
#
# elif choice == 5:
#     dirs_only()
#
# elif choice == 6:
#     files_only()
#
# elif choice == 7:
#     sys_info()
#
# elif choice == 8:
#     app_creator()
# elif choice == 9:
#    play_victory()
# elif choice == 10:
#     pass
# elif choice == 11:
#     cd_dir()
# elif choice == 12:
#     print('Bye!')
#     exit()