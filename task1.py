day = int(input("Введите номер дня недели: "))

if 1 <= day <= 7:
    if day == 1:
        print("Понедельник")
    elif day == 2:
        print("Вторник")
    elif day == 3:
        print("Среда")
    elif day == 4:
        print("Четверг")
    elif day == 5:
        print("Пятница")
    elif day == 6:
        print("Суббота")
    else:
        print("Воскресенье")
else:
    print("Такого дня недели не существует")