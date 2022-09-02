# coding : utf-8

def isInt(duration):
    try:
        int(duration)
        return True
    except ValueError:
        return False

is_jobs = 1
while is_jobs > 0:
    duration = input("Введите время в секундах или стоп чтобы завершить выполнение программы: ")
    if (isInt(duration) == True) and (int(duration) > 0):
        d = int(duration) // 86400
        h = (int(duration) // 3600) % 24
        m = (int(duration) // 60) % 60
        s = int(duration) % 60
        if int(duration) < 60:
            print(s, "сек")
        elif int(duration) < 3600:
            print (m, "мин", s, "сек")
        elif int(duration) < 86400:
            print(h, "час", m, "мин", s, "сек")
        else:
            print(d, "дн", h, "час", m, "мин", s, "сек")
    elif duration == "стоп":
        is_jobs = 0
    elif (isInt(duration) == False) or (int(duration) <= 0):
        print("Заново попробуй!")
input()
