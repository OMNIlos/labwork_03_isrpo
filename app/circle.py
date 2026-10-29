import math


def area(r: int | float) -> float:
    """Возвращает площадь круга по радиусу."""
    return math.pi * r * r


def perimeter(r: int | float) -> float:
    """Возвращает длину окружности по радиусу."""
    return 2 * math.pi * r
