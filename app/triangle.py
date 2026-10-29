def area(a: int | float, h: int | float) -> float:
    """Возвращает площадь треугольника по основанию и высоте."""
    return a * h / 2


def perimeter(
    a: int | float,
    b: int | float,
    c: int | float,
) -> int | float:
    """Возвращает периметр треугольника."""
    return a + b + c
