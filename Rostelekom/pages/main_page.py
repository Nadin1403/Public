from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from time import sleep

class MainPage:
    def __init__(self, driver):
        self.driver = driver
        self.email_tab = (By.ID, "t-btn-tab-mail") # вкладка "Почта"
        self.email_box = (By.ID, 'username') # поле ввода электронной почты
        self.password = (By.ID, "password") # поле ввода пароля
        self.enter_button = (By.ID, "kc-login") # кнопка "Войти"
        self.continue_button = (By.ID, "reset") # кнопка "Продолжить"
        self.register = (By.CSS_SELECTOR, "a#kc-register.rt-link.rt-link--orange") # гиперссылка "Зарегистрироваться"
        self.contract_orange = (By.CSS_SELECTOR, "a.rt-link.rt-link--orange") # оранжевая надпись "пользовательского соглашения"
        self.contract_footer = (By.CSS_SELECTOR, "span.rt-footer-left__item-accent") # "Пользовательским соглашением" в подвале
        self.privacy_policy = (By.CSS_SELECTOR, "span.rt-footer-left__item-accent") # "Политика конфиденциальности" в подвале
        self.cookies = (By.ID, "cookies-tip-open") # надпись "Cookies" в подвале
        self.forgot_password = (By.ID, "forgot_password") # надпись "Забыл пароль"
        self.lk_btn = (By.ID, "lk-btn") # кнопка личного кабинета на странице личного кабинета
        self.invalid_login_text = (By.ID, "form-error-message") # надпись "Неправильный логин или пароль"
        self.password_new = (By.ID, "password-new") # поле "Новый пароль"
        self.password_confirm = (By.ID, "password-confirm") # поле "Повторить пароль"
        self.save_button = (By.ID, "t-btn-reset-pass")  # кнопка "Сохранить"
        self.cookies_title = (By.CLASS_NAME, "rt-tooltip__title") # текст про куки во всплывающем окне
        self.X = (By.CLASS_NAME, "rt-tooltip__close") # кнопка крестик закрытия окна
        self.offer_title = (By.CLASS_NAME, 'offer - title') # заголовок пользовательского соглашения
        self.name = (By.NAME, "firstName") # поле "Имя"
        self.lastname = (By.NAME, "lastName")  # поле "Фамилия"
        self.region = (By.CLASS_NAME, "rt-select.rt-select--search.register-form__dropdown") # поле "Регион"
        self.V = (By.CLASS_NAME, 'rt-input.rt-input--rounded.rt-input--orange.rt-input--actions') # кнопка галочка
        self.address = (By.ID, 'address') # поле "Почта или телефон"
        self.password_new_reg = (By.ID, "password") # поле "Новый пароль"
        self.register_button = (By.NAME, 'register') # кнопка "Зарегистрироваться"
        self.VK = (By.ID, "oidc_vk") # социальная сеть "ВКонтакте"
        self.VKsite = (By.CSS_SELECTOR, "span.vkuiButton__content.vkuiText.vkuiText--"
                                        "sizeY-compact.vkuiText--w-2") # поле на сайте "ВКонтакте"
        self.Odnoklassniki = (By.ID, "oidc_ok") # социальная сеть "Одноклассники"
        self.Odnoklassnikisite = (By.ID, "field_email") # поле на сайте "Одноклассники"



    def page_loading(self): # метод загрузки начальной страницы
        self.driver.get("https://b2c.passport.rt.ru/auth/realms/b2c/protocol/"
                        "openid-connect/auth?client_id=account_b2c&redirect_uri"
                        "=https://b2c.passport.rt.ru/account_b2c/login?theme%3Dl"
                        "ight&response_type=code&scope=openid&state=6706e633-21d8"
                        "-478b-baac-d9593dff15a5&theme=light&auth_type")

    def is_loaded(self): # метод проверки загрузки начальной страницы
        try:
            WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(self.password))
            return True
        except:
            return False

    def scroll_down(self): # метод скроллинга страницы вниз на 500 пикселей
        self.driver.execute_script("window.scrollTo(0, 500)")


    def click_email_tab(self): # метод, который выбирает вкладку "Почта" и нажимает на неё
        search_email_tab = self.driver.find_element(*self.email_tab) # ищем вкладку электронной почты
        search_email_tab.click() # нажимаем на элемент

    def search_email_input(self, email): # метод, вводящий электронную почту в поле
        search_email_box = self.driver.find_element(*self.email_box)  # ищем поле ввода электронной почты
        search_email_box.clear() # очищаем поле ввода электронной почты
        search_email_box.send_keys(email) # вводим электронную почту

    def search_password_enter(self, passwrd): # метод, вводящий пароль в поле и нажимающий на кнопку "Войти"
        search_password = self.driver.find_element(*self.password)  # ищем поле ввода пароля
        search_password.clear() # очищаем поле ввода пароля
        search_password.send_keys(passwrd) # вводим пароль
        sleep(30)
        search_enter_button = self.driver.find_element(*self.enter_button) # ищем кнопку "Войти"
        search_enter_button.click()  # нажимаем кнопку "Войти"

    def is_loaded_lk(self): # метод проверки загрузки страницы личного кабинета
        try:
            WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(self.lk_btn))
            return True
        except:
            return False

    def is_loaded_invalid_login_text(self): # метод проверки загрузки надписи "Неверный логин или пароль"
        try:
            WebDriverWait(self.driver, 20).until(EC.presence_of_element_located(self.invalid_login_text))
            return True
        except:
            return False

    def click_forgot_password(self, email): # метод, который нажимает на кнопку "Забыли пароль"
        search_forgot_password = self.driver.find_element(*self.forgot_password) # ищем кнопку "Забыли пароль"
        search_forgot_password.click() # нажимаем на кнопку "Забыли пароль"
        search_email_tab = self.driver.find_element(*self.email_tab)  # ищем вкладку электронной почты
        search_email_tab.click() # нажать на вкладку "Почта"
        search_email_box = self.driver.find_element(*self.email_box)  # ищем поле ввода электронной почты
        search_email_box.clear()  # очищаем поле ввода электронной почты
        search_email_box.send_keys(email)  # вводим электронную почту
        sleep(30)
        search_continue_button = self.driver.find_element(*self.continue_button)  # ищем кнопку "Продолжить"
        search_continue_button.click() # нажимаем кнопку "Продолжить"

    def search_password_new(self, passwrd): # метод, вводящий новый пароль,
        # вводящий повторно пароль в поле и нажимающий на кнопку "Сохранить"
        search_password_new = self.driver.find_element(*self.password_new)  # ищем поле ввода нового пароля
        search_password_new.clear() # очищаем поле ввода пароля
        search_password_new.send_keys(passwrd) # вводим новый пароль
        search_password_confirm = self.driver.find_element(*self.password_confirm)  # ищем поле повторного ввода пароля
        search_password_confirm.clear() # очищаем поле повторного ввода пароля
        search_password_confirm.send_keys(passwrd) # вводим повторно пароль
        sleep(5)
        search_save_button = self.driver.find_element(*self.save_button) # ищем кнопку "Сохранить"
        search_save_button.click()  # нажимаем кнопку "Сохранить"

    def search_cookies_window(self): # метод поиска гиперссылки "Cookies" и нажате на неё
        search_cookies = self.driver.find_element(*self.cookies)  # ищем гиперссылку "Cookies"
        search_cookies.click()  # нажимаем на элемент

    def search_X(self): # метод поиска кнопки с крестиком и нажатие на неё
        search_X_button = self.driver.find_element(*self.X)
        search_X_button.click()

    def search_go_to_the_page_contract_footer(self): # метод поиска гиперссылки
        # "Пользовательским соглашением" и нажате на неё
        search_contract_footer = self.driver.find_element(*self.contract_footer)
        search_contract_footer.click()

    def is_loaded_contract(self): # метод проверки загрузки страницы пользовательского соглашения
        try:
            WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(self.offer_title))
            return True
        except:
            return False

    def search_go_to_the_page_privacy_policy(self): # метод поиска гиперссылки
        # "Политика конфиденциальности" и нажатие на неё
        search_privacy_policy = self.driver.find_element(*self.privacy_policy)
        search_privacy_policy.click()

    def search_go_to_the_contract_orange(self): # метод поиска оранжевой гиперссылки
        # "пользовательского соглашения" и нажатие на неё
        search_contract_orange = self.driver.find_element(*self.contract_orange)
        search_contract_orange.click()

    def search_registr(self): # метод поиска гиперссылки "Зарегистрироваться" и нажатие на неё
        search_register = self.driver.find_element(*self.register)
        search_register.click()

    def search_name_lastname(self, name, lastname): # метод поиска полей имени и фамилии и ввод их
        search_name = self.driver.find_element(*self.name) # ищем элемент "Имя"
        search_name.clear()  # очищаем поле ввода имени
        search_name.send_keys(name)  # вводим имя
        search_lastname = self.driver.find_element(*self.lastname) # ищем элемент "Фамилия"
        search_lastname.clear()  # очищаем поле ввода фамилии
        search_lastname.send_keys(lastname)  # вводим фамилию

    def search_address_tab(self, adress): # ищем поле "почта или телефон" и вводим почту или телефон
        search_address = self.driver.find_element(*self.address)  # ищем элемент в "почта или телефон"
        search_address.clear() # очищаем поле ввода почты или телефона
        search_address.send_keys(adress) # вводим почту или телефон

    def search_new_pass_registration(self, passwrd): # метод, вводящий новый пароль,
        # вводящий повторно пароль в поле и нажимающий на кнопку "Сохранить"
        search_new_pass = self.driver.find_element(*self.password_new_reg)  # ищем поле ввода нового пароля
        search_new_pass.clear() # очищаем поле ввода пароля
        search_new_pass.send_keys(passwrd) # вводим новый пароль
        search_pass_confirm = self.driver.find_element(*self.password_confirm)  # ищем поле повторного ввода пароля
        search_pass_confirm.clear() # очищаем поле повторного ввода пароля
        search_pass_confirm.send_keys(passwrd) # вводим повторно пароль
        search_register_button = self.driver.find_element(*self.register_button) # ищем кнопку "Зарегистрироваться"
        search_register_button.click()  # нажимаем кнопку "Зарегистрироваться"

    def region_menu(self): # метод, который пытается выбрать регион
        search_region = self.driver.find_element(*self.region)
        search_region.click()
        search_V = self.driver.find_element(*self.V)
        search_V.click()

    def search_button_VKontakte(self): # метод, который ищет кнопку "ВКонтакте" и нажимает на неё
        search_VK = self.driver.find_element(*self.VK)
        search_VK.click()

    def search_load_VKontakte(self): # метод, который проверяет загрузку сайта ВКонтакте
        try:
            WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(self.VKsite))
            return True
        except:
            return False

    def search_button_Odnoklassniki(self): # метод, который ищет кнопку "Одноклассники" и нажимает на неё
        search_VK = self.driver.find_element(*self.Odnoklassniki)
        search_VK.click()

    def search_load_Odnoklassniki(self): # метод, который проверяет загрузку сайта Одноклассники
        try:
            WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(self.Odnoklassnikisite))
            return True
        except:
            return False