# Задача 3. Напишите программу, которая по заданному номеру четверти, показывает диапазон возможных координат точек в этой четверти (x и y).

quarter = int(input("Введите номер координатной четверти (от 1 до 4): "))

if 1 <= quarter <= 4:
    if quarter == 1:
        print("Диапазон возможных координат в I координатной четверти: x > 0 и y > 0")
    elif quarter == 2:
        print("Диапазон возможных координат в II координатной четверти: x < 0 и y > 0")
    elif quarter == 3:
        print("Диапазон возможных координат в III координатной четверти: x < 0 и y < 0")
    else:
        print("Диапазон возможных координат в IV координатной четверти: x > 0 и y < 0")
else:
    print("Такой координатной четверти не существует")