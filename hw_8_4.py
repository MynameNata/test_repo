import unittest
from hw_5 import type_of_triangle

class TestTypeOfTriangle(unittest.TestCase):
    def setUp(self):
        self.trgl = type_of_triangle

    def test_Equilateral_triangle(self):
        self.assertEqual(self.trgl(q=4, w=4, e=4), 'Equilateral triangle (равносторонний)')

    def test_Isosceles_triangle(self):
        self.assertEqual(self.trgl(q=2, w=2, e=3), 'Isosceles triangle (равнобедренный)')


if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TestTypeOfTriangle)
    result = unittest.TestResult()
    print(result)
