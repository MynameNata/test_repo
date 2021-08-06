import unittest
from hw_5 import triangle

class TestTriangle(unittest.TestCase):
    def setUp(self):
        self.tr = triangle

    def test_positive_full(self):
        self.assertEqual(self.tr(a=1, b=2, c=3), True)

    def test_all_is_zero(self):
        self.assertEqual(self.tr(a=0, b=0, c=0), False)

    def test_one_of_item_is_zero(self):
        self.assertEqual(self.tr(a=4, b=0, c=5), False)

    @unittest.expectedFailure
    def test_negative_full(self):
        self.assertEqual(self.tr(a=0, b=0, c=0), True)

    @unittest.expectedFailure
    def test_neg_one_of_item_is_zero(self):
        self.assertEqual(self.tr(a=3, b=4, c=0), True)



if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TestTriangle)
    result = unittest.TestResult()
    print(result)
