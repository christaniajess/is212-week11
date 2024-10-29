import unittest
from ex2_smelly import calculate_area, Circle, Rectangle, Triangle

class TestShape(unittest.TestCase):
    def test_calculate_area_circle(self):
        # Test for a circle with radius 5
        circle = Circle(radius=5)
        result = calculate_area(circle)
        self.assertAlmostEqual(result, 78.5, places=2)

    def test_calculate_area_rectangle(self):
        # Test for a rectangle with length 4 and width 6
        rectangle = Rectangle(length=4, width=6)
        result = calculate_area(rectangle)
        self.assertEqual(result, 24)

    def test_calculate_area_triangle(self):
        # Test for a triangle with base 10 and height 8
        triangle = Triangle(base=10, height=8)
        result = calculate_area(triangle)
        self.assertEqual(result, 40)

if __name__ == '__main__':
    unittest.main()