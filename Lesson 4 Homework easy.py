# Задание-1:
# Напишите функцию, переводящую км в мили и выводящую информацию на консоль
# т.е функция ничего не возвращает, а выводит на консоль ответ самостоятельно
# Предполагается, что 1км = 1,609 мили

def convert():
    km = float(input("Введите кол-во км: "))
    miles = km * 1.609
    print(miles)
convert()

# Задание-2:
# Напишите функцию, округляющую полученное произвольное десятичное число
# до кол-ва знаков (кол-во знаков передается вторым аргументом).
# Округление должно происходить по математическим правилам (0.6 --> 1, 0.4 --> 0).
# Для решения задачи не используйте встроенные функции и функции из модуля math.

def my_round():
    number_1 = float(input("Введите ваше число: "))
    number_2 = round(number_1, 0)
    print("Полученное округленное число: ", number_2)
my_round()

# Задание-3:
# Дан шестизначный номер билета. Определить, является ли билет счастливым.
# Решение реализовать в виде функции.
# Билет считается счастливым, если сумма его первых и последних цифр равны.
# !!!P.S.: функция не должна НИЧЕГО print'ить, должна возвращать либо True,
# ибо False (если счастливый и несчастливый соответственно)

def lucky_guess():
    ticket = list(input("Введите номер билета: "))
    if ticket[0] + ticket[1] == ticket[-1] + ticket[-2]:
        return True
    else:
        return False
lucky_guess
print(lucky_guess())