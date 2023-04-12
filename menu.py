import shutil
import os
import platform

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


choice = int(input('Please chose your action from the list below: '))

if choice == 1:
    name = input('Please give name to the folder you would like to create: ')
    os.mkdir(name)
elif choice == 2:
    name = input('Please specify name  of the folder you would like to delete: ')
    os.rmdir(name)
elif choice == 3:
    source_path = input('Please specify name  of the folder or file you would like to copy: ')
    destination_path = input('Please specify destination path: ')
    shutil.copy2(source_path, destination_path)
elif choice == 4:
    # path = os.getcwd()
    # print(path)
    print(os.listdir(os.getcwd()))
elif choice == 5:
    pass
elif choice == 6:
    pass
elif choice == 7:
    print(platform.platform())
elif choice == 8:
    pass
elif choice == 9:
    pass
elif choice == 10:
    pass
elif choice == 11:
    pass