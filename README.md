# HomeWorkPy
  вывод со следующий строки-обрабный слеш и n '(\n)'
c= round (a/d,3)# вывод с округлением 
print(f"{d} {a}") # вывод через интерполяцию
print( "{}: {}". format(a,d) ) 
 чтобы закоментить надо перед текстом поставить решетку(# ) либо тройные кавычки(''')

print(type(a))# показывает тип данны -->

a,b = map(int,input().split()) - если необходимо ввести два целых числа в одну строку через пробел
a,b,c = map(float,input().split()) - если необходимо ввести три вещественных числа в одну строку через пробел
## Управляющие конструкции: while-else
i = 0
while i < 5:
if i == 3:
break
i = i + 1
else:
print('Пожалуй')
print('хватит )')
print(i)
После выполнения данного кода в консоль выведется только цифра 3, то что
находится внутри else будет игнорироваться, так как цикл завершился не
самостоятельно.
## Пример программного кода без использования break:
n = 423
summa = 0
while summa > 0:
x = n % 10
summa = summa + x
n = n // 10
else:
print('Пожалуй')
print('хватит )')
print(summa)
# Пожалуй
# хватит )
## Задача: Пользователь вводит число, необходимо найти минимальный делитель
данного числа
n = int(input())
flag = True
i = 2
while flag:
if n % i == 0: # если остаток при делении числа n на i равен 0
flag = False
print(i)
elif i > n // 2: # делить числа не может превышать введенное число, деленное
на 2
print(n)
flag = False
i += 1
Данный алгоритм будет работать до тех пор, пока не найдется минимальный
делитель введенного числа. Когда будет найден первый делитель цикл остановит
свою работу, так как условие, которое находится внутри станет ложным(False)
Пример использования цикла for:
for i in enumeration:
# operator 1
# operator 2
# ...
# operator n
for i in 1, -2, 3, 14, 5:
print(i)
# 1 -2 3 15 5
Range
● Range выдает значения из диапазона с шагом 1.
● Если указано только одно число — от 0 до заданного числа.
● Если нужен другой шаг, третьим аргументов можно задать приращение.
r = range(5) # 0 1 2 3 4
r = range(2, 5) # 2 3 4
r = range(-5, 0) # ----
r = range(1, 10, 2) # 1 3 5 7
r = range(100, 0, -20) # 100 80 60 40 20
r = range(100, 0, -20) # range(100, 0, -20)
for i in r:
print(i)
# 100 80 60 40 20
for i in range(5):
print(i)
# 0 1 2 3 4


## СТРОКИ
## text = 'СъЕШЬ ещё этих МяГкИх французских булок'
1. Определить количество символов в строке:
print(len(text)) # 39
2. Проверить наличие символа в строке (in):
print('ещё' in text) # True
3. Функция, которая делает все буквы строки маленькими:
print(text.lower()) # съешь ещё этих мягких французских булок
4. Функция, которая делает все буквы строки большими:
print(text.upper()) # СЪЕШЬ ЕЩЁ ЭТИХ МЯГКИХ ФРАНЦУЗСКИХ БУЛОК
5. Заменить слово на другое :
print(text.replace('ещё','ЕЩЁ')) # СъЕШЬ ЕЩЁ этих МяГкИх французских булок
💡 help(название функции) — встроенная справка о функции.
29
## Срезы
● Мы представляем строку в виде массива символов. Значит мы можем
обращаться к элементам по индексам.
● Отрицательное число в индексе — счёт с конца строки
## text = 'съешь ещё этих мягких французских булок'
print(text[0]) # c
print(text[1]) # ъ
print(text[len(text)-1]) # к
print(text[-5]) # б
print(text[:]) # съешь ещё этих мягких французских булок
print(text[:2]) # съ
print(text[len(text)-2:]) # ок
print(text[2:9]) # ешь ещё
print(text[6:-18]) # ещё этих мягких
print(text[0:len(text):6]) # сеикакл
print(text[::6]) # сеикакл
print(t[: :-1]) # переворачивает строку( зеркалит ее)
text = text[2:9] + text[-5] + text[:2] # ...

## СПИСКИ -LISTS
Можно список заполнять не только при его создание, но и во время работы
программы:
list_1 = list() # создание пустого списка
  for i in range(5): # цикл выполнится 5 раз
  n = int(input()) # пользователь вводит целое число
  list_1.append(n) # сохранение элемента в конец списка
# 1-я итерация цикла(повторение 1): n = 12, list_1 = [12]
# 2-я итерация цикла(повторение 2): n = 7, list_1 = [12, 7]

Взаимодействие цикла for со списком:
list_1 = [12, 7, -1, 21, 0]
  for i in list_1:
  print(i) # вывод каждого элемента списка
# 1-я итерация цикла(повторение 1): i = 12
# Удаление последнего элемента списка.
Метод который  удаляет последний элемент из списка:
list_1 = [12, 7, -1, 21, 0]
print(list_1.pop()) # 0
print(list_1) # [12, 7, -1, 21]
print(list_1.pop()) # 21
Надо указать значение индекса в качестве аргумента функции pop:
list_1 = [12, 7, -1, 21, 0]
print(list_1.pop(0)) # 12
a=list_1.pop(0))-удаленному индексу присваиватеся переменная.
## Добавление элемента на нужную позицию.
Функция insert — указание индекса (позиции) и значения.
list_1 = [12, 7, -1, 21, 0]
print(list1.insert(2, 11))- в скобказ указана на первом месте индекс  и на втором месте - значение , которое мв вставляем., 
print(list1) # [12, 7, 11, -1, 21, 0]
## Также существует срезс писка

