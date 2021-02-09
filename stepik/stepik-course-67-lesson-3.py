"""Задачи из раздела 3 'Функции. Словари. Интерпретатор. Файлы. Модули' курса"""

'''[ expression for item in list if conditional ]  # генератор списка
{ key:value for item in list if conditional }  # генератор словаря
 {key:value for key,value in zip(x,y)}  # генератор словаря из двух списков
 dict = {v:k for k, v in dict.items()}  #  инверсия словаря'''
'''encoding='utf-8' для изменения кодировки при чтении из файла'''


import string

'''Написание функции'''

def f(x):
    if x <= -2:
        return 1 - (x+2)**2
    elif x <= 2 and x > -2:
        return - x/2
    elif x > 2:
        return (x-2)**2 + 1

'''Напишите функцию modify_list(l), которая принимает на вход список целых чисел, удаляет из него все нечётные значения, а чётные нацело делит на два'''

def modify_list(l):
    i = 0
    while i < len(l):
        if l[i] % 2 == 0:
            l[i] = int(l[i]/2)
            i += 1
        else:
            del l[i]
            
lst = [10, 5, 8, 3, 0]
modify_list(lst)
print(lst)

'''Напишите функцию update_dictionary(d, key, value), которая принимает на вход словарь d и два числа: key и value.

Если ключ key есть в словаре d, то добавьте значение value в список, который хранится по этому ключу.
Если ключа key нет в словаре, то нужно добавить значение в список по ключу 2 * key. Если и ключа 2 * key нет, то нужно добавить ключ 2 * key в словарь и сопоставить ему список из переданного элемента [value].

Требуется реализовать только эту функцию, кода вне её не должно быть.
Функция не должна вызывать внутри себя функции input и print.'''

def update_dictionary(d, key, value):
    if key in d:
        d[key] += [value]
    elif 2*key in d:
        d[key*2] += [value]
    else:
        d[key*2] = [value]

d = {}
print(update_dictionary(d, 1, -1))  # None
print(d)                            # {2: [-1]}
update_dictionary(d, 2, -2)
print(d)                            # {2: [-1, -2]}
update_dictionary(d, 1, -3)
print(d)                            # {2: [-1, -2, -3]}

'''Когда Антон прочитал «Войну и мир», ему стало интересно, сколько слов и в каком количестве используется в этой книге.

Помогите Антону написать упрощённую версию такой программы, которая сможет подсчитать слова, разделённые пробелом и вывести получившуюся статистику.

Программа должна считывать одну строку со стандартного ввода и выводить для каждого уникального слова в этой строке число его повторений (без учёта регистра) в формате "слово количество" (см. пример вывода).
Порядок вывода слов может быть произвольным, каждое уникальное слово должно выводиться только один раз.'''

s = input('').lower().translate(str.maketrans('', '', string.punctuation)).split() # применение единого регистра, удаление знаков пунктуации, создание списка
d2 = {key2: s.count(key2) for key2 in s} # создание словаря с указанием частоты встречаемости слова в качестве значения
for key2 in d2:
    print(key2, d2[key2])

'''Напишите программу, которая считывает строку с числом n, которое задаёт количество чисел, которые нужно считать. Далее считывает n строк с числами x_i, по одному числу в каждой строке. Итого будет n+1 строк.
При считывании числа x_i программа должна на отдельной строке вывести значение f(x_i). Функция f(x) уже реализована и доступна для вызова. 
Функция вычисляется достаточно долго и зависит только от переданного аргумента x. Для того, чтобы уложиться в ограничение по времени, нужно избежать повторного вычисления значений.'''

'''def f(i):
    i = i + 1
    return i'''

number = int(input())   # число строк
numbers = [int(input()) for number in range(number)]    # ввод чисел
cache = {}
for i in numbers:
    if i not in cache:
        cache[i] = f(i)   # кэширование значений
    print(cache[i])

'''Восстановление исходной строки'''

