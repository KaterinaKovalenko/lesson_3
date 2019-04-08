#  Белки проводят большую часть дня, играя.
#  В частности, они играют, если температура составляет от 10 до 20 (включительно).
#  Если лето, то верхний предел температуры равен 30 вместо 20.
#  Напишите функцию, которая принимает температуру int и логическое значение is_summer,
#  верните True, если белки играют, и False в противном случае.
def squirrels(temperature, is_summer):
    is_play = False
    if is_summer:
        if 60 <= temperature <= 100:
            is_play = True
           # return "Igraut Blya!!!!"
        # else:
        #     return "Pizdec ne igrayt(((("
    if not is_summer:
        if 60 < temperature <= 90:
            is_play = True
            #return "Igraut Blya!!!!"
        # else:
        #     return "Pizdec ne igrayt(((("
    return is_play


temp = int(input("Enter the temperature "))
sq = squirrels(temp, is_summer=False)
print(sq)
