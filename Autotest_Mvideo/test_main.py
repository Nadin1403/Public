# тесты запускаются кнопкой Run

from time import sleep
from pages.main_page import MainPage

def test_search(driver):
    main_page = MainPage(driver) # инициализация, приведение к рабочей готовности
    main_page.load() # загружаем страницу
    assert main_page.is_loaded() # проверяем, загрузилась ли страница
    main_page.search_for_product("iPhone") # вводим текст
    sleep(10)
    assert driver.current_url.startswith("https://www.mvideo.ru/smartfony-i-svyaz")
    # проверяем, что загруженная страница содержит в себе прописанный адрес




