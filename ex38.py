# Дополнить телефонный справочник возможностью изменения и удаления данных.
# Пользователь также может ввести имя или фамилию,
# и Вы должны реализовать функционал для изменения и удаления данных
from logg import input_data, print_data, delit_data, change_data


def interfase():
    print("Это бот умеет записывать,выводить, изменять, удалять  данные в телефонном справочнике. \n"

        "1-запись данных\n"
        "2-вывод данных\n"
        "3-изменение данных\n"
        "4-удаление данных")
    num = int(input(" Введите  цифру выбранной функции: "))

    while num != 1 and num != 2 and num != 3 and num != 4:

      print("Вы ввели неверное число")
      num = int(input("Введите число: "))



if num==1:
    input_data()
elif num==2:
          print_data()
  # elif num==3:
        # change_data()
          
  # elif num==4:
      #   delit_data()
      
interfase()        
    

# Пополнить телефонный справочник возможностью изменения и удаления данных.
# Пользователь также может ввести имя или фамилию,
# и Вы должны реализовать функционал для изменения и удаления данных

      
