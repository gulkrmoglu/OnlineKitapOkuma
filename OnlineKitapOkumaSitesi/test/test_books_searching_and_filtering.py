import pytest
import unittest
from OnlineKitapOkumaSitesi.pages.sn02_books_searching_and_filtering import BooksSearchingAndFiltering


@pytest.mark.usefixtures("setup")
class TestCategoryAndAuthor(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def class_setup(self):
        self.books_searching_and_filtering= BooksSearchingAndFiltering(self.driver)

    def test_books_searching_and_filtering(self):
        self.books_searching_and_filtering.filter_by_book_title()
        self.books_searching_and_filtering.multiple_filtering()
        self.books_searching_and_filtering.invalid_book_name()

if __name__ == "__main__":
    unittest.main()
        
        