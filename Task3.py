'''
Задание 3 Задайте список из n чисел последовательности (1+1/n)^n и выведите на экран их сумму,
округлённую до трёх знаков после точки.

Пример:

Для n = 6 -> 14.072
while i < (n + 1):
    a.append((1 + 1/i)**i)
    i += 1
for index in range(0,n):
    sum = sum + a[index]
'''
n = int(input('Введите число: '))
a = []
sum = 0
i = 1
while i < (n + 1):
    a.append((1 + 1/i)**i)
    i += 1
for index in range(0,n):
    sum = sum + a[index]
print(a)
print(round(sum,3))
