import pytest
import unittest
from OnlineKitapOkumaSitesi.pages.sn03_book_content import BookContent


@pytest.mark.usefixtures("setup")
class TestBookContent(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def class_setup(self):
        self.book_content= BookContent(self.driver)

    def test_books_searching_and_filtering(self):
        self.book_content.book_content()

if __name__ == "__main__":
    unittest.main()        