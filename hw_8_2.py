import unittest
from hw_5 import year_leap

class TestYearLeap(unittest.TestCase):
    def setUp(self):
        self.year_l = year_leap

    def test_leap_year(self):
        self.assertEqual(self.year_l(year=2000), True)

    def test_Not_leap_year(self):
        self.assertEqual(self.year_l(year=2019), False)

    def test_empty_enter(self):
        with self.assertRaises(TypeError):
            self.year_l(year=' ')

    def test_alpha(self):
        with self.assertRaises(TypeError):
            self.year_l(year='hkjjljljk')

    @unittest.expectedFailure
    def test_enter_alpha(self):
        self.assertEqual(self.year_l(year='dsdsfsdfs'), True)




if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TestYearLeap)
    result = unittest.TestResult()
    print(result)
