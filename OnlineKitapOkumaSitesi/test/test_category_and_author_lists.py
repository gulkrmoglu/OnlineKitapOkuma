import pytest
import unittest
from OnlineKitapOkumaSitesi.pages.sn01_category_and_author_lists import CategoryAndAuthor


@pytest.mark.usefixtures("setup")
class TestCategoryAndAuthor(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def class_setup(self):
        self.category_and_author_lists= CategoryAndAuthor(self.driver)

    def test_category_and_author_lists(self):
        self.category_and_author_lists.category()
        self.category_and_author_lists.author()
        self.category_and_author_lists.invalid_category()
        self.category_and_author_lists.invalid_author()


if __name__ == "__main__":
    unittest.main()
        