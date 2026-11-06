import unittest
from app.rectangle import area, perimeter


class TestRectangle(unittest.TestCase):
    def test_area(self):
        """Проверяет площадь прямоугольника."""
        self.assertEqual(area(2, 3), 6)
        self.assertEqual(area(3, 4), 12)

    def test_perimeter(self):
        """Проверяет периметр прямоугольника."""
        self.assertEqual(perimeter(2, 3), 10)
        self.assertEqual(perimeter(3, 4), 14)

    def test_zero_side(self):
        """Проверяет нулевую сторону."""
        self.assertEqual(area(5, 0), 0)

    def test_area_negative_side(self):
        """Проверяет ошибку для отрицательной стороны."""
        with self.assertRaises(ValueError):
            area(-2, 3)

    def test_perimeter_negative_side(self):
        """Проверяет ошибку для отрицательной стороны."""
        with self.assertRaises(ValueError):
            perimeter(-2, 3)

    def test_invalid_type(self):
        """Проверяет неверный тип данных."""
        with self.assertRaises(TypeError):
            area(None, 3)
        with self.assertRaises(TypeError):
            perimeter(None, 3)

    def test_string_type(self):
        """Проверяет передачу строки."""
        with self.assertRaises(TypeError):
            area("2", "3")
        with self.assertRaises(TypeError):
            perimeter("2", 3)


if __name__ == "__main__":
    unittest.main()
