import unittest
from square import area, perimeter

'''
Test for square
'''


class SquareTestCase(unittest.TestCase):
    def test_zero_side(self):
        res_area = area(0)
        res_perimeter = perimeter(0)
        self.assertEqual(res_area, 0)
        self.assertEqual(res_perimeter, 0)

    def test_valid_side(self):
        res_area = area(3)
        res_perimeter = perimeter(3)
        self.assertEqual(res_area, 9)
        self.assertEqual(res_perimeter, 12)

    def test_valid_side2(self):
        res_area = area(5)
        res_perimeter = perimeter(5)
        self.assertEqual(res_area, 25)
        self.assertEqual(res_perimeter, 20)

    def test_invalid_side(self):
        res_area = area("6r")
        res_perimeter = perimeter("6r")
        self.assertEqual(res_area, 0)
        self.assertEqual(res_perimeter, 0)

    def test_negative_side_area(self):
        res_area = area(-2)
        res_perimeter = perimeter(3)
        self.assertEqual(res_area, 0)
        self.assertEqual(res_perimeter, 12)

    def test_int_string_side_area(self):
        res_area = area("3")
        res_perimeter = perimeter(3)
        self.assertEqual(res_area, 9)
        self.assertEqual(res_perimeter, 12)

    def test_negative_side_perimeter(self):
        res_area = area(2)
        res_perimeter = perimeter(-6)
        self.assertEqual(res_area, 4)
        self.assertEqual(res_perimeter, 0)

    def test_int_string_side_perimeter(self):
        res_area = area(4)
        res_perimeter = perimeter("4")
        self.assertEqual(res_area, 16)
        self.assertEqual(res_perimeter, 16)




# if name == 'main':
#     unittest.main()
