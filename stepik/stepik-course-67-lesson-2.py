"""Задачи из раздела 2 'Циклы. Строки. Списки' курса"""

'''Вывод после первого введенного нуля суммы полученных на вход чисел'''

number_sum = 0
number = int(input(''))
while number != 0:
    number_sum += number
    number = int(input(''))
print(number_sum)

'''Программа должна считывать размеры команд (два положительных целых числа aa и bb, каждое число вводится на отдельной строке) и выводить наименьшее число dd, которое делится на оба этих числа без остатка'''

a = int(input(''))
b = int(input(''))
i = 0
while a > 0 and b > 0:
    i += 1
    if i % a == 0 and i % b == 0:
        break
print(i)

'''Напишите программу, которая считывает целые числа с консоли по одному числу в строке.

Для каждого введённого числа проверить:
если число меньше 10, то пропускаем это число;
если число больше 100, то прекращаем считывать числа;
в остальных случаях вывести это число обратно на консоль в отдельной строке.

'''

while True:
    num1 = int(input(''))
    if num1 < 10:
        continue
    elif num1 > 100:
        break
    else:
        print(num1)

'''Таблица умножения'''

factor1 = int(input(''))
factor2 = int(input(''))
factor3 = int(input(''))
factor4 = int(input(''))

if (factor2 <= 10 and factor4 <= 10) and (factor1 <= factor2) and (factor3 <= factor4):
    print(end='\t')
    for k in range(factor3, factor4 + 1):  # вывод вторых множителей
        print(k, end='\t')
    print()
    for i in range(factor1, factor2 + 1):
        print(i, end='\t')  # вывод первых множителей
        for k in range(factor3, factor4 + 1):
            print(k * i, end='\t')
        print()

'''Среднее арифметическое чисел, кратных 3, на заданном отрезке'''

number1 = int(input(''))
number2 = int(input(''))
sum = 0
quantity = 0
for i in range(number1, number2 + 1):
    if i % 3 == 0:
        sum += i
        quantity += 1
    else:
        continue
print(sum / quantity)

'''Процентное соотношение GC в геномной последовательности'''

sequence = input('')
g = sequence.upper().count('G')
c = sequence.upper().count('C')
print(100*(g + c)/len(sequence))

'''Вывод символов'''

s = 'abcdefghijk'
print(s[-1:-10:-2]) # интервал от [-1,-10) с шагом -2

'''Сжатие последовательности ДНК'''

dna = input('')
dna2 = ''
count = 0
if len(dna) == 1:   # строка состоит из одного символа
    dna2 += dna[0] + '1'
else:    # строка состоит из нескольких символов
    for i in range(0, len(dna) - 1):    # перебор символов
        if i != len(dna) - 2:  # анализ всех символов, кроме последней пары
            if dna[i] == dna[i + 1]:    # совпадение символов
                count += 1
            else:
                dna2 += dna[i] + str(count + 1)    # добавление следующего значения к новой последовательности
                count *= 0  # обнуление счетчика при несовпадении символов
        else:
            if dna[len(dna) - 2] == dna[len(dna) - 1]:  # анализ последней пары
                count += 2
                dna2 += dna[i] + str(count)    # добавление финальных значений при совпадении
            else:
                dna2 += dna[len(dna) - 2] + "1" + dna[len(dna) - 1] + "1"   # добавление финальных значений при несовпадении
print(dna2)

'''Вывод суммы чисел'''

integers = [int(i) for i in input().split()]    # ввод строки с целыми числами, разделитель - пробел
sum_integers = 0
for i in range(0, len(integers)):
    sum_integers += integers[i]
print(sum_integers)

'''Сумма соседних чисел от заданного'''

integers_2 = [int(i) for i in input().split()]
sum_integers_2 = []
for i in range(0, len(integers_2)):
    if len(integers_2) == 1:
        sum_integers_2.append(integers_2[i])
    elif len(integers_2) == 2:
        sum_integers_2.append(integers_2[1]*2)
        sum_integers_2.append(integers_2[0]*2)
        break
    elif i != len(integers_2) - 1:
        sum_integers_2.append(integers_2[i-1] + integers_2[i+1])
    else:
        sum_integers_2.append(integers_2[i-1] + integers_2[0])
