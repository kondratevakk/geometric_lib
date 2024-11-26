import unittest
import math
from circle import area, perimeter

'''
Test for Circle
'''


class CircleTestCase(unittest.TestCase):
    def test_zero_side(self):
        res_area = area(0)
        res_perimeter = perimeter(0)
        self.assertEqual(res_area, 0)
        self.assertEqual(res_perimeter, 0)

    def test_valid_side(self):
        res_area = area(3)
        res_perimeter = perimeter(3)
        self.assertEqual(res_area, 9 * math.pi)
        self.assertEqual(res_perimeter, 6 * math.pi)

    def test_valid_side2(self):
        res_area = area(5)
        res_perimeter = perimeter(5)
        self.assertEqual(res_area, 25 * math.pi)
        self.assertEqual(res_perimeter, 10 * math.pi)

    def test_invalid_side_area(self):
        res_area = area("tr")
        res_perimeter = perimeter(2)
        self.assertEqual(res_area, 0)
        self.assertEqual(res_perimeter, 4 * math.pi)

    def test_invalid_side_perimeter(self):
        res_area = area(6)
        res_perimeter = perimeter("y")
        self.assertEqual(res_area, 36 * math.pi)
        self.assertEqual(res_perimeter, 0)

    def test_invalid_side_both(self):
        res_area = area("r")
        res_perimeter = perimeter("r")
        self.assertEqual(res_area, 0)
        self.assertEqual(res_perimeter, 0)

    def test_negative_side_area(self):
        res_area = area(-2)
        res_perimeter = perimeter(3)
        self.assertEqual(res_area, 0)
        self.assertEqual(res_perimeter, 6 * math.pi)

    def test_int_string_side_area(self):
        res_area = area("3")
        res_perimeter = perimeter(3)
        self.assertEqual(res_area, 9 * math.pi)
        self.assertEqual(res_perimeter, 6 * math.pi)

    def test_negative_side_perimeter(self):
        res_area = area(2)
        res_perimeter = perimeter(-6)
        self.assertEqual(res_area, 4 * math.pi)
        self.assertEqual(res_perimeter, 0)

    def test_int_string_side_perimeter(self):
        res_area = area(3)
        res_perimeter = perimeter("4")
        self.assertEqual(res_area, 9 * math.pi)
        self.assertEqual(res_perimeter, 8 * math.pi)

# if __name__ == '__main__':
#     unittest.main()
