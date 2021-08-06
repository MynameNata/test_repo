import unittest
from hw_6 import Employee


class Test_Employee(unittest.TestCase):
    def setUp(self):
        self.emp = Employee('Den Nm', 1988, position='programmer', experience=7, salary=4000)

    def test_full_name(self):
        self.assertEqual(self.emp.full_name, 'Den Nm')

    def test_birth_year(self):
        self.assertEqual(self.emp.birth_year, 1988)

    def test_type_of_position(self):
        self.assertEqual(self.emp.type_of_position(works_year=9), 'programmer Senior')

    def test_age(self):
        self.assertEqual(self.emp.age(current_year=2021), 33)

    @unittest.expectedFailure
    def test_increase_salary(self):
        self.assertEqual(self.emp.increase_salary(increase=1000), 9000)

    @unittest.expectedFailure
    def test_type_of_position(self):
        self.assertEqual(self.emp.type_of_position(works_year=2), 'programmer Senior')





if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(Test_Employee)
    result = unittest.TestResult()
    print(result)