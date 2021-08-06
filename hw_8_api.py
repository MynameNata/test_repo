import unittest
from hw_7 import create_book, get_my_book, id_book, in_list

class TestApi(unittest.TestCase):
    def setUp(self):
        self.post_book = create_book
        self.get_book = get_my_book
        self.in_list = in_list

    def test_status_code(self):
        self.assertEqual(self.post_book.status_code, 201)

    def test_get_book(self):
        self.assertEqual(self.get_book.url, (f"http://pulse-rest-testing.herokuapp.com/books/{id_book}"))

    # def test_book_in_list(self):
    #     self.assertIn(id_book, self.in_list.json(id(id_book)))





if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TestApi)
    result = unittest.TestResult()