# Действительный номер телефона программы.
#
# Создайте программу, которая проверяет, имеет ли строка правильный формат для
# номера телефона . Программа должна проверить, что строка содержит только числовые
# символы и имеет длину всего 10 символов. Напечатайте подходящее сообщение в зависимости
# от результата оценки строки.
def nam():
    tel = input("Введите номер телефона ")
    return tel


mob = nam()
if len(mob) == 10 and mob.isdigit():
    print("OK")
else:
    print("Input Error")




