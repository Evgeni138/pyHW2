# Задайте список из N элементов, заполненных числами из промежутка [-N, N].
# Найдите произведение элементов на указанных позициях.
# Позиции хранятся в файле file.txt в одной строке одно число.
n = int(input('--> ',))
array = [-n]
for i in range(1, 2 * n + 1):
    array.append(- n + i)
print(array)
print('Введите позиции двух чисел для вычисления произведения')
a = int(input('a --> ',))
b = int(input('b --> ',))
print(array[a - 1] * array[b - 1])