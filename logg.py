from data_create import name_data, surname_data, phone_data, address_data


def input_data():
    name = name_data()
    surname = surname_data()
    phone = phone_data()
    address = address_data()
    var = int(input(f"В каком формате записать данные"f"1 вариант{surname}\n{name}\n{phone}\n{address}\n"
                    f"2 вариант {surname}; {name}; {phone}; {address}\n"
                    f"Выберите вариант "))
    while var != 1 and var != 2:
        print("Вы ввели неверное число")
        var = int(input("Введите число: "))
    if var == 1:
        with open("data_first_variant.cvs", "a", encoding="utf-8") as f:
            f.write(f"{surname}\n{name}\n{phone}\n{address}\n\n ")
    elif var == 2:
        with open("data_second_variant.cvs", "a", encoding="utf-8") as f:
            f.write(f"{surname};{name};{phone};{address}\n\n")

# input_data()


def print_data():
    print("Вывожу Ваши данные из 1 файла: \n ")
    with open("data_first_variant.cvs", "r", encoding="utf-8") as f:
        data_first = f.readlines()
        data_first_list = []
        j = 0
        for i in range(len(data_first)):
            if data_first[i] == "\n" or data_first[i] == len(data_first)-1:
                data_first_list.append("".join(data_first[j:i+1]))
                j = i
    print("".join(data_first_list))

    print("Вывожу Ваши данные из 2 файла: \n ")
    with open("data_second_variant.cvs", "r", encoding="utf-8") as f:
        data_second = f.readlines()

        print(* data_second)


# print_data()


def change_data():
    name = name_data()
    surname = surname_data()
    var = int(input(f"в каком справочнике находится Ваш контакт?- "))
    while var != 1 and var != 2:
        print("Вы ввели неверное число")
        var = int(input("Введите число: "))
    if var == 2:
        with open("data_second_variant.cvs", "r", encoding='utf-8') as s:
            s = s.readlines()
            s1 = input(
                "Введите  новые значения фамилии имени, адреса и номера телефона через пробел ").split()
            s1 = ";".join(s1)
            s1 = s1+"\n"
            s1 = s1.title()
            for i, l in enumerate(s):
                if name in l and surname in l:
                    s.pop(i)
                    s.insert(i, s1)

        with open("data_second_variant.cvs", "w", encoding='utf-8') as s1:
            s1.write(" ".join(s)+"\n")
    elif var == 1:
        with open("data_first_variant.cvs", "r", encoding='utf-8') as s:
            s = s.readlines()
            s1 = input(
                "Введите  новые значения фамилии имени, адреса и номера телефона через пробел ").split()
            s1 = "\n".join(s1)
            s1 = s1.title()
            for i, l in enumerate(s):
                if surname in l or name in l:
                    for j in s[i:i+4]:
                        s.pop(i)
                        s.insert(i, s1)
            with open("data_first_variant.cvs", "w", encoding='utf-8') as s2:
                s2.write("\n"+" ".join(s)+"\n")


# change_data()


def delit_data():
    name = name_data()
    surname = surname_data()
    var = int(input(f"в каком справочнике находится Ваш контакт?- "))
    while var != 1 and var != 2:
          print("Вы ввели неверное число")
          var = int(input("Введите число: "))
    if var == 2:
      with open("data_second_variant.cvs", "r", encoding='utf-8') as s:
            s = s.readlines()
            for i, l in enumerate(s):
                if name in l and surname in l:
                    s[i] = ""

      with open("data_second_variant.cvs", "w", encoding='utf-8') as s1:
            s1.write(" ".join(s)+"\n")
#     elif var==1:
      with open("data_first_variant.cvs", "r", encoding='utf-8') as s:
            s = s.readlines()
            for i, l in enumerate(s):
                if surname in l or name in l:
                    for j in s[i:i+4]:
                        s.pop(i)

      with open("data_first_variant.cvs" , "w", encoding='utf-8') as s1:
            s1.write(" ".join(s)+"\n")


# delit_data()
