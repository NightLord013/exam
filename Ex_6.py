# Задание:
# Написать программу, которая выводит введенную строку в обратном порядке,
# причем каждое слово с новой строки. Вывод оформить в телеграфном стиле,
# т.е. каждая буква появляется с некоторой задержкой.
# Для этого использовать функцию delay(N), где N–время задержки.
import time
s = input()
for i in reversed(s):
    print(i[::-1], end="")
    time.sleep(1) # задержка 1 секунда
    if i == " ":
        print("\n", end="")