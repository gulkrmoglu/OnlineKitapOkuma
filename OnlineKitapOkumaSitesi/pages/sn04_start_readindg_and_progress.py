from OnlineKitapOkumaSitesi.pages.constants.globalConstants import *
from OnlineKitapOkumaSitesi.pages.PageBase import PageBase
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import time

class StartReadingAndProgress(PageBase):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
    #Okumaya başlanması ve okuma ilerlemesinin durumu (case1)
    def start_reading_and_progress(self):
        species=self.WaitForElementVisible(SPECIES)
        actions = ActionChains(self.driver)
        actions.move_to_element(species).perform()
        time.sleep(6)
        philosophy=self.WaitForElementVisible(PHILOSOPHY).click()
        time.sleep(20)
        self.driver.execute_script("window.scrollBy(0,400)", "")
        thomas=self.WaitForElementVisible(THOMAS).click()
        time.sleep(10)
        self.driver.execute_script("window.scrollBy(0,600)", "")
        time.sleep(30)
        read = self.WaitForElementVisible(READ).click()
        time.sleep(10)   
        for _ in range(5):  
            actions.send_keys(Keys.RIGHT).perform()
            time.sleep(2)  
        time.sleep(20)
        

        
       
        