print(*sum_integers_2)  # вывод списка строкой

'''Вывод повторяющихся чисел'''

integers_3 = [int(i) for i in input().split()]
integers_3_copy = []
integers_3.sort()   # сортировка по возрастанию элементов списка
for i in range(0, len(integers_3)):
    if integers_3.count(integers_3[i]) > 1:
        integers_3_copy.append(integers_3[i])     # добавление каждого повторяющегося элемента в новый список
i = 0
while i < len(integers_3_copy)-1:   # длина списка меняется во время выполнения цикла, поэтому реализация не через цикл for
    if integers_3_copy[i] == integers_3_copy[i+1]:
        del integers_3_copy[i]    # удаление повторяющегося элемента в новом списке по индексу, индекс следующего элемента равен i
    else:
        i += 1
print(*integers_3_copy)  # вывод нового списка строкой

'''Считывание с консоли чисел (по одному в строке), пока их сумма не будет равна 0, с выводом суммы квадратов'''

check_sum = int(input(''))
final_sum = check_sum**2
while check_sum != 0:
    d = int(input(''))
    check_sum += d
    final_sum += d**2
print(final_sum)

'''Число повторяется столько раз, чему равно, вывод n чисел'''

n = int(input(''))
repeat = []
for i in range(1,n+1):
    for k in range(1, i+1):
        repeat.append(i)
print(*repeat[0:n])

'''Позиции числа x в переданном списке lst'''

lst = [int(i) for i in input().split()]
x = int(input(''))
check = False
for i in range(0, len(lst)):
    if lst[i] == x:
        print(i, end='\t')
        check = True
    elif i == len(lst) - 1 and check != True:
        print('Отсутствует')

'''Двумерный список'''

'''Ввод двумерного списка:

A = []
for i in range(n):
 A.append(list(map(int, input().split())))
 
Или, без использования сложных вложенных вызовов функций:
A = []
for i in range(n):
 row = input().split()
 for i in range(len(row)):
 row[i] = int(row[i])
 A.append(row)
 
Можно сделать то же самое и при помощи генератора:
A = [ list(map(int, input().split())) for i in range(n)]'''

'''Изменение элементов матрицы'''

import copy

matrix = []
row = []

while row != ['end']:  # ввод матрицы
    row = [i for i in input().split()]
    if row == ['end']:
        break
    else:
        for i in range(0, len(row)):
            row[i] = int(row[i])
        matrix.append(row)

matrix_2 = copy.deepcopy(matrix)

if len(matrix) == 1 and len(matrix[0]) == 1:   # матрица из одного элемента
    matrix_2[0][0] = matrix[0][0]*4
elif len(matrix[0]) == 1 and len(matrix) != 1:   # матрица из одного столбца
    for i in range(len(matrix)):
        if i == 0:  # первый элемент стоблца
            matrix_2[0][0] = matrix[1][0] + matrix[len(matrix) - 1][0] + 2*matrix[0][0]
        elif i == len(matrix) - 1:  # последний элемент столбца
            matrix_2[len(matrix) - 1][0] = matrix[0][0] + matrix[len(matrix) - 2][0] + 2*matrix[len(matrix) - 1][0]
        else:   # промежуточные элементы столбца
            matrix_2[i][0] = 2*matrix[i][0]+matrix[i+1][0]+matrix[i-1][0]
elif len(matrix[0]) != 1 and len(matrix) == 1:   # матрица из одной строки
    for j in range(len(matrix[0])):
        if j == 0:  # первый элемент строки
            matrix_2[0][0] = matrix[0][0] * 2 + matrix[0][1] + matrix[0][len(matrix[0]) - 1]
        elif j == len(matrix[0]) - 1:  # последний элемент строки
            matrix_2[0][j] = matrix[0][j] * 2 + matrix[0][j-1] + matrix[0][0]
        else:   # промежуточные элементы строки
            matrix_2[0][j] = matrix[0][j] * 2 + matrix[0][j+1] + matrix[0][j-1]
