# Задание:
# Ввести строку.
# Получить все символы, расположенные после первого двоеточия (:)

s = input()
if ":" in s:
    ind = s.index(":") #получает номер индекса символа ":"
    print(s[ind+1:])
else:
    pass