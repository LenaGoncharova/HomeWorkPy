#  Винни-Пух попросил Вас посмотреть,
# есть ли в его стихах ритм.
# Поскольку разобраться в его кричалках не настолько просто, насколько легко он их придумывает,
# # Вам стоит написать программу. Винни-Пух считает,
# # что ритм есть, если число слогов (т.е. число гласных букв) в каждой фразе стихотворения одинаковое.
# # Фраза может состоять из одного слова, если во фразе несколько слов, то они разделяются дефисами.
# # Фразы отделяются друг от друга пробелами. Стихотворение  Винни-Пух вбивает в программу с клавиатуры.
# # В ответе напишите “Парам пам-пам”, если с ритмом все в порядке и “Пам парам”,
# #

def words(str):
    str=str.split()
    lst_count=[]
  
    for i in str:
        count = 0
      
        for j in i:
            if j in "уеаоыэяию":
                count += 1
        lst_count.append(count) 
      
    if len(lst_count)==lst_count.count(lst_count[0]):
                return"“Парам пам-пам”"
    return "Пам парам"
str=input( "введите строку ")
res=words(str)
print(res)





    





