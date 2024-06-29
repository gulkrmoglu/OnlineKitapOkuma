from OnlineKitapOkumaSitesi.pages.constants.globalConstants import *
from OnlineKitapOkumaSitesi.pages.PageBase import PageBase
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import time

class CategoryAndAuthor(PageBase):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    #Belirli bir kategori seçilerek kitapların listelenmesi durumu.(CASE 1)
    def category(self):
        species=self.WaitForElementVisible(SPECIES)
        actions = ActionChains(self.driver)
        actions.move_to_element(species).perform()
        time.sleep(6)
        #self.driver.execute_script("window.scrollBy(0,400)", "")
        child=self.WaitForElementVisible(CHILD)
        self.driver.execute_script("arguments[0].scrollIntoView(true);", child)
        self.driver.get("https://el-kitap.org/e-kitaplar/deneme/")
        self.driver.execute_script("window.scrollBy(0,500)", "")

    #Belirli bir yazar seçilerek kitaplarının listelenmesi durumu.
    def author(self):
        self.driver.get("https://el-kitap.org/")
        search_icon=self.WaitForElementVisible(SEARCHING).click()
        search_text_box=self.WaitForElementVisible(SEARCH_TEXT_BOX)
        search_text_box.send_keys(SEARCH_AUTHOR)
        time.sleep(3)
        search_button=self.WaitForElementVisible(SEARCH_BUTTON).click()       
        time.sleep(5)        
        self.driver.execute_script("window.scrollBy(0,500)", "")
        
    #Geçersiz kategori seçilmesi durumu(CASE3)
    def invalid_category(self):
        self.driver.get("https://el-kitap.org/")
        search_icon=self.WaitForElementVisible(SEARCHING).click()
        search_text_box=self.WaitForElementVisible(SEARCH_TEXT_BOX)
        search_text_box.send_keys(SEARCH_CATEGORY)
        time.sleep(3)
        search_button=self.WaitForElementVisible(SEARCH_BUTTON).click()
        time.sleep(5)        
        alert_message=self.WaitForElementVisible(ALERT_MESSAGE)
        assert {alert_message.text == ALERT_TEXT}
        self.driver.execute_script("window.scrollBy(0,400)", "")

    def invalid_author(self):
        self.driver.get("https://el-kitap.org/")
        search_icon=self.WaitForElementVisible(SEARCHING).click()
        search_text_box=self.WaitForElementVisible(SEARCH_TEXT_BOX)
        search_text_box.send_keys(SEARCHTEXTBOX)
        time.sleep(3)
        search_button=self.WaitForElementVisible(SEARCH_BUTTON).click()
        time.sleep(5)        
        alert_message=self.WaitForElementVisible(ALERT_MESSAGE)
        assert {alert_message.text == ALERT_TEXT}
        self.driver.execute_script("window.scrollBy(0,400)", "")









              
     

        
       
        

