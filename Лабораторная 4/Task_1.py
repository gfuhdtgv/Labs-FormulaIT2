if __name__ == "__main__":
    class Shape:
        def __init__(self, color: str):
            """Инициализация по цвету"""
            self.color = color

        def area(self) -> float:
            """Вычислить площадь"""
            pass

        def perimeter(self) -> float:
            """Вычислить периметр"""
            pass

        def __str__(self) -> str:
            """Возвращает строковое представление фигуры"""
            pass

    class Circle(Shape):
        def __init__(self, color: str, radius: float):
            """Задать цвет, радиус"""
            super().__init__(color)
            self.radius = radius

        def area(self) -> float:
            """Вычисление площади окружности"""
            return 3.14 * self.radius ** 2


        def __str__(self) -> str:
            """Возвращает строковое представление круга."""
            return f"A {self.color} circle with radius {self.radius}"


    class Rectangle(Shape):
        def __init__(self, color: str, width: float, height: float):
            """Задайте прямоугольнику цвет, ширину и высоту."""
            super().__init__(color)
            self.width = width
            self.height = height

        def area(self) -> float:
            """Площадь прямоугольника"""
            return self.width * self.height

        def perimeter(self) -> float:
            """Периметр прямоугольника"""
            return 2 * (self.width + self.height)

        def __str__(self) -> str:
            """Возвращает строковое представление прямоугольника."""
            return f"A {self.color} rectangle with width {self.width} and height {self.height}"

        def __repr__(self) -> str:
            return f"Rectangle({self.color}, {self.width}, {self.height})"
