# Задача-1:
# Дан список фруктов.
# Напишите программу, выводящую фрукты в виде нумерованного списка,
# выровненного по правой стороне.
# Пример:
# Дано: ["яблоко", "банан", "киви", "арбуз"]
# Вывод:
# 1. яблоко
# 2.  банан
# 3.   киви
# 4.  арбуз

# Подсказка: воспользоваться методом .format()

fruit_list = ["apple", "banana", "kiwi", "water_melon"]
a = 0
for i in fruit_list:
    a += 1
    print(a, ".", '{:>12}'.format(i))

# Задача-2:
# Даны два произвольных списка.
# Удалите из первого списка элементы, присутствующие во втором списке.

list_1 = [35, "walrus", 7, "fig", 47, "interrogation"]
list_2 = [22, 7, 19, "interrogation", 35]
if 35 in list_2:
    list_1.remove(35)
elif "walrus" in list_2:
    list_1.remove("walrus")
elif 7 in list_2:
    list_1.remove(7)
elif "fig" in list_2:
    list_1.remove("fig")
elif 47 in list_2:
    list_1.remove(47)
elif "interrogation" in list_2:
    list_1.remove("interrogation")
print(list_1)

# Задача-3:
# Дан произвольный список из целых чисел.
# Получите НОВЫЙ список из элементов исходного, выполнив следующие условия:
# если элемент кратен двум, то разделить его на 4, если не кратен, то умножить на два.

random_list = [4, 52, 7, 9, 60, 3]
new_list = []
a = random_list[0]
for a in random_list:
    if a % 2 == 0:
        new_list.append(a/4)
    else:
        new_list.append(a*2)
print(new_list)