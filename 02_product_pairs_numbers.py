# Напишите программу, которая найдёт произведение пар чисел списка. 
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.

numbers = input('Введите несколько чисел через пробел: ').split(' ') 
your_list = []
my_list = []

for i in range(len(numbers)):           # вывод введённых чисел списком
    your_list.append(int(numbers[i]))
print(f'Введённый список: {your_list}')

if len(numbers)%2 == 0:
    for i in range(int(len(numbers)/2)):
        multiplication = int(numbers[i]) * int(numbers[len(numbers)-1-i])
        my_list.append(multiplication)
else:
    for i in range(int(len(numbers)/2 + 1)):        # чтобы программа корректно работала при нечётном количестве чисел 
        multiplication = int(numbers[i]) * int(numbers[len(numbers)-1-i])
        my_list.append(multiplication)
print(f'Полученный список: {my_list}')