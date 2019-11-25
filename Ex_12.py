# Задания
# программу, определяющую и выводящую на экран значение и индексы
# первого максимального элемента двумерного массива размером MxN.
# Значения М и N вводятся с клавиатуры, 2<М<10, 2<N<10.
# Элементы массива - случайные числа,
# находящиеся в диапазоне от -9 до 9 включительно.

from random import randint
N = (int(input()))
M = (int(input()))
mas = []
maxim = 0
for i in range(N):
    mas.append([])
    for j in range(M):
        mas[i].append(randint(-9,9)) #заполнение массива
        if mas[i][j] > maxim:
            maxim = mas[i][j]
            max_i = i
            max_j = j
print(mas)
print(maxim)
print(max_i, max_j)

