def funk():  # Обьявяем функцию
    password = input("введите пароль")  # Обьявляем переменну присваемая ей интерактивное значение пароля
    digits = letters = 0  # Изначаьно обьявляем переменные digits и letters равными 0 подразумевая что пароль не введен
    if len(password) < 10:  # После введения данных проверяем пароль на соответствие по количеству символов
        return False
    for c in password:  # Запускаем цикл для проверки наличия в пароле цифр и букв
        if c.isdigit():  # Проверка на наличее цифр
            digits += 1
        elif c.isalpha():  # Проверка на наличее букв
            letters += 1
    if digits == 0 or letters == 0:
        return False
    return password


if __name__ == "__main__":  # Сказали что так нужно, почему пока-что не понятно
    pas = funk()
    if pas:
        print("Your password is strong.")
    else:
        print("Your password is not strong enough.")









