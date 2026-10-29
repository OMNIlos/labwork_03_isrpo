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


if __name__ == "__main__":
    unittest.main()
