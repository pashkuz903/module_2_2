# Ввод значений от пользователя
first = int(input('Введите 1-ое числовое значение: '))
second = int(input('Введите 2-ое числовое значение: '))
third = int(input('Введите 2-ое числовое значение: '))
# Логически условия
if first == second and first == third:
    print('Вы ввели 3 одинаковых числа')
elif first == second or first == third or second == third:
    print('Вы ввели 2 одинаковых числа')
else: print('Вы ввели 0 одинаковых чисел')