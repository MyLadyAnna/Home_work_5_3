# Напишите программу, которая будет преобразовывать десятичное число в двоичное.

number = int(input('Введите целое число:'))
my_list = []

while number > 1:
    result = number % 2
    my_list.append(result)
    number //= 2
else:
    my_list.append(number)

my_list.reverse()     # реверс списка

print(*my_list, sep = '')