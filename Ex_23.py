# Задания
# Даны два множества:  А - элементы целые числа от 1 до 20 ( [1. .20] )
# и  В- элементы случайные числа, лежащие в интервале от 0 до 20,
# количество запрашивается с клавиатуры.  Из множества А  выделить  множество С,
# элементы которого - четные числа.
# Определить имеют ли множества B и С одинаковые элементы

from random import randint
A = set(range(1,21))
B = set()
nB = (int(input()))
for i in range(nB):
    B.add(randint(0,50))
print(B)
C = set()
for i in A:
    if i%2==0:
        C.add(i)
print(C)
print(B.intersection(C)) # поиск пересечений(аналогично B & C)
