from selenium.webdriver.common.by import By
URL="https://el-kitap.org/"
SPECIES=(By.ID,"menu-item-2176")
CHILD= (By.ID,"menu-item-2183")
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