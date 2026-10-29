import math
import unittest

from app.circle import area, perimeter


class TestCircle(unittest.TestCase):
    def test_area(self):
        """Проверяет площадь круга."""
        self.assertAlmostEqual(area(4), math.pi * 16)
        self.assertAlmostEqual(area(25), math.pi * 625)

    def test_perimeter(self):
        """Проверяет длину окружности."""
        self.assertAlmostEqual(perimeter(4), math.pi * 8)
        self.assertAlmostEqual(perimeter(25), math.pi * 50)

    def test_zero_radius(self):
        """Проверяет нулевой радиус."""
        self.assertEqual(area(0), 0)
        self.assertEqual(perimeter(0), 0)


if __name__ == "__main__":
    unittest.main()
