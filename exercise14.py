# Задача 14: Требуется вывести все целые степени двойки (т.е. числа вида 2k), не превосходящие числа N.



n=int(input('Введите число N:'))
k=1
while 2**k <=n:
    print(f'2**{k}={2**k}')
    k+=1

