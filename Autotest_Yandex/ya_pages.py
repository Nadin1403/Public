from selenium.webdriver.common.by import By

from base_page import BasePage

class YaSearchLocators:
    # определяем необходимые локаторы
    LOCATOR_YANDEX_SEARCH_FIELD = (By.ID, "text") # локатор поискового поля
    LOCATOR_YANDEX_SEARCH_BUTTON = (By.XPATH,
                                    "//button[contains(text(), 'Найти')]")
                                    # локатор кнопки "Найти"

class SearchHelper(BasePage):
    # класс, который будет искать
    def enter_word(self, word): # передаем слово, которое будем искать
        search_field = self.find_element(YaSearchLocators.
                                         LOCATOR_YANDEX_SEARCH_FIELD)
                                        # передаем класс локаторов и локатор
        search_field.click() # кликаем на локатор
        # после этого локатор активируется и мы вводим слово, которое будем искать
        search_field.send_keys(word)
        return search_field # возвращаем как раз это поле

    # метод для поиска(клика)
    def click_on_search_button(self):
        return self.find_element(YaSearchLocators.
                                 LOCATOR_YANDEX_SEARCH_BUTTON, time=2).click()






