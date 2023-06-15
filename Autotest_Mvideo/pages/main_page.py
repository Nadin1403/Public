from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from time import sleep

class MainPage:
    # в этом классе мы будем описывать объекты, которые у нас есть и все методы
    def __init__(self, driver):# метод, описывающий все необходимые объекты
        self.driver = driver
        self.search_box = (By.ID, "1") # поле ввода запроса
        self.search_button = (By.CSS_SELECTOR,
                              'div[class="search-icon-wrap ng-star-inserted"]')
                              # кнопка поиска с лупой

    def load(self): # метод загрузки начальной страницы
        self.driver.get("https://www.mvideo.ru")

    def is_loaded(self):
        # метод проверки загрузки страницы
        try:
            WebDriverWait(self.driver, 10).until(EC.presence_of_element_located
                                                 (self.search_box))
            return True
        except:
            return False

    def search_for_product(self, query):
        # метод, позволяющий нам писать в строке поиска
        search_input = self.driver.find_element(*self.search_box) # ищем элемент
        search_input.clear() # очищаем поле ввода
        search_input.send_keys(query) # вводим текст
        sleep(5)
        self.driver.find_element(*self.search_button).click() # нажимаем на кнопку поиска








