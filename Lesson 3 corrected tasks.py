# Задача-2 (normal):
# Даны два произвольных списка.
# Удалите из первого списка элементы, присутствующие во втором списке.

list_1 = [35, "walrus", 7, "fig", 47, "interrogation"]
list_2 = [22, 7, 19, "interrogation", 35]
for i in list_1.copy():
    if i in list_2:
        list_1.remove(i)
print(list_1)