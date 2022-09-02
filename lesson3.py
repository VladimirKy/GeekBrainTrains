# coding : utf-8

import os
import sys
import psutil
import random

# комментарий

print("Привет, программист!")
user_name = input("Как твое имя, сынок? ")
user_id = random.randint(0, 99)
print("Привет,", user_name, "№ ", user_id)
is_jobs = 1
while not is_jobs == 'Y':
    print("№ ", user_id)
    is_jobs = input("Будешь работать или где? (Y/N)")
    if is_jobs == 'Y':
        print("Вот, что я могу! Нажми соответствующую цифру:")
        print(" [1] Список файлов и папок в текущей директории")
        print(" [2] Подробная информация о системе  ")
        print(" (имя директории,кодировка, имя пользователя, ")
        print("  количество ядер процессора)")        
        print(" [3] Завершить работу")
        id_jobs = 1
        while not id_jobs == '3':
            id_jobs = input()
            if id_jobs == '1':
                print("Список файлов и папок в текущей директории:")
                print(os.listdir())
                print()
                print("Вот, что я могу! Нажми соответствующую цифру:")
                print(" [1] Список файлов и папок в текущей директории")
                print(" [2] Подробная информация о системе  ")
                print(" (имя директории,кодировка, имя пользователя, ")
                print("  количество ядер процессора)")                
                print(" [3] Завершить работу")
            elif id_jobs == '2':
                print("Подробная информация о системе:")
                print("Имя директории: ", os.getcwd())
                print("Платформа: ", os.name)
                print("Кодировка: ", sys.getdefaultencoding())
                print("Имя пользователя: ", os.getlogin())
                print("Количество ядер процессора: ", psutil.cpu_count())
                print()
                print("Вот, что я могу! Нажми соответствующую цифру:")
                print(" [1] Список файлов и папок в текущей директории")
                print(" [2] Подробная информация о системе  ")
                print(" (имя директории,кодировка, имя пользователя, ")
                print("  количество ядер процессора)")                
                print(" [3] Завершить работу")
            elif id_jobs == '3':
                print("До скорой встречи!")
            else:
                print("try Again! № ", user_id)
    elif is_jobs == 'N':
        for i in range(0, user_id):
            print("Бездельник!")
    else:
        print("Try again, please!")
input()