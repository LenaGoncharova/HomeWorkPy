# # Задача 6: Вы пользуетесь общественным транспортом?
# # Вероятно, вы расплачивались за проезд и получали билет с номером. 
# # Счастливым билетом называют такой билет с шестизначным номером, где сумма первых трех цифр равна сумме последних трех.
# # Т.е. билет с номером 385916 – счастливый, т.к. 3+8+5=9+1+6. Вам требуется написать программу, которая проверяет счастливость билета.

# # *Пример:*

# # 385916 -> yes
# # 123456 -> no

# a = int(input('введите номер билета: '))
# a1=a%1000
# a2=a//1000
# x=a1%10
# y=a1//10%10
# z=a1//100%10
# x1=a2%10
# y1=a2//10%10
# z1=a2//100%10
# sum=x+y+z
# sum1=x1+y1+z1
# print('yes'if  sum==sum1 else'no') 

# # a = int(input('введите номер билета: '))
# a1=a//1000
# sum=0
# sum1=0
# if a<1000000:
#  while a>1000 :
#     f=a%10
#     sum = sum+f
#     a=a//10
# while a1>0 :
#         f1=a1%10
#         sum1 = sum1+f1
#         a1=a1//10 
# print('yes'if  sum==sum1 else'no')

# n = int(input())
# n1 = n // 100000
# n2 = (n % 100000) // 10000
# n3 = (n % 10000) // 1000
# n4 = (n % 1000) // 100
# n5 = (n % 100) // 10
# n6 = n % 10
# if n1 + n2 + n3 == n4 + n5 + n6:
#     print('yes')
# else:
#     print('no')
# Можете рассказать про решение через нумерацию строк
n = input( )
if int(n[0]) + int(n[1]) + int(n[2]) == int(n[3]) + int(n[4]) + int(n[5]):

    print('yes')
else:
    print('no')
print(int(n [0]))
