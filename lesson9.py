# coding utf-8

i = 0
j = 0
# k = 0 // переменная для перебора в цикле всех чисел из списка для разложения на цифры
m = 0
n = 0
aa_mount = 0
aaa_mount = 0
odd = [i for i in range(1, 1001, 2)]  # от 0 до 500 номера элементов
for j in range(0, 500):
    odd[j] = odd[j] ** 3
print(odd)
# x = [int(k) for k in str(odd[3])] // разложение на цифры числа из списка
# print(x) // вывод на экран этих цифр
# a_mount = sum(map(int, list(str(odd[3])))) // сумма разложенных цифр числа из списка
# print(a_mount) // вывод на экран этой суммы
for m in range(0, 500):
    if sum(map(int, list(str(odd[m])))) % 7 == 0:
        aa_mount += odd[m]
#        print(odd[m], "делится нацело на 7!") // скрываем вывод на экран для отладки
#    else: // --"--
#        print(odd[m], "не делится нацело на 7") // --"--
print("a. Сумма тех чисел списка, сумма цифр которых делится на 7 без остатка, = ", aa_mount)
for n in range(0, 500):
    odd[n] += 17
    if sum(map(int, list(str(odd[n])))) % 7 == 0:
        aaa_mount += odd[n]
#        print(odd[n], "делится нацело на 7!") // скрываем вывод на экран для отладки
#    else: // --"--
#        print(odd[n], "не делится нацело на 7") // --"--
print("b. Сумма чисел списка, сложенных с 17 и сумма цифр которых делится на 7 без остатка, = ", aaa_mount)
print("c. Задача под пунктом b решена без создания нового списка")
input()