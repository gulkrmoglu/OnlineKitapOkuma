import pytest
import unittest
from OnlineKitapOkumaSitesi.pages.sn04_start_readindg_and_progress import StartReadingAndProgress


@pytest.mark.usefixtures("setup")
class TestStartReadingAndProgress(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def class_setup(self):
        self.start_reading_and_progress= StartReadingAndProgress(self.driver)

    def test_books_searching_and_filtering(self):
        self.start_reading_and_progress.start_reading_and_progress()

if __name__ == "__main__":
    unittest.main()        