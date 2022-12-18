# Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов

def fibonacci(n):           # фун Фибоначчи
    if n in [1, 2]:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)

def negafibonacci(n):           # фун негафибоначчи
    if n == 1:
        return 1
    elif n == 2:
        return -1
    else:
        return negafibonacci(n-2) - negafibonacci(n-1)
        
number = int(input('Введите целое число: '))

list_result = []

for i in range(1, number + 1):
   list_result.append(fibonacci(i))
   list_result.insert(0, negafibonacci(i))        #ставит в начало списка
list_result.insert(number,0)
print(list_result)


