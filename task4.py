# Задача 4. Напишите программу, которая на вход принимает число (N), а на выходе показывает все чётные числа от 1 до N.

import math

number = float(input("Введите число N: "))

number = abs(number)
x = math.floor(number)

for i in range (1, x + 1):
    if i % 2 == 0:  
        print(i, end = " ")