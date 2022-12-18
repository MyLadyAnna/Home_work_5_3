# Напишите программу, которая найдёт произведение пар чисел списка. 
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.

import random

length_list = int(input('Введите длину списка: '))
my_list = []
result_list = []

for _ in range(length_list):                # вывод рандомного списка
    my_list.append(random.randint(1, 10))

print(f'Сгенерированный список: {my_list}')

if len(my_list)%2 == 0:
    for i in range(int(len(my_list)/2)):
        multiplication = int(my_list[i]) * int(my_list[len(my_list)-1-i])
        result_list.append(multiplication)
else:
    for i in range(int(len(my_list)/2 + 1)):        # чтобы программа корректно работала при нечётном количестве чисел
        multiplication = int(my_list[i]) * int(my_list[len(my_list)-1-i])
        result_list.append(multiplication)

print(f'Полученный список: {result_list}')