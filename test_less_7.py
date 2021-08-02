import unittest
from dis import distance
from HtmlTestRunner import HTMLTestRunner


class TestDistance(unittest.TestCase):
    def setUp(self):
        print('Set up')


    def test_0000(self):
        res = distance (0, 0, 0, 0)
        self.assertEqual(res, 0)

    def test_0100(self):
        res = distance(1, 0, 0, 0)
        self.assertEqual(res, 1)

if __name__ == '__main__':

    # t = TestDistance('test_0000')
    # t2 = TestDistance('test_0100')
    # suite = unittest.TestSuite([t, t2])

    suite = unittest.TestLoader().loadTestsFromTestCase(TestDistance)
    result = unittest.TestResult()
    print(result)
    #
    # suite.run(result)
    # print(result)
    # result = t.run()

    # unittest.main(verbosity=2, testRunner=HtmlTestRunner(output= r'C:\Users\Natalia\Desktop\test_repo\test_repo'))
