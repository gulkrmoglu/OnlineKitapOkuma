from OnlineKitapOkumaSitesi.pages.constants.globalConstants import *
from OnlineKitapOkumaSitesi.pages.PageBase import PageBase
from selenium.webdriver.common.keys import Keys
import time

class BooksSearchingAndFiltering(PageBase):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
    
    #Kitap başlığına göre sonuçların listelenmesi durumu(CASE1)
    def filter_by_book_title(self):
        search_icon=self.WaitForElementVisible(SEARCHING).click()
        search_text_box=self.WaitForElementVisible(SEARCH_TEXT_BOX)
        search_text_box.send_keys(SEARCH_BOOK)
        time.sleep(3)
        search_button=self.WaitForElementVisible(SEARCH_BUTTON).click()        
        time.sleep(5)       
        self.driver.execute_script("window.scrollBy(0,400)", "")

       
     #Birden fazla fitreleme kullanılması durumu(CASE2)
    def multiple_filtering(self):
        self.driver.get("https://el-kitap.org/")
        search_icon=self.WaitForElementVisible(SEARCHING).click()
        search_text_box=self.WaitForElementVisible(SEARCH_TEXT_BOX)
        search_text_box.send_keys(SEARCH_WORLD_CLASSICS)        
        time.sleep(3)
        search_button=self.WaitForElementVisible(SEARCH_BUTTON).click() 
        self.driver.execute_script("window.scrollBy(0,400)", "")       
        time.sleep(5)  
        search_icon=self.WaitForElementVisible(SEARCHING).click()
        search_text_box=self.WaitForElementVisible(SEARCH_TEXT_BOX)
        search_text_box.send_keys(Keys.CONTROL + 'a')
        search_text_box.send_keys(Keys.DELETE)
        search_text_box.send_keys(SEARCH_LITERATURE)
        time.sleep(3)
        search_button=self.WaitForElementVisible(SEARCH_BUTTON).click()  
        self.driver.execute_script("window.scrollBy(0,400)", "")         
        time.sleep(5)   
        search_icon=self.WaitForElementVisible(SEARCHING).click()
        search_text_box=self.WaitForElementVisible(SEARCH_TEXT_BOX)
        search_text_box.send_keys(Keys.CONTROL + 'a')
        search_text_box.send_keys(Keys.DELETE)
        search_text_box.send_keys(SEARCH_H_G)
        time.sleep(3)
        search_button=self.WaitForElementVisible(SEARCH_BUTTON).click()  
        self.driver.execute_script("window.scrollBy(0,400)", "")         
        time.sleep(5)  

     #Geçersiz kitap adıyla arama durumu(CASE3)
    def invalid_book_name(self):
        self.driver.get("https://el-kitap.org/")
        search_icon=self.WaitForElementVisible(SEARCHING).click()
        search_text_box=self.WaitForElementVisible(SEARCH_TEXT_BOX)
        search_text_box.send_keys(SEARCH_KELIME)
        time.sleep(3)
        search_button=self.WaitForElementVisible(SEARCH_BUTTON).click()
        time.sleep(5)        
        alert_message=self.WaitForElementVisible(ALERT_MESSAGE)
        assert {alert_message.text == ALERT_TEXT}
        self.driver.execute_script("window.scrollBy(0,400)", "")
