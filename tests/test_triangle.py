import unittest
from app.triangle import area, perimeter


class TestTriangle(unittest.TestCase):
    def test_area(self):
        """Проверяет площадь треугольника."""
        self.assertEqual(area(4, 3), 6)
        self.assertEqual(area(5, 2.5), 6.25)

    def test_perimeter(self):
        """Проверяет периметр треугольника."""
        self.assertEqual(perimeter(3, 4, 5), 12)
        self.assertEqual(perimeter(2.5, 2.5, 3), 8)

    def test_zero_height(self):
        """Проверяет нулевую высоту."""
        self.assertEqual(area(5, 0), 0)

    def test_negative_values(self):
        """Проверяет отрицательные значения."""
        self.assertEqual(area(-4, 3), -6)
        self.assertEqual(perimeter(-3, 4, 5), 6)

    def test_invalid_type(self):
        """Проверяет неверный тип данных."""
        with self.assertRaises(TypeError):
            area(None, 3)
        with self.assertRaises(TypeError):
            perimeter(None, 4, 5)


if __name__ == "__main__":
    unittest.main()
