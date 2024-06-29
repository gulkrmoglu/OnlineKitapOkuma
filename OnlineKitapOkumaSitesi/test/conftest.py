from selenium import webdriver
import pytest


@pytest.fixture(scope="class")
def setup(request):
        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.get("https://el-kitap.org/")
        request.cls.driver=driver
        yield         
        driver.quit()