import unittest
from app.square import area, perimeter


class TestSquare(unittest.TestCase):
    def test_area(self):
        """Проверяет площадь квадрата."""
        self.assertEqual(area(4), 16)
        self.assertEqual(area(2.5), 6.25)

    def test_perimeter(self):
        """Проверяет периметр квадрата."""
        self.assertEqual(perimeter(4), 16)
        self.assertEqual(perimeter(2.5), 10)

    def test_zero_side(self):
        """Проверяет нулевую сторону."""
        self.assertEqual(area(0), 0)
        self.assertEqual(perimeter(0), 0)

    def test_area_negative_side(self):
        """Проверяет ошибку для отрицательной стороны."""
        with self.assertRaises(ValueError):
            area(-4)

    def test_perimeter_negative_side(self):
        """Проверяет ошибку для отрицательной стороны."""
        with self.assertRaises(ValueError):
            perimeter(-4)

    def test_invalid_type(self):
        """Проверяет неверный тип данных."""
        with self.assertRaises(TypeError):
            area(None)
        with self.assertRaises(TypeError):
            perimeter(None)

    def test_string_type(self):
        """Проверяет передачу строки."""
        with self.assertRaises(TypeError):
            area("4")
        with self.assertRaises(TypeError):
            perimeter("4")


if __name__ == "__main__":
    unittest.main()
