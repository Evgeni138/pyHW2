# Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
#
# Пример:
#
# - 6782 -> 23
# - 0,56 -> 11

def sum(number):
    result = 0
    number = str(number)
    for i in range(0, len(number)):
        if number[i].isdigit():
            result += int(number[i])
    return result

print(sum(67.025))
