#  Проверка имени.
#
# Напишите программу, в которой хранится переменная с вашим именем (в нижнем регистре), а
# затем запрашивает ваше имя в качестве входных данных. Программа должна проверить,
# равен ли ваш ввод сохраненному имени, даже если у данного имени есть другой регистр, например, если ваш
# ввод «Антон», а сохраненное имя «Антон», он должен вернуть True.

# def func_name():
#     name1 = input("Enter your name - ")
#     name1 = name1.lower()
#     return (name1)
#
#
# a = func_name()
# name = "katya"
# if name == a:
#     print("True")
# else:
#     print("Enter error")
# def get_data ():
#     f = open("names.txt", "r")
#     a = f.read()
#     return a
#
#
# def func_name():
#     name1 = input("Enter your name - ")
#     name1 = name1.lower()
#     return name1
#
#
# a = get_data()
# f_n = func_name()
# if f_n in a:
#     print("True")
# else:
#     print("Enter error")


def get_data():
    f = open("names.txt", "r")
    a = f.read()
    return a


def func_name():
    name1 = input("Enter your name - ")
    name1 = name1.lower()
    return name1


a = get_data()
f_n = func_name()
if f_n in a:
    print("True")
else:
    print("Enter error")