text = ''
with open('text_for_lesson3.txt') as inf:   # чтение файла
    old_text = inf.readline()   # чтение первой строки из файла
    for i in range(len(old_text)):   # перебор букв
        if old_text[i].isalpha():
           char = old_text[i]
        elif i + 1 != len(old_text) and old_text[i+1].isdigit() and old_text[i].isdigit():
            num = old_text[i] + old_text[i+1]
            text += int(num)*char
        elif i != 0 and old_text[i-1].isalpha() and old_text[i].isdigit():
            num = old_text[i]
            text += int(num)*char

    with open('text/new_text_for_lesson3.txt', 'w') as ouf:  # запись результата в файл
        ouf.write(text)

'''Наиболее часто используемое слово в тексте'''

with open('text/text2_for_lesson3.txt') as text2_for_lesson3:   # чтение файла
    old_text2 = text2_for_lesson3.read().lower().translate(str.maketrans('', '', string.punctuation)).split()   # чтение первой строки из файла, применение единого регистра, удаление знаков пунктуации, создание списка
    textD = {key3: old_text2.count(key3) for key3 in old_text2} # создание словаря с указанием частоты встречаемости слова в качестве значения
    max_value = max(textD.values())  # максимальное значение
    for i in textD:  # поиск ключа по значению
        if textD[i] == max_value:
            max_key = i
    print(max_key, max_value)


'''Подсчет успеваемости учеников'''

stat = open('text/stat.txt')
stat_upd = open('text/stat_upd.txt', 'w')
data2 = {}
math = 0
physics = 0
russian = 0
data = [line.strip().split(';') for line in stat]   #  считывание строк с удалением служебных символов
for i in range(len(data)):
    name = data[i][0]
    grades = {'math': int(data[i][1]), 'physics': int(data[i][2]), 'russian': int(data[i][3])}   #  создание словаря с данными
    data2[name] = grades
for i in data2:
    average = (data2[i]['math'] + data2[i]['physics'] + data2[i]['russian'])/3   #  средняя оценка каждого ученика
    print(str(average), file=stat_upd)   #  вывод в файл
    math += data2[i]['math']
    physics += data2[i]['physics']
    russian += data2[i]['russian']
print(str(math/len(data)), str(physics/len(data)), str(russian/len(data)), file=stat_upd)   #  среднее по каждому предмету
stat.close()
stat_upd.close()

'''Напишите программу, которая подключает модуль math и, используя значение числа π из этого модуля, находит для переданного ей на стандартный ввод радиуса круга периметр этого круга и выводит его на стандартный вывод.'''

import math
r = float(input(''))
print(2*math.pi*r)

'''Напишите программу, которая запускается из консоли и печатает значения всех переданных аргументов на экран (имя скрипта выводить не нужно). Не изменяйте порядок аргументов при выводе.'''

import sys
print(*sys.argv[1::])   # или print(' '.join(sys.argv[1:]))

'''Число строк в файле'''

import requests

url = 'https://stepic.org/media/attachments/course67/3.6.2/324.txt'.strip() # в содержимом файла удаляются лишние символы для получения url
r = requests.get(url)
print(len(r.text.splitlines())) # разбиение строк для получения списка, длину которого можно посчитать

'''Имеется набор файлов, каждый из которых, кроме последнего, содержит имя следующего файла.
Первое слово в тексте последнего файла: "We".
Загрузите содержимое последнего файла из набора, как ответ на это задание.
'''
url = 'https://stepic.org/media/attachments/course67/3.6.3/699991.txt'.strip()
info = ['']
while info[0].startswith('We') != True:
    url = 'https://stepic.org/media/attachments/course67/3.6.3/' + (requests.get(url)).text.strip()
    r = requests.get(url)
    info = r.text.splitlines()
    print(info[0])   # мониторинг первого элемента массива
with open('text/final_text_for_lesson3.txt', 'w') as ouf3:  # запись результата в файл
    ouf3.write(r.text)

'''Напишите программу, которая принимает на стандартный вход список игр футбольных команд с результатом матча и выводит на стандартный вывод сводную таблицу результатов всех матчей.
За победу команде начисляется 3 очка, за поражение — 0, за ничью — 1.'''

n_games = int(input())  # ввод числа игр
games = [input().split(';') for i in range(n_games)]  # ввод игр в формате: Спартак;9;Зенит;10
dataGame = {}
for i in range(len(games)):  # создание словаря с данными
    dataGame[games[i][0]] = {'game': 0, 'wins': 0, 'equality': 0, 'losses': 0, 'points': 0}
    dataGame[games[i][2]] = {'game': 0, 'wins': 0, 'equality': 0, 'losses': 0, 'points': 0}
set(dataGame)  # удаление повторяющихся элементов
for key in dataGame:  # сравнение данных в списке и добавление значений в словарь
    for i in range(len(games)):
        if key == games[i][0] or key == games[i][2]:
            dataGame[key]['game'] += 1
            if int(games[i][1]) == int(games[i][3]):
                dataGame[key]['equality'] += 1
        if key == games[i][0]:
            if int(games[i][1]) > int(games[i][3]):
                dataGame[key]['wins'] += 1
            elif int(games[i][1]) < int(games[i][3]):
                dataGame[key]['losses'] += 1
        if key == games[i][2]:
            if int(games[i][1]) < int(games[i][3]):
                dataGame[key]['wins'] += 1
            elif int(games[i][1]) > int(games[i][3]):
                dataGame[key]['losses'] += 1
    dataGame[key]['points'] = 3*dataGame[key]['wins']+dataGame[key]['equality']

for key, games in dataGame.items():  # вывод ключей и значений в необходимом формате
    print((key+':'), *games.values(), end='\n')

'''Шифрование и дешифрование'''

key_source = list(input(''))
key_result = list(input(''))

text_source1 = list(input(''))
text_result2 = list(input(''))

text_result1=[]
text_source2=[]

keys = {key: value for key, value in zip(key_source, key_result)}

for i in text_source1:
    for key in keys:
        if i == key:
            text_result1 += keys[key]

for i in text_result2:
    for key in keys:
        if keys[key] == i:
            text_source2 += key

print(''.join(text_result1))
print(''.join(text_source2))

''' Альтернативное решение'''

a,b,c,d=input(),input(),input(),input()
print(''.join(b[a.index(i)] for i in c))
print(''.join(a[b.index(i)] for i in d))

'''Проверка орфографии'''

wordsN = int(input())  # ввод числа корректных слов
words = [input().lower() for i in range(wordsN)]
checkN = int(input())
check = []
for i in range(checkN):
    check += input().lower().split()
check2 = set(check)
for i in check2:
    if i not in words:
        print(i)

'''Альтернативное решение'''

words = {input().lower() for i in range(int(input()))}
check = set()
for word in range(int(input())):
    check |= {i.lower() for i in input().split()}

print(*check.difference(words), sep="\n")

'''Черепашка'''

'''navigation = dict(input().split() for i in range(int(input())))  # повторяющиеся значения удаляются
'''

navigation = {'север': 0, 'юг': 0, 'запад': 0, 'восток': 0}
for key, value in [input().split() for i in range(int(input()))]:
    navigation[key] += int(value)  # словарь (вводится число команд и команды вида направление вида "восток 40")

x, y = 0, 0
for i in navigation:
    if i == 'север':
        y += int(navigation[i])
    elif i == 'восток':
        x += int(navigation[i])
    elif i == 'запад':
        x -= int(navigation[i])
    elif i == 'юг':
        y -= int(navigation[i])
print(x, y)

'''Рост учащихся'''

with open('text/data.txt') as inf:   # чтение файла
    dt = {}
    dt_n = {}
    for key, text, value in [i.strip().split() for i in inf.readlines()]:  # суммирование роста
        if key not in dt.keys():
            dt[key] = float(value)
            dt_n[key] = 1
        else:
            dt[key] += float(value)
            dt_n[key] += 1
    for key in dt:  # среднее значение
        dt[key] = dt.pop(key) / dt_n[key]
    for i in range(1,12):  # добавление классов без учеников
        if str(i) not in dt.keys():
            dt[str(i)] = '-'
        print(i, dt[str(i)])

