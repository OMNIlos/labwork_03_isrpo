import unittest
from app.circle import area, perimeter

PI = 3.141592653589793


class TestCircle(unittest.TestCase):
    def test_area(self):
        """Проверяет площадь круга."""
        self.assertAlmostEqual(area(4), PI * 16)
        self.assertAlmostEqual(area(25), PI * 625)

    def test_perimeter(self):
        """Проверяет длину окружности."""
        self.assertAlmostEqual(perimeter(4), PI * 8)
        self.assertAlmostEqual(perimeter(25), PI * 50)

    def test_zero_radius(self):
        """Проверяет нулевой радиус."""
        self.assertEqual(area(0), 0)
        self.assertEqual(perimeter(0), 0)

    def test_negative_radius(self):
        """Проверяет отрицательный радиус."""
        self.assertAlmostEqual(area(-4), PI * 16)
        self.assertAlmostEqual(perimeter(-4), -PI * 8)

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
