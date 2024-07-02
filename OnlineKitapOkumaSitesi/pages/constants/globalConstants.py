from selenium.webdriver.common.by import By
URL="https://el-kitap.org/"
SPECIES=(By.ID,"menu-item-2176")
CHILD= (By.ID,"menu-item-2183")
ATTEMPT=(By.ID,"menu-item-2184")
ATTEMPT_CSS=(By.CSS_SELECTOR,"#top-menu > #menu-item-2176 #menu-item-2184 > a")
SEARCHING=(By.CSS_SELECTOR,"#masthead > div > div.header-search > span")
SEARCH_TEXT_BOX=(By.CSS_SELECTOR,"#page > div.search-screen.js-search-screen.open > form > label > input")
SEARCH_AUTHOR="Stefan Zweig"
SEARCH_CATEGORY="Hollandaca"
SEARCH_BUTTON= (By.CSS_SELECTOR,"#page > div.search-screen.js-search-screen.open > form > button")
ALERT_MESSAGE=(By.CSS_SELECTOR,"#main > section")
ALERT_TEXT="Nothing Found.Sorry, but nothing matched your search terms. Please try again with some different keywords."
SEARCHTEXTBOX="Gül Karamahmutoğlu"
SEARCH_BOOK="Amok Koşucusu"
SEARCH_WORLD_CLASSICS="Dünya Klasikleri ve Fyodor Dostoyevski"
SEARCH_LITERATURE="Edebiyat ve Ekonomi"
SEARCH_H_G="H G"
SEARCH_KELIME="xyzAbDF"
STORY=(By.ID,"menu-item-2202")
STEPHAN=(By.CSS_SELECTOR,".post-card:nth-child(1) > .post-card__body a")
SEARCH_STORY="öykü"
PHILOSOPHY=(By.CSS_SELECTOR,"#top-menu > #menu-item-2176 #menu-item-2192 > a")
THOMAS=(By.CSS_SELECTOR,".post-card:nth-child(1) > .post-card__body a")
READ=(By.CSS_SELECTOR,".entry-content > p > .btn:nth-child(1)")
PAGEONE=(By.XPATH,"//div[@id='pagesContainer_documentViewer_arrowright']")
#(By.CSS_SELECTOR,"#pagesContainer_documentViewer_arrowright")
#(By.ID,"pagesContainer_documentViewer_arrowright")
DOWNLOAD=(By.CSS_SELECTOR,"https://el-kitap.org/thomas-more-utopia/#n1")
DOWNLOAD_XPATH=(By.XPATH,"//*[@id='toolbar_documentViewer']/img[2]")