else:   # матрица 2х2 и более
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if i == 0:
                if j == 0:  # первая строка
                    matrix_2[i][j] = matrix[0][len(matrix[0]) - 1] + matrix[i + 1][j] + matrix[len(matrix) - 1][0] + matrix[i][j + 1]  # элемент в левом верхнем углу
                elif j == len(matrix[0]) - 1:
                    matrix_2[i][j] = matrix[len(matrix) - 1][len(matrix[0]) - 1] + matrix[i + 1][j] + matrix[i][j - 1] + matrix[0][0]  # элемент в правом верхнем углу
                else:
                    matrix_2[i][j] = matrix[len(matrix) - 1][j] + matrix[i + 1][j] + matrix[i][j - 1] + matrix[i][j + 1]  # первая строка между первым и последним элементом
            elif i == len(matrix) - 1:  # последняя строка
                if j == 0:
                    matrix_2[i][j] = matrix[i][len(matrix[0]) - 1] + matrix[0][0] + matrix[i - 1][j] + matrix[i][j + 1]  # элемент в левом нижнем углу
                elif j == len(matrix[0]) - 1:
                    matrix_2[i][j] = matrix[i - 1][j] + matrix[i][j - 1] + matrix[len(matrix) - 1][0] + matrix[0][len(matrix[0]) - 1]  # элемент в правом нижнем углу
                else:
                    matrix_2[i][j] = matrix[i][j - 1] + matrix[i][j + 1] + matrix[i - 1][j] + matrix[0][j]  # последняя строка между первым и последним элементом
            elif j == 0:  # первый столбец (кроме первого и последнего элемента)
                matrix_2[i][j] = matrix[i - 1][j] + matrix[i + 1][j] + matrix[i][j + 1] + matrix[i][len(matrix[0]) - 1]
            elif j == len(matrix[0]) - 1:   # последний столбец (кроме первого и последнего элемента)
                matrix_2[i][j] = matrix[i - 1][j] + matrix[i + 1][j] + matrix[i][j - 1] + matrix[i][0]
            else:   # все элементы (кроме крайних)
                matrix_2[i][j] = matrix[i - 1][j] + matrix[i + 1][j] + matrix[i][j - 1] + matrix[i][j + 1]

for row in matrix_2:  # вывод матрицы
    print(' '.join([str(elem) for elem in row]))

'''Альтернативное решение'''

matrix_a = []
row_a = input()
while row_a != "end":
    matrix_a.append(row_a.split())
    row_a = input()
for i in range(len(matrix_a)):
    for j in range(len(matrix_a[i])):
        print(int(matrix_a[i-1][j]) + int(matrix_a[i-len(matrix_a)+1][j]) + int(matrix_a[i][j-1]) + int(matrix_a[i][j-len(matrix_a[i])+1]), end =" ")
    print()

'''Спираль'''

import math

loop = int(input())
helix = [[0] * loop for i in range(loop)]  # создание квадратной матрицы

for n in range(1, math.ceil(loop / 2) + 1):  # заполнение значениями на каждом витке
    helix[0][0] = 1
    for j in range(loop):  # →
        if helix[n - 1][j] == 0:
            helix[n - 1][j] = helix[n - 1][j - 1] + 1
    for i in range(1, loop):  # ↓
        if helix[i][loop - 1 - n + 1] == 0:
            helix[i][loop - 1 - n + 1] = helix[i - 1][loop - 1 - n + 1] + 1
    for j in range(1, loop):  # ←
        if helix[loop - 1 - n + 1][loop - 1 - j] == 0:
            helix[loop - 1 - n + 1][loop - 1 - j] = helix[loop - 1 - n + 1][loop - j] + 1
    for i in range(1, loop):  # ↑
        if helix[loop - 1 - i][n - 1] == 0:
            helix[loop - 1 - i][n - 1] = helix[loop - i][n - 1] + 1

for i in range(loop):  # вывод матрицы
    for j in range(loop):
        print(helix[i][j], end=' ')
    print()