# Задача 12: Петя и Катя – брат и сестра. Петя – студент, а Катя – школьница.
# Петя помогает Кате по математике. Он задумывает два натуральных числа X и Y (X,Y≤1000), 
# а Катя должна их отгадать. Для этого Петя делает две подсказк
#  Он называет сумму этих чисел S и их произведение P. Помогите Кате отгадать задуманные Петей числа.



s=int(input('введите сумму чисел: '))
p=int(input('введите произведение  чисел: '))

for i in range(1000):
    for j in range (10000):
        if i+j==s and i*j== p:
          print (f'x =', i, 'y =',j)
        