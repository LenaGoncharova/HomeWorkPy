# Требуется найти в массиве list_1 самый близкий по величине элемент к заданному числу k и вывести его.
#Пример:
#list_1 = [1, 2, 3, 4, 5]
#k = 6
# 5
list_1 = [ 1,5,8]
k= int(input( "введите любое число- "))
num=abs(list_1[0]-k)
# index1=0
for i in range(1,len(list_1)):
    num1=abs(list_1[i]-k)
    if num1<=num:
        num1=num
        index1=list_1[i]
print(index1)




    



       
    
        
      
