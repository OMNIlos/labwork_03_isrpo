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

    def test_negative_side(self):
        """Проверяет отрицательную сторону."""
        self.assertEqual(area(-4), 16)
        self.assertEqual(perimeter(-4), -16)

    def test_invalid_type(self):
        """Проверяет неверный тип данных."""
        with self.assertRaises(TypeError):
            area(None)
        with self.assertRaises(TypeError):
            perimeter(None)


if __name__ == "__main__":
    unittest.main()
