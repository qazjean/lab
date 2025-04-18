from abc import ABC, abstractmethod
import math
class Shape(ABC):  #абстрактный класс
    @abstractmethod
    def area(self) : #абстрактный метод для площади
        pass
    @abstractmethod
    def perimeter(self): #абстрактный метод для периметра
        pass

class Rectangle(Shape):  #Прямоугольник
    def __init__(self, width, height):
        self.width = width
        self.height = height
    def area(self):
        return self.height * self.width
    def perimeter(self):
        return 2*self.height + 2 * self.width
    def __str__(self): #без этого метода я получу <__main__.Rectangle object at 0x0000022E0C323A10>,
        #когда захочу вывести строковое представление экземпляра
        return f"Прямоугольник (ширина={self.width}, высота={self.height})"

class Cicle(Shape): #окружность
    def __init__(self, rad):
        self.rad = rad
    def area(self):
        return self.rad * math.pi**2
    def perimeter(self):
        return 2 * math.pi * self.rad
    def __str__(self):
        return f"Круг (радиус={self.rad})"

class Triangle(Shape): #треуольник
    def __init__(self, side1, side2, side3): #я решила считать площадь через формулу Герона,
        # хотя можно и через синус угла между двумя сторонами
        if not (side1 + side2 > side3 and side1 + side3 > side2 and side2 + side3 > side1):
            raise ValueError("Треугольник с такими сторонами не существует")
        #в треугольнике одна сторона всегда меньше суммы двух других. Если я не проведу проверку тут,
            #я могу натолкнуться на отрицательный корень ниже
        self.side1 = side1
        self.side2 = side2
        self.side3 = side3
    def perimeter(self):
        return self.side1 + self.side2 + self.side3
    def area(self):
        p = self.perimeter() / 2
        return math.sqrt(p*(p-self.side1)*(p-self.side2)*(p-self.side3))
    def __str__(self):
        return f"Треугольник (стороны={self.side1}, {self.side2}, {self.side3})"

def choose_shape(): #функция, благодаря которой пользователь может сам вводить данные о фигуре (с учетом положительности сторон)
    shape = input("Введите тип вашей фигруры, пожалуйста:")
    try:
        if shape.lower() == "прямоугольник":
            width = float(input("Введите ширину прямоугольника: "))
            height = float(input("Введите высоту прямоугольника: "))
            if width <= 0 or height <= 0:
                raise ValueError("Стороны должны быть положительными")
            return Rectangle(width, height)
        elif shape.lower() == "окружность":
            rad = float(input("Введите радиус окружности: "))
            if rad <= 0:
                raise ValueError("Радиус должен быть положительным")
            return Cicle(rad)
        elif shape.lower() == "треугольник":
            side1 = float(input("Введите длину первой стороны треугольника: "))
            side2 = float(input("Введите длину второй стороны треугольника: "))
            side3 = float(input("Введите длину третьей стороны треугольника: "))
            if side1 <= 0 or side2 <= 0 or side3 <= 0:
                raise ValueError("Стороны должны быть положительными")
            return Triangle(side1, side2, side3)
        else:
            print("Попроуйте еще раз, пожалуйста")
            return None
    except ValueError as e: #Обработка ошибок
        print(f"Ошибка: {e}. Попробуйте снова.")

def print_shape_info(shape): #ура полиморфизму
        print(f"\n{shape}")
        print(f"Площадь: {shape.area():.2f}")
        print(f"Периметр: {shape.perimeter():.2f}")

shape = choose_shape()
if shape != None:
    print_shape_info(shape)
