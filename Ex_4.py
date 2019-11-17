# Задание:
# Даны число n, последовательность чисел a1...an.
# Найти номер первого четного члена последовательности.
# Если четных членов нет, то ответом должно быть число 10.

from random import randint
n = (int(input()))
seq = [0] * n
i = 0
while i < n:
    seq[i] = randint(1, 20)
    i +=1
print(seq)
for i in seq:
    if i%2 == 0:
        print(seq.index(i))
        break
    else:
        print(10)