● Отрицательное число в индексе — счёт с конца списка
list_1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(list_1[1]) # 2
print(list_1[-5]) # 6
print(list_1[:]) # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(list_1[len(list_1)-2:]) #[9, 10]
print(list_1[0:len(list_1):6]) # [1, 7]
print(list_1[::6]) # [1, 7]

## Создание рандомного списка
from random import randint

list_1 = [randint(-3, 6) for i in range(1, 9)]
print(list_1)
## Кортеж — это неизменяемый список.
 Кортеж занимаетменьше места в памяти и работают быстрее, по сравнению со списками
 t = () # создание пустого кортежа
print(type(t)) # class <'tuple'>
t = (1,)
print(type(t))
t = (1)
print(type(t))
t = (28, 9, 1990)
print(type(t))
colors = ['red', 'green', 'blue']
print(colors) # ['red', 'green', 'blue']
t = tuple(colors)
print(t) # ('red', 'green', 'blue')
t = tuple(['red', 'green', 'blue'])
print(t[0]) # red
print(t[2]) # blue
for e in t:
print(e) # red green blue
t[0] = 'black' # TypeError: 'tuple' object does not support(нельзя изменять
кортеж)
7
## Можно распаковать кортеж в независимые переменные:
t = tuple(['red', 'green', 'blue'])
red, green, blue = t
print('r:{} g:{} b:{}'.format(red, green, blue)) # r:red g:green b:blue

## Словари — неупорядоченные коллекции произвольных объектов с
доступом по ключу.
 В словаре для определения элемента используется значение ключа (строка, число).
 dictionary = {}
dictionary ={'up': '↑', 'left': '←', 'down': '↓', 'right': '→'}
print(dictionary) # {'up':'↑', 'left':'←', 'down':'↓', 'right':'→'}
print(dictionary['left']) # ←
# типы ключей могут отличаться
print(dictionary['up']) # ↑
# типы ключей могут отличаться
dictionary['left'] = '⇐'
print(dictionary['left']) # ⇐
print(dictionary['type']) # KeyError: 'type'
del dictionary['left'] # удаление элемента
for item in dictionary: # for (k,v) in dictionary.items():
print('{}: {}'.format(item, dictionary[item]))
# up: ↑
# down: ↓
# right: →
  ## Множества содержат в себе уникальные элементы, не обязательно
