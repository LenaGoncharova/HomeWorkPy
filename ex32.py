# Определить индексы элементов массива (списка), значения которых принадлежат заданному
# диапазону (т.е. не меньше заданного минимума и не больше заданного максимума)
import random
lst =[random.randint (-10,10)  for i in range(15)]
print(lst)
min=int(input('Введите минимальное значение '))
max=int(input('Введите максимальное значение '))
lst1=[]
for i in range(len(lst)):
    if  min<=lst[i]<=max:
        lst1.append(i)
print(lst1)


