# Задача 2: Найдите сумму цифр трехзначного числа.

# *Пример:*

# 123 -> 6 (1 + 2 + 3)
# 100 -> 1 (1 + 0 + 0) |

# a= int(input('введите трехзначное число:  '))
# print( 'сумма числа',a,'->')
# sum=0
# while a>0:
#     f=a%10
#     sum = sum+f
#     a=a//10
# print (sum )
a= int(input('введите трехзначное число:  '))
a1=a%10
a2=a//10%10
a3=a//100%10
sum=a1+a2+a3
print(f' {a} -> {sum} ( {a1} + {a2} + {a3} ) ')
print(" {} -> {} ( {} + {} + {} )".format(a,sum,a1,a2,a3))

# a= int(input('введите  число:  '))
print( 'сумма числа',a,'->')
sum=0
while a>0:
    f=a%10
    sum = sum+f
    a=a//10
print (sum )