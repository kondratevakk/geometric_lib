import math

def area(r):
    """
    Вычисляет площадь круга по заданному радиусу.

    Параметры:
    r (float): Радиус круга.

    Возвращает:
    float: Площадь круга.

    Пример вызова:
    >>> area(5)
    78.53981633974483
    """
    return math.pi * r * r


def perimeter(r):
    """
    Вычисляет длину окружности (периметр круга) по заданному радиусу.

    Параметры:
    r (float): Радиус круга.

    Возвращает:
    float: Длина окружности.

    Пример вызова:
    >>> perimeter(5)
    31.41592653589793
    """
    return 2 * math.pi * r
