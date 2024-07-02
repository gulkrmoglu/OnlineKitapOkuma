from OnlineKitapOkumaSitesi.pages.constants.globalConstants import *
from OnlineKitapOkumaSitesi.pages.PageBase import PageBase
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import time

class BookContent(PageBase):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
     #Geçerli kitap ve yazar adıyla kitap içeriğinin detaylarını gösterme durumu(case1)
    def book_content(self):
        search_icon=self.WaitForElementVisible(SEARCHING).click()
        search_text_box=self.WaitForElementVisible(SEARCH_TEXT_BOX)
        search_text_box.send_keys(SEARCH_STORY)
        time.sleep(3)
        search_button=self.WaitForElementVisible(SEARCH_BUTTON).click()        
        time.sleep(5)       
        self.driver.execute_script("window.scrollBy(0,400)", "")
        stephan=self.WaitForElementVisible(STEPHAN).click()  
        time.sleep(30)
        self.driver.execute_script("window.scrollBy(0,400)", "")
