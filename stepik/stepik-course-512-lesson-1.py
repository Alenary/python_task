"""Задачи из раздела 1 '1  Базовые принципы языка Python' курса"""

'''Сумма чисел'''

'''numbers = [int(input()) for i in range(int(input()))]
sum = 0
for i in numbers:
    sum += i
print(sum)'''

'''print(sum([int(input()) for i in range(int(input()))]))
'''

'''Подсчет различающихся чисел'''

'''objects = [1, 2, 1, 2, 3] # одинаковые числа соответствуют одинаковым объектам, а различные – различным
print(len(set([id(o) for o in objects])))'''

a = []

def foo(arg1, arg2):
  a.append("foo")

foo(a.append("arg1"), a.append("arg2"))

print(a)