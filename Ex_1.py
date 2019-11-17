# Задание:
# Даны целые числа a, n, x1...xn (n>0).
# Определить, каким по счету (индекс) идет в последовательности x1...xn член,
# равный а. Если такого члена нет, то ответом должно быть число 10.
from random import randint
a = (int(input()))
n = (int(input()))
i = 0
seq = [0] * n
while i < n:
    seq[i] = randint(1, 20)
    i += 1
print(seq)
if a in seq:
    print(seq.index(a))
else:
    print(10)
