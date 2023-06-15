# тест вызывается кнопкой Run
from ya_pages import SearchHelper
from search_page import SearchPageHelper

def test_search(browser): # вызываем фикстуру браузера, чтобы браузер открылся
    ya_main_page = SearchHelper(browser) # вызов главной страницы
    ya_search_page = SearchPageHelper(browser) # вызов страницы с меню под поиском
    ya_main_page.go_to_site() # переходим на сайт
    ya_main_page.enter_word("Privet") # набираем слово, которое будем искать
    ya_main_page.click_on_search_button() # кликаем на кнопку поиска
    elements = ya_search_page.check_navi_bar() # кликаем на меню под поиском
    assert "Картинка" and "Видео" in elements
    print('___')
    print(elements)