упорядоченные.
Одно множество может содержать значения любых типов. Если у Вас есть два
множества, Вы можете совершать над ними любые стандартные операции,
например, объединение, пересечение и разность. 
colors = {'red', 'green', 'blue'}
print(colors) # {'red', 'green', 'blue'}
colors.add('red')
print(colors) # {'red', 'green', 'blue'}
colors.add('gray')
print(colors) # {'red', 'green', 'blue','gray'}
colors.remove('red')
print(colors) # {'green', 'blue','gray'}
colors.remove('red') # KeyError: 'red'
colors.discard('red') # ok
print(colors) # {'green', 'blue','gray'}
colors.clear() # { }
print(colors) # set()

a = {1, 2, 3, 5, 8}
b = {2, 5, 8, 13, 21}
c = a.copy() # c = {1, 2, 3, 5, 8}
u = a.union(b) # u = {1, 2, 3, 5, 8, 13,
i = a.intersection(b) # i = {8, 2, 5}
dl = a.difference(b) # dl = {1, 3}
dr = b.difference(a) # dr = {13, 21}
q=a.union(b).difference(a.intersection(b)) # {1, 21, 3, 13}
## Неизменяемое или замороженное множество(frozenset) — множество, с которым
не будут работать методы удаления и добавления.
a = {1, 2, 3, 5, 8}
b = frozenset(a)
print(b) # frozenset({1, 2, 3, 5, 8})
 ## List comprehension — это упрощенный подход к созданию списка, который
задействует цикл for, а также инструкции if-else для определения того, что в итоге
окажется в финальном списке.
1. Простая ситуация — список:
list_1 = [exp for item in iterable]
2. Выборка по заданному условию:
list_1 = [exp for item in iterable (if conditional)]
Задача: Создать список, состоящий из четных чисел в диапазоне от 1 до 100.
Решение:
1. Создать список чисел от 1 до 100
list_1 = []
for i in range(1, 101):
list_1.append(i)
print(list_1) # [1, 2, 3,..., 100]
Эту же функцию можно записать так:
list_1 = [i for i in range(1, 101)] # [1, 2, 3,..., 100]
11
2. Добавить условие (только чётные числа)
list_1 = [i for i in range(1, 101) if i % 2 == 0] # [2, 4, 6,..., 100]
Допустим, вы решили создать пары каждому из чисел (кортежи)
list_1 = [(i, i) for i in range(1, 101) if i % 2 == 0] # [(2, 2), (4, 4),...,
(100, 100)]
Также можно умножать, делить, прибавлять, вычитать. Например, умножить
значение на 2.
list_1 = [i * 2 for i in range(10) if i % 2 == 0]
print(list_1) # [0, 4, 8, 12, 16]


## Самые распространенные ошибки:
● SyntaxError(Синтаксическая ошибка)
number_first = 5
number_second = 7
if number_first > number_second # !!!!!-нет двоеточия(:)
print(number_first

● IndentationError(Ошибка отступов)
number_first = 5
number_second = 7
if number_first > number_second:

● TypeError(Типовая ошибка)
text = 'Python'
number = 5
print(text + number)
# Нельзя складывать строки и числа
● ZeroDivisionError(Деление на 0)
number_first = 5
number_second = 0
print(number_first // number_second)
# Делить на 0 нельзя
● KeyError(Ошибка ключа)
dictionary = {1: 'Monday', 2: 'Tuesday'}
print(dictionary[3])
# Такого ключа не существует
13
● NameError(Ошибка имени переменной)
name = 'Ivan'
print(names)
# Переменной names не существует
● ValueError(Ошибка значения)
text = 'Python'
print(int(text))
# Нельзя символы перевести в целые значения



