# Задача-1: Написать класс для фигуры-треугольника, заданного координатами трех точек.
# Определить методы, позволяющие вычислить: площадь, высоту и периметр фигуры.

class triangles:
    def __init__(self, a1, a2, b1, b2, c1, c2):
        self.a1 = a1
        self.a2 = a2
        self.b1 = b1
        self.b2 = b2
        self.c1 = c1
        self.c2 = c2
        import math
        self.AB = round((math.sqrt((self.b1**2 - self.a1**2) + (self.b2**2 - self.a2**2))), 1)
        self.BC = round((math.sqrt((self.c1**2 - self.b1**2) + (self.c2**2 - self.b2**2))), 1)
        self.AC = round((math.sqrt((self.c1**2 - self.a1**2) + (self.c2**2 - self.a2**2))), 1)
    def perimetr(self):
        Per = self.AB + self.BC + self.AC
        return Per
    def triangle_area(self):
        import math
        per_half = (self.AB +self.BC + self.AC)/2
        S = math.sqrt(per_half*(per_half - self.AB)*(per_half - self.BC)*(per_half - self.AC))
        return round(S, 1)
    def triangle_height(self):
        import math
        per_half = (self.AB +self.BC + self.AC)/2
        S = math.sqrt(per_half*(per_half - self.AB)*(per_half - self.BC)*(per_half - self.AC))
        self.height_AB = round(((S*2)/self.AB), 1)
        self.height_BC = round(((S*2)/self.BC), 1)
        self.height_AC = round(((S*2)/self.AC), 1)
        print("Высота стороны AB: {}, высота стороны ВС: {}, высота стороны АС: {}".format(self.height_AB, self.height_BC, self.height_AC))
        return self.height_AB, self.height_BC, self.height_AC
first = triangles(1, 2, 3, 1, 1, -4)

# Задача-2: Написать Класс "Равнобочная трапеция", заданной координатами 4-х точек.
# Предусмотреть в классе методы:
# проверка, является ли фигура равнобочной трапецией;
# вычисления: длины сторон, периметр, площадь.

class IsoscelesTrapezoid:
    def __init__(self, a1, a2, b1, b2, c1, c2, d1, d2):
        self.a1 = a1
        self.a2 = a2
        self.b1 = b1
        self.b2 = b2
        self.c1 = c1
        self.c2 = c2
        self.d1 = d1
        self.d2 = d2
        import math
        self.AB = round((math.sqrt((self.b1**2 - self.a1**2) + (self.b2**2 - self.a2**2))), 1)
        self.BC = round((math.sqrt((self.c1**2 - self.b1**2) + (self.c2**2 - self.b2**2))), 1)
        self.CD = round((math.sqrt((self.d1**2 - self.b1**2) + (self.d2**2 - self.b2**2))), 1)
        self.AD = round((math.sqrt((self.a1**2 - self.d1**2) + (self.a2**2 - self.d2**2))), 1)
    def if_hips_is_even(self):
        if self.AB == self.CD:
            print("Это равнобедренная трапеция")
        else:
            print("Это неравнобедренная трапеция")
    def lenght_of_sides(self):
        print("Сторона АВ: {}, сторона ВС: {}, сторона CD: {}, сторона AD: {}".format(self.AB, self.BC, self.CD, self.AD))
    def perimeter(self):
        Per = self.AB + self.BC + self.CD + self.AD
        return Per
    def area(self):
        import math
        S = (self.BC + self.AD)/2 * math.sqrt(self.AB**2 - (((self.AD - self.BC)**2 + self.AB**2 - self.CD**2)/(2 * (self.AD - self.BC)))**2)
        return round(S, 1)
second = IsoscelesTrapezoid(-2, -2, 2, 2, -3, 3, 2, 2)