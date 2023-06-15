from selenium.webdriver.common.by import By

from base_page import BasePage

class YaSearchPageLocators:
    # класс для наших локаторов
    LOCATOR_YANDEX_NAVI_BAR = (By.CSS_SELECTOR, ".service__name")

class SearchPageHelper(BasePage):
    # класс для поиска локаторов
    def check_navi_bar(self):
        all_list = self.find_elements(YaSearchPageLocators.
                                      LOCATOR_YANDEX_NAVI_BAR)
        # выведем список названий возвращаемых элементов
        nave_bar_text_menu = [x.text for x in all_list]
        return nave_bar_text_menu











