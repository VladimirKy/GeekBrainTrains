# coding utf-8

n = 1
while not n == 101:
    if n % 10 == 1 and n != 11:
        print(n, "процент")
        n += 1
    elif (1 < n % 10 < 5) and ((n > 21) or (n < 5)) :
        print(n, "процента")
        n += 1
    else:
        print(n, "процентов")
        n += 1
input()
