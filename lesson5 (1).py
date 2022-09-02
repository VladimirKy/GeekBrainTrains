# coding : utf-8

import os
import os.path
import random
import shutil
import sys

import psutil


def print_menu():
    print("Вот, что я могу! Нажми соответствующую цифру:")
    print(" [1] Список файлов и папок в текущей директории")
    print(" [2] Подробная информация о системе  ")
    print(" (имя директории,кодировка, имя пользователя, ")
    print("  количество ядер процессора)")
    print(" [3] Дублирование файла, который ты укажешь")
    print(" [4] Удаление дублированных файлов в директории")
    print(" [5] Завершить работу")


def print_system_info():
    print("Подробная информация о системе:")
    print("Имя директории: ", os.getcwd())
    print("Платформа: ", os.name)
    print("Кодировка: ", sys.getdefaultencoding())
    print("Имя пользователя: ", os.getlogin())
    print("Количество ядер процессора: ", psutil.cpu_count())
    print()


def duplicate_file(dupl_file):
    file_list = os.listdir()
    i = 0
    is_file = False
    while i < len(file_list):
        if dupl_file == file_list[i]:
            shutil.copy(dbl_file, dbl_file + '.dupl')
            print("Файл", dbl_file, " продублирован!")
            is_file = True
            break
        i += 1
    if not is_file:
        print("Неправильно ввел!")


def del_dupl_in_path(path_del):
    if os.path.isdir(path_del):
        os.chdir(del_dupl_dir)
        dupl_list = os.listdir()
        print(dupl_list)
        i = 0
        j = 0
        for i in dupl_list:
            if i.endswith('.dupl'):
                os.remove(i)
                print("Файл ", i, " удален")
                j += 1
        if j == 1:
            print("Удален ", j, " дублированный файл")
        elif (j > 1) and (j < 5):
            print("Удалено ", j, " дублированных файла")
        elif j > 4:
            print("Удалено ", j, " дублированных файлов")
        elif j == 0:
            print("Нет файлов для удаления")
    else:
        print("Неправильный ввод!")


def main():
    print("Привет, программист!")
    user_name = input("Как твоё имя, сынок? ")
    user_id = random.randint(0, 99)
    print("Привет,", user_name, "№ ", user_id)
    is_jobs = 1
    while not is_jobs == 'Y':
        print("№ ", user_id)
        is_jobs = input("Будешь работать или где? (Y/N)")
        if is_jobs == 'Y':
            id_jobs = 1
            while not id_jobs == '5':
                print_menu()
                id_jobs = input()
                if id_jobs == '1':
                    print("Список файлов и папок в текущей директории:")
                    print(os.listdir())
                elif id_jobs == '2':
                    print_system_info()
                elif id_jobs == '3':
                    print(os.listdir())
                    dupl_file = input("Введите имя файла для дублирования: ")
                    duplicate_file(dupl_file)
                elif id_jobs == '4':
                    path_del = input("Введите точный путь для удаления .dupl: ")
                    del_dupl_in_path(path_del)
                elif id_jobs == '5':
                    print("До скорой встречи!")
                else:
                    print("try Again! № ", user_id)
        elif is_jobs == 'N':
            for i in range(0, user_id):
                print("Бездельник!")
        else:
            print("Try again, please!")
    input()


if __name__ == "__main__":
    main()
