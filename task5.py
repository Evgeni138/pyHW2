# Реализуйте алгоритм перемешивания списка.
import random

spisok = [1, 2, 3, 4, 5, 6, 7]
# random.shuffle(spisok)
print(spisok)
for i in range(len(spisok)):
    j = random.randrange(0, 7)
    temp = spisok[i]
    spisok[i] = spisok[j]
    spisok[j] = temp
print(spisok)