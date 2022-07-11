# Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.
#
# Пример:
#
# - пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)




def fuctorial(number):
    if number == 0:
        print(1)
    else:
        result = 1
        for i in range(number):
            result *= (i+1)
        return result


num = int(input('--> ',))
result = []
for i in range(1, num + 1):
    result.append(fuctorial(i))
print(result)
