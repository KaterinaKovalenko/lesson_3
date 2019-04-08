#  1)Написать функцию, которая будет считать и возвращать сумму двух чисел.
#    Если сумма больше 10 - вывести на экран “This sum is greater than 10.
#    It’s {sum}”, если меньше - “This sum is less than 10. It’s {sum}”
sum1 = int(input("введите чисо от 1 до 10 "))
sum2 = int(input("введите чисо от 1 до 10 "))


def sum(sum1, sum2):
    return sum1 + sum2

sum3 = sum(sum1, sum2)
if sum3 >= 10:
    print(f"This sum is greater than 10. It’s {sum3}")
else:
    print(f"This sum is less than 10. It’s {sum3}")

#  2)Написать функцию, которая будет принимать пароль.
#  Если в пароле есть буквы и цифры и его длина не менее 10 символов вывести:
#  “Your password is strong.” в противном случае “Your password is not strong enough.”


