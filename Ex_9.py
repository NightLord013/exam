# Задание:
# В заданной строке удалить все цифры.
# Если цифр в строке не было введено, то вывести сообщение об этом

s = input()
st = []
q = 0
for i in s:
    if i.isalpha():
        st.append(i)
    elif i == " ":
        st.append(i)
    elif i.isdigit():
        q += 1
        continue
if q == 0:
    print("В строке нет цифр")
else:
    print("".join(st))
            
