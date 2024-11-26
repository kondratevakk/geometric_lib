import unittest
from triangle import area, perimeter

'''
Test for Triangle
'''


class TriangleTestCase(unittest.TestCase):
    def test_zero_side(self):
        res_area = area(0, 0)
        res_perimeter = perimeter(0, 0, 0)
        self.assertEqual(res_area, 0)
        self.assertEqual(res_perimeter, 0)

    def test_valid_side(self):
        res_area = area(3, 4)
        res_perimeter = perimeter(3, 4, 5)
        self.assertEqual(res_area, 6)
        self.assertEqual(res_perimeter, 12)

    def test_valid_side2(self):
        res_area = area(5, 6)
        res_perimeter = perimeter(5, 6, 9)
        self.assertEqual(res_area, 15)
        self.assertEqual(res_perimeter, 20)

    def test_invalid_side_area(self):
        res_area = area("tr", 7)
        res_perimeter = perimeter(2, 3, 4)
        self.assertEqual(res_area, 0)
        self.assertEqual(res_perimeter, 9)

    def test_invalid_side_perimeter(self):
        res_area = area(6, 10)
        res_perimeter = perimeter(6, "y", 8)
        self.assertEqual(res_area, 30)
        self.assertEqual(res_perimeter, 0)

    def test_invalid_side_both(self):
        res_area = area("a", "b")
        res_perimeter = perimeter("a", "b", "c")
        self.assertEqual(res_area, 0)
        self.assertEqual(res_perimeter, 0)

    def test_negative_side_area(self):
        res_area = area(-2, 3)
        res_perimeter = perimeter(3, 4, 6)
        self.assertEqual(res_area, 0)
        self.assertEqual(res_perimeter, 13)

    def test_int_string_side_area(self):
        res_area = area("3", 4)
        res_perimeter = perimeter(3, 4, 5)
        self.assertEqual(res_area, 6)
        self.assertEqual(res_perimeter, 12)

    def test_negative_side_perimeter(self):
        res_area = area(2, 3)
        res_perimeter = perimeter(3, 4, -6)
        self.assertEqual(res_area, 3)
        self.assertEqual(res_perimeter, 0)

    def test_int_string_side_perimeter(self):
        res_area = area(3, 4)
        res_perimeter = perimeter(3, "4", 5)
        self.assertEqual(res_area, 6)
        self.assertEqual(res_perimeter, 12)

# if __name__ == '__main__':
#     unittest.main()
