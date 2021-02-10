"""Задачи из раздела 1 'Операторы. Переменные. Типы данных. Условия' курса"""

'''Определение качества сна'''

A = int(input('Введите число '))
B = int(input('Введите число '))
H = int(input('Введите число '))
if B >= H >= A:
    print("Это нормально")
elif H < A:
    print("Недосып")
elif H > B:
    print("Пересып")

'''Опредедение года'''

year = int(input('Введите число 1900≤n≤3000 '))
if 3000 >= year >= 1900:
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        print("Високосный")
    else:
        print("Обычный")

'''Площадь треугольника по трем сторонам'''

a_triangle = int(input(''))
b_triangle = int(input(''))
c_triangle = int(input(''))
p_triangle = (a_triangle+b_triangle+c_triangle)/2
s_triangle = (p_triangle*(p_triangle-a_triangle)*(p_triangle-b_triangle)*(p_triangle-c_triangle))**(1/2)
print(s_triangle)

'''Принадлежность интервалу'''

x = int(input(''))
print((-15 < x <= 12) or (14 < x < 17) or (19 <= x))

'''Калькулятор'''

value1 = float(input(''))
value2 = float(input(''))
action = input('')
if (action == "/" or action == "mod" or action == "div") and value2 == 0:
    print("Деление на 0!")
elif action == "+":
    print(value1+value2)
elif action == "-":
    print(value1-value2)
elif action == "/":
    print(value1/value2)
elif action == "*":
    print(value1*value2)
elif action == "mod":
    print(value1 % value2)
elif action == "pow":
    print(value1**value2)
elif action == "div":
    print(value1//value2)

'''Жители страны Малевии часто экспериментируют с планировкой комнат. Комнаты бывают треугольные, прямоугольные и круглые. Чтобы быстро вычислять жилплощадь, требуется написать программу, на вход которой подаётся тип фигуры комнаты и соответствующие параметры, которая бы выводила площадь получившейся комнаты.
Для числа π в стране Малевии используют значение 3.14.'''

type = input('')
if type == 'треугольник':
    a = float(input(''))
    b = float(input(''))
    c = float(input(''))
    p = (a + b + c) / 2
    print((p * (p - a) * (p - b) * (p - c)) ** (1 / 2))
elif type == 'прямоугольник':
    a = float(input(''))
    b = float(input(''))
    print(a * b)
elif type == 'круг':
    r = float(input(''))
    print(3.14 * (r ** 2))

'''Напишите программу, которая получает на вход три целых числа, по одному числу в строке, и выводит на консоль в три строки сначала максимальное, потом минимальное, после чего оставшееся число.

На ввод могут подаваться и повторяющиеся числа.'''

number_1 = int(input(''))
number_2 = int(input(''))
number_3 = int(input(''))
all_numbers = [number_1, number_2, number_3]
print(max(all_numbers))
print(min(all_numbers))
for i in range(3):
    if i != all_numbers.index(max(all_numbers)) and i != all_numbers.index(min(all_numbers)):
        print(all_numbers[i])
        break

'''Робот'''

number = int(input(''))
if 0 <= number <= 1000:
    if number != 0 and number != 1000 and number % 100 != 11 and number % 10 == 1 or 0 < number < 99 and number != 11 and number % 10 == 1:
        print(number, "программист")
    elif number != 0 and number != 1000 and number % 100 != 12 and number % 10 == 2 or 0 < number < 99 and number != 12 and number % 10 == 2:
        print(number, "программиста")
    elif number != 0 and number != 1000 and number % 100 != 13 and number % 10 == 3 or 0 < number < 99 and number != 13 and number % 10 == 3:
        print(number, "программиста")
    elif number != 0 and number != 1000 and number % 100 != 14 and number % 10 == 4 or 0 < number < 99 and number != 14 and number % 10 == 4:
        print(number, "программиста")
    else:
        print(number, "программистов")


'''Билет'''

ticket = input('')
if int(ticket[0]) + int(ticket[1]) + int(ticket[2]) == int(ticket[3]) + int(ticket[4]) + int(ticket[5]):
    print('Счастливый')
else:
    print('Обычный')
