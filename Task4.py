'''
Задание 4 Задайте список из N элементов, заполненных числами из промежутка [-N, N].
Найдите произведение элементов на позициях a и b.
Значения N, a и b вводит пользователь с клавиатуры.
'''

n = int(input('Введите кол-во элементов: '))
a = int(input('Введите позицию элемента a: '))
b = int(input('Введите позицию элемента b: '))
list = []

for i in range(-n, n+1):
    list.append(i)
result = list[a] * list[b]
print(f'Вывод элементов в списке {list}')
print(f'Произведение элементов на позициях {a} и {b} равно {result}')

