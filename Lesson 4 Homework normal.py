# Задание-1:
# Напишите функцию, возвращающую ряд Фибоначчи с n-элемента до m-элемента.
# Первыми элементами ряда считать цифры 1 1

def fibonacci():
    n = int(input("Введите начало вашего интервала: "))
    m = int(input("Введите конец вашего интервала: "))
    if n == 0:
        print("Ваша последовательность должна начинаться по крайней мере с единицы")
    else:
        list_of_numbers = [1, 1]
        a = list_of_numbers[0]
        b = list_of_numbers[1]
        for i in range(m + 1):
            c = a + b
            list_of_numbers.append(c)
            a = b
            b = c
        print(list_of_numbers[n-1:m])
fibonacci()

# Задача-2:
# Напишите функцию, сортирующую принимаемый список по возрастанию.
# Для сортировки используйте любой алгоритм (например пузырьковый).
# Для решения данной задачи нельзя использовать встроенную функцию и метод sort()

def bubble_sort(list): 
    for i in range(0,len(list)-1): 
        for j in range(len(list)-1): 
            if(list[j]>list[j+1]): 
                a = list[j] 
                list[j] = list[j+1] 
                list[j+1] = a 
    return list 
list_1 = [2, 10, -12, 2.5, 20, -11, 4, 4, 0]
bubble_sort(list_1)
print(bubble_sort(list_1))

# Задача-3:
# Напишите собственную реализацию стандартной функции filter.
# Разумеется, внутри нельзя использовать саму функцию filter.

def function_of_even_numbers_filtering(list):
    list_2 = []
    for i in list:
        if i % 2 != 0:
            list_2.append(i)
    print(list_2)
function_of_even_numbers_filtering([2, 7, -12, 2.5, 3, -11, 4, 9, 0])

# Задача-4:
# Даны четыре точки А1(х1, у1), А2(x2 ,у2), А3(x3 , у3), А4(х4, у4).
# Определить, будут ли они вершинами параллелограмма.

