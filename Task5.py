'''
Задание 5 Реализуйте алгоритм перемешивания списка.
'''
arr = [10, 2, 3, 4, 5, 6]
print(f'Изначальный список: {arr}')

lengthOfArr = len(arr)
import random

for i in range(lengthOfArr):
    a = random.randint(0, lengthOfArr - 1)
    b = arr.pop(a)
    arr.append(b)
print(f'Новый список: {arr}')