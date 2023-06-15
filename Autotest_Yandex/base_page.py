from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# определяем наш базовый класс
class BasePage:
    def __init__(self, driver): # принимает наш драйвер
        self.driver = driver
        self.base_url = 'https://ya.ru/'

    # опишем переход на сайт
    def go_to_site(self):
        return self.driver.get(self.base_url)

    # поиск одного элемента
    def find_element(self, locator, time=20):
        return WebDriverWait(self.driver, time).until(EC.presence_of_element_located(locator),
                                                      message=f"Не найден{locator}")

    # поиск нескольких элементов
    def find_elements(self, locator, time=20):
        return WebDriverWait(self.driver, time).until(EC.presence_of_all_elements_located(locator),
                                                      message=f"Не найден{locator}")



