# Задайте список из вещественных чисел. Напишите программу, которая найдёт
# разницу между максимальным и минимальным значением дробной части элементов, отличной от 0.

import random

length_list = int(input('Введите длину списка: '))
my_list = []

for _ in range(length_list):
    amoun = random.randint(0,3)
    number = round(random.uniform(0, 10), amoun)
    if number == int(number):
        my_list.append(int(number))
    else:
        my_list.append(number)      
print(f'Полученный список: {my_list}')

max_fraction = 0
min_fraction = 999

for item in my_list:                                # Ищем max и min
    if ((item - item//1) < min_fraction) and ((item - item//1) != 0):
        min_fraction = item - item//1
    if (item - item//1) > max_fraction:
        max_fraction = item - item//1
print(f'Разница между максимальным и минимальным значением дробной части элементов: {round(max_fraction - min_fraction, 3)}')
