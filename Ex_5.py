# Задание:
# Даны натуральные числа n, a1...an.
# Определить количество членов последовательности a1...an,
# имеющих четные порядковые номера и являющихся нечетными числами.
# Если условие не выполняется вывести сообщение об этом.

from random import randint
n = (int(input()))
seq = [0] * n
i = 0
while i < n:
    seq[i] = randint(1, 20)
    i += 1
print(seq)
for i in seq:
    if (i%2 == 1) and (seq.index(i)%2 == 0) and (seq.index(i) > 0):
        print (i)
