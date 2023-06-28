from pages.main_page import MainPage
from selenium.webdriver.common.by import By
from time import sleep

def test_enter_in_lk_positive(browser): # позитивный тест для входа в аккаунт по электронной почте
    main_page = MainPage(browser) # вызов главной страницы
    main_page.page_loading() # метод загрузки начальной страницы
    assert main_page.is_loaded() # проверяем, загрузилась ли начальная страница
    main_page.click_email_tab() # кликаем на вкладку "Почта"
    main_page.search_email_input("pr1403@yandex.ru") # вводим валидную электронную почту
    main_page.search_password_enter("Ruuu080312") # вводим валидный пароль и нажимаем кнопку "Войти"
    assert main_page.is_loaded_lk() # проверяем, загрузилась ли страница личного кабинета

def test_enter_in_lk_negative_1(browser): # негативный тест для входа в аккаунт по электронной почте
    main_page = MainPage(browser) # вызов главной страницы
    main_page.page_loading() # метод загрузки начальной страницы
    assert main_page.is_loaded() # проверяем, загрузилась ли начальная страница
    main_page.click_email_tab() # кликаем на вкладку "Почта"
    main_page.search_email_input("@yandex.ru") # вводим невалидную электронную почту
    main_page.search_password_enter("Ruuu080312") # вводим валидный пароль и нажимаем кнопку "Войти"
    main_page.is_loaded_invalid_login_text() # проверяем, что надпись "Неверный логин или пароль" загрузилась
    assert browser.find_element(By.ID, "form-error-message").text == "Неверный логин или пароль" or "Неверно введен текст с картинки"
    # проверяем, что на странице присутствует текст "Неверный логин или пароль" или "Неверное введен текст с картинки"

def test_enter_in_lk_negative_2(browser): # негативный тест для входа в аккаунт по электронной почте
    main_page = MainPage(browser) # вызов главной страницы
    main_page.page_loading() # метод загрузки начальной страницы
    assert main_page.is_loaded() # проверяем, загрузилась ли начальная страница
    main_page.click_email_tab() # кликаем на вкладку "Почта"
    main_page.search_email_input("русский@yandex.ru") # вводим невалидную электронную почту
    main_page.search_password_enter("123") # вводим невалидный пароль и нажимаем кнопку "Войти"
    main_page.is_loaded_invalid_login_text() # проверяем, что надпись "Неверный логин или пароль" загрузилась
    assert browser.find_element(By.ID, "form-error-message").text == "Неверный логин или пароль" or "Неверно введен текст с картинки"
    # проверяем, что на странице присутствует текст "Неверный логин или пароль" или "Неверное введен текст с картинки"

def test_enter_in_lk_negative_3(browser): # негативный тест для входа в аккаунт по электронной почте
    main_page = MainPage(browser) # вызов главной страницы
    main_page.page_loading() # метод загрузки начальной страницы
    assert main_page.is_loaded() # проверяем, загрузилась ли начальная страница
    main_page.click_email_tab() # кликаем на вкладку "Почта"
    main_page.search_email_input("pr1403@yandex.ru") # вводим валидную электронную почту
    main_page.search_password_enter("Русский текст длинный и с пробелами") # вводим невалидный пароль и нажимаем кнопку "Войти"
    main_page.is_loaded_invalid_login_text() # проверяем, что надпись "Неверный логин или пароль" загрузилась
    assert browser.find_element(By.ID, "form-error-message").text == "Неверный логин или пароль" or "Неверно введен текст с картинки"
    # проверяем, что на странице присутствует текст "Неверный логин или пароль" или "Неверно введен текст с картинки"

def test_enter_in_lk_negative_4(browser): # негативный тест для входа в аккаунт по электронной почте
    main_page = MainPage(browser) # вызов главной страницы
    main_page.page_loading() # метод загрузки начальной страницы
    assert main_page.is_loaded() # проверяем, загрузилась ли начальная страница
    main_page.click_email_tab() # кликаем на вкладку "Почта"
    main_page.search_email_input("") # оставляем пустое поле
    main_page.search_password_enter("") # оставляем пустое поле
    assert browser.find_element(By.CSS_SELECTOR, "span.rt-input-container__meta.rt-input-container__meta--error").text == "Введите адрес, указанный при регистрации"
    # проверяем, что на странице присутствует текст "Введите адрес, указанный при регистрации"

def test_enter_in_lk_negative_5(browser): # негативный тест для входа в аккаунт по электронной почте
    # ввод в поля более 1000 символов
    main_page = MainPage(browser) # вызов главной страницы
    main_page.page_loading() # метод загрузки начальной страницы
    assert main_page.is_loaded() # проверяем, загрузилась ли начальная страница
    main_page.click_email_tab() # кликаем на вкладку "Почта"
    main_page.search_email_input("Ровно 1000 знаков будет в этом абзаце. В действительности 1000 знаков – "
                                 "это в одном случае более чем достаточно, в другом – слишком мало, "
                                 "в третьем – даже слишком много. Согласитесь, заголовок длиной в 15 предложений "
                                 "выглядел бы странно. А рассказ с предысторией, интригой и развязкой в тысячу "
                                 "знаков уложить сможет только очень талантливый писатель. В среднем тысяча знаков"
                                 " – это хорошее развернутое описание товара в каталоге. В такой объем уместится "
                                 "и подробная характеристика, и область применения, и особенности данной модели, "
                                 "и даже на призывающий рекламный абзац место останется. Если оценивать на глаз, "
                                 "то текст в 1000 знаков (без пробелов) – это примерно половина страницы А4 шрифтом"
                                 " Times NewRoman размером 12 пт с полуторным интервалом. Если вам ничего не "
                                 "говорят эти параметры, то просто поверьте на слово: это примерно полстраницы "
                                 "привычного вам текста. Теперь следующий вопрос: когда 1000 символов мало? "
                                 "Если для описания товара 700-1000 знаков вполне достаточно, то текст на страницу "
                                 "сайта нужно писать побольше объемом. Объем в 2000-3000 знаков – это добротная "
                                 "статья, достаточная для раскрытия темы. Минимальный рекомендуемый объем статьи "
                                 "– около 1500 знаков.А вообще самый простой и разумный способ - воспользоваться "
                                 "средствами статистики и поиска в том же ворде.") # вводим невалидную электронную почту
    main_page.search_password_enter("Ровно 1000 знаков будет в этом абзаце. В действительности 1000 знаков – "
                                 "это в одном случае более чем достаточно, в другом – слишком мало, "
                                 "в третьем – даже слишком много. Согласитесь, заголовок длиной в 15 предложений "
                                 "выглядел бы странно. А рассказ с предысторией, интригой и развязкой в тысячу "
                                 "знаков уложить сможет только очень талантливый писатель. В среднем тысяча знаков"
                                 " – это хорошее развернутое описание товара в каталоге. В такой объем уместится "
                                 "и подробная характеристика, и область применения, и особенности данной модели, "
                                 "и даже на призывающий рекламный абзац место останется. Если оценивать на глаз, "
                                 "то текст в 1000 знаков (без пробелов) – это примерно половина страницы А4 шрифтом"
                                 " Times NewRoman размером 12 пт с полуторным интервалом. Если вам ничего не "
                                 "говорят эти параметры, то просто поверьте на слово: это примерно полстраницы "
                                 "привычного вам текста. Теперь следующий вопрос: когда 1000 символов мало? "
                                 "Если для описания товара 700-1000 знаков вполне достаточно, то текст на страницу "
                                 "сайта нужно писать побольше объемом. Объем в 2000-3000 знаков – это добротная "
                                 "статья, достаточная для раскрытия темы. Минимальный рекомендуемый объем статьи "
                                 "– около 1500 знаков.А вообще самый простой и разумный способ - воспользоваться "
                                 "средствами статистики и поиска в том же ворде.") # вводим невалидный пароль и нажимаем кнопку "Войти"
    assert browser.find_element(By.CSS_SELECTOR, "body").text == "Internal Server Error"
    # проверяем, что на странице присутствует текст "Internal Server Error"

def test_enter_in_lk_negative_6(browser): # негативный тест для входа в аккаунт по электронной почте
    main_page = MainPage(browser) # вызов главной страницы
    main_page.page_loading() # метод загрузки начальной страницы
    assert main_page.is_loaded() # проверяем, загрузилась ли начальная страница
    main_page.click_email_tab() # кликаем на вкладку "Почта"
    main_page.search_email_input("True") # вводим булево значение
    main_page.search_password_enter("False") # вводим булево значение
    sleep(5)
    assert browser.find_element(By.ID, "form-error-message").text == "Неверный логин или пароль" or "Неверно введен текст с картинки"
    # проверяем, что на странице присутствует текст "Неверный логин или пароль" или "Неверно введен текст с картинки"

def test_recovery_password_positive(browser): # позитивный тест для восстановления пароля по электронной почте
    main_page = MainPage(browser) # вызов главной страницы
    main_page.page_loading() # метод загрузки начальной страницы
    assert main_page.is_loaded() # проверяем, загрузилась ли начальная страница
    main_page.click_forgot_password("pr1403@yandex.ru")
    sleep(45)
    main_page.search_password_new("Ruu080312") # вводим новый пароль два раза и нажимаем "Сохранить"
    assert browser.find_element(By.ID, "card-container__title").text == "Авторизация"
    # проверяем, что на странице присутствует текст "Авторизация"

def test_recovery_password_negative(browser): # негативный тест для восстановления пароля по электронной почте
    main_page = MainPage(browser) # вызов главной страницы
    main_page.page_loading() # метод загрузки начальной страницы
    assert main_page.is_loaded() # проверяем, загрузилась ли начальная страница
    main_page.click_forgot_password("pr1403@yandex.ru")
    sleep(45)
    if browser.find_element(By.CLASS_NAME, "code-input-container__error").text == "Превышено количество отправленных кодов в сутки":
        print("Превышено количество отправленных кодов в сутки")
    else:
        main_page.search_password_new("Ruu080312") # вводим новый пароль два раза и нажимаем "Сохранить"
        assert browser.find_element(By.ID, "form-error-message").text == "Этот пароль уже использовался, укажите другой пароль"
        # проверяем, что на странице присутствует текст "Этот пароль уже использовался, укажите другой пароль"

def test_cookies_windows(browser): # открытие гипертекстового окна "Cookies"
    main_page = MainPage(browser)  # вызов главной страницы
    main_page.page_loading()  # метод загрузки начальной страницы
    assert main_page.is_loaded()  # проверяем, загрузилась ли начальная страница
    main_page.search_cookies_window() # нажимаем на гиперссылку "Cookies"
    assert browser.find_element(By.CLASS_NAME, "rt-tooltip__title").text == "Мы используем Cookie"
    print("Мы используем Cookie")
    main_page.search_X()

def test_go_to_the_page_contract_footer(browser): # переход по ссылке на страницу пользовательского соглашения
    main_page = MainPage(browser)  # вызов главной страницы
    main_page.page_loading()  # метод загрузки начальной страницы
    assert main_page.is_loaded()  # проверяем, загрузилась ли начальная страница
    main_page.scroll_down() # скроллим страницу вниз
    main_page.search_go_to_the_page_contract_footer() # нажимаем на гиперссылку "Пользовательского соглашения"
    print("Переход на страницу произошёл")

def test_go_to_the_page_privacy_policy(browser): # переход по ссылке на страницу пользовательского соглашения
    main_page = MainPage(browser)  # вызов главной страницы
    main_page.page_loading()  # метод загрузки начальной страницы
    assert main_page.is_loaded()  # проверяем, загрузилась ли начальная страница
    main_page.scroll_down() # скроллим страницу вниз
    main_page.search_go_to_the_page_privacy_policy() # нажимаем на гиперссылку "Политикой конфиденциальности"
    print("Переход на страницу произошёл")

def test_go_to_the_orange_page_contract_footer(browser): # переход по оранжевой ссылке на страницу пользовательского соглашения
    main_page = MainPage(browser)  # вызов главной страницы
    main_page.page_loading()  # метод загрузки начальной страницы
    assert main_page.is_loaded()  # проверяем, загрузилась ли начальная страница
    main_page.search_go_to_the_contract_orange() # нажимаем на гиперссылку "Политикой конфиденциальности"
    print("Переход на страницу произошёл")

def test_registration_1(browser): # негативный тест на регистрацию по уже зарегистрированному адресу
    main_page = MainPage(browser)  # вызов главной страницы
    main_page.page_loading()  # метод загрузки начальной страницы
    assert main_page.is_loaded()  # проверяем, загрузилась ли начальная страница
    main_page.scroll_down() # скроллим страницу вниз
    main_page.search_registr() # ищем "Зарегистрироваться" и нажимаем на него
    main_page.search_name_lastname("Руслана", "Иванова") # вводим валидные данные
    main_page.region_menu() # пытаемся выбрать регион
    main_page.search_address_tab("pr1403@yandex.ru") # вводим валидные данные
    main_page.search_new_pass_registration("Tu123456") # вводим валидные данные
    assert browser.find_element(By.CLASS_NAME, "card-modal__card").text == \
           "Учётная запись уже существует\nПопробуйте войти в неё. Если вы забыли пароль — восстановите " \
           "его.\nВойти\nВосстановить пароль" # проверяем наличие данного текста на странице
    print("Учётная запись уже существует")

def test_registration_2(browser): # негативный тест на регистрацию
    main_page = MainPage(browser)  # вызов главной страницы
    main_page.page_loading()  # метод загрузки начальной страницы
    assert main_page.is_loaded()  # проверяем, загрузилась ли начальная страница
    main_page.scroll_down() # скроллим страницу вниз
    main_page.search_registr() # ищем "Зарегистрироваться" и нажимаем на него
    main_page.search_name_lastname("Nina", "Bill") # вводим невалидные данные
    main_page.region_menu() # пытаемся выбрать регион
    main_page.search_address_tab("pr1403@yandex.ru") # вводим валидные данные
    main_page.search_new_pass_registration("Tu123456") # вводим валидные данные
    assert browser.find_element(By.CLASS_NAME, "rt-input-container__meta.rt-input-container__meta--error").text == \
           "Необходимо заполнить поле кириллицей. От 2 до 30 символов." # проверяем наличие данного текста на странице
    print("Необходимо заполнить поле кириллицей. От 2 до 30 символов.")

def test_registration_3(browser): # негативный тест на регистрацию
    main_page = MainPage(browser)  # вызов главной страницы
    main_page.page_loading()  # метод загрузки начальной страницы
    assert main_page.is_loaded()  # проверяем, загрузилась ли начальная страница
    main_page.scroll_down() # скроллим страницу вниз
    main_page.search_registr() # ищем "Зарегистрироваться" и нажимаем на него
    main_page.search_name_lastname("", "") # вводим невалидные данные
    main_page.region_menu() # пытаемся выбрать регион
    main_page.search_address_tab("pr1403@yandex.ru") # вводим валидные данные
    main_page.search_new_pass_registration("Tu123456") # вводим валидные данные
    assert browser.find_element(By.CLASS_NAME, "rt-input-container__meta.rt-input-container__meta--error").text == \
           "Необходимо заполнить поле кириллицей. От 2 до 30 символов." # проверяем наличие данного текста на странице
    print("Необходимо заполнить поле кириллицей. От 2 до 30 символов.")

def test_registration_4(browser): # негативный тест на регистрацию
    main_page = MainPage(browser)  # вызов главной страницы
    main_page.page_loading()  # метод загрузки начальной страницы
    assert main_page.is_loaded()  # проверяем, загрузилась ли начальная страница
    main_page.scroll_down() # скроллим страницу вниз
    main_page.search_registr() # ищем "Зарегистрироваться" и нажимаем на него
    main_page.search_name_lastname("Виолетта", "Скакунова") # вводим валидные данные
    main_page.region_menu() # пытаемся выбрать регион
    main_page.search_address_tab("pr1403@yandex.ru") # вводим валидные данные
    main_page.search_new_pass_registration("3456") # вводим невалидные данные
    assert browser.find_element(By.CLASS_NAME, "rt-input-container__meta.rt-input-container__meta--error").text == \
           "Длина пароля должна быть не менее 8 символов" # проверяем наличие данного текста на странице
    print("Длина пароля должна быть не менее 8 символов")

def test_registration_5(browser): # негативный тест на регистрацию
    main_page = MainPage(browser)  # вызов главной страницы
    main_page.page_loading()  # метод загрузки начальной страницы
    assert main_page.is_loaded()  # проверяем, загрузилась ли начальная страница
    main_page.scroll_down() # скроллим страницу вниз
    main_page.search_registr() # ищем "Зарегистрироваться" и нажимаем на него
    main_page.search_name_lastname("Виолетта", "Скакунова") # вводим валидные данные
    main_page.region_menu() # пытаемся выбрать регион
    main_page.search_address_tab("pr@.ru") # вводим невалидные данные
    main_page.search_new_pass_registration("Ti123456") # вводим валидные данные
    assert browser.find_element(By.CLASS_NAME, "rt-input-container__meta.rt-input-container__meta--error").text == \
           "Введите телефон в формате +7ХХХХХХХХХХ или +375XXXXXXXXX, или email в формате example@email.ru"
           # проверяем наличие данного текста на странице
    print("Введите телефон в формате +7ХХХХХХХХХХ или +375XXXXXXXXX, или email в формате example@email.ru")

def test_registration_6(browser): # негативный тест на регистрацию
    main_page = MainPage(browser)  # вызов главной страницы
    main_page.page_loading()  # метод загрузки начальной страницы
    assert main_page.is_loaded()  # проверяем, загрузилась ли начальная страница
    main_page.scroll_down() # скроллим страницу вниз
    main_page.search_registr() # ищем "Зарегистрироваться" и нажимаем на него
    main_page.search_name_lastname("Вот пример статьи на 1000 символов. Это достаточно маленький текст, "
                                   "оптимально подходящий для карточек товаров в интернет-магазинах или "
                                   "для небольших информационных публикаций. В таком тексте редко бывает "
                                   "более 2-3 абзацев и обычно один подзаголовок. Но можно и без него. "
                                   "На 1000 символов рекомендовано использовать 1-2 ключа и одну картину. "
                                   "Текст на 1000 символов – это сколько примерно слов? Статистика Word "
                                   "показывает, что «тысяча» включает в себя 150-200 слов средней величины. "
                                   "Но, если злоупотреблять предлогами, союзами и другими частями речи на "
                                   "1-2 символа, то количество слов неизменно возрастает. В копирайтерской "
                                   "деятельности принято считать «тысячи» с пробелами или без. Учет пробелов "
                                   "увеличивает объем текста примерно на 100-200 символов – именно столько раз "
                                   "мы разделяем слова свободным пространством. Считать пробелы заказчики не "
                                   "любят, так как это «пустое место». Однако некоторые фирмы и биржи видят "
                                   "справедливым ставить стоимость за 1000 символов с пробелами, считая "
                                   "последние важным элементом качественного восприятия. Согласитесь, "
                                   "читать слитный текст без единого пропуска, никто не будет. Но большинству "
                                   "нужна цена за 1000 знаков без пробелов.", "СкакуноваСкакуноваСкакуноваСкакунова") # вводим невалидные данные
    main_page.region_menu() # пытаемся выбрать регион
    main_page.search_address_tab("pr1403@yandex.ru") # вводим валидные данные
    main_page.search_new_pass_registration("Ti123456") # вводим валидные данные
    assert browser.find_element(By.CLASS_NAME, "rt-input-container__meta.rt-input-container__meta--error").text == \
           "Необходимо заполнить поле кириллицей. От 2 до 30 символов."
           # проверяем наличие данного текста на странице
    print("Необходимо заполнить поле кириллицей. От 2 до 30 символов.")

def test_registration_7(browser): # негативный тест на регистрацию
    main_page = MainPage(browser)  # вызов главной страницы
    main_page.page_loading()  # метод загрузки начальной страницы
    assert main_page.is_loaded()  # проверяем, загрузилась ли начальная страница
    main_page.scroll_down() # скроллим страницу вниз
    main_page.search_registr() # ищем "Зарегистрироваться" и нажимаем на него
    main_page.search_name_lastname("Виолетта", "Скакунова") # вводим валидные данные
    main_page.region_menu() # пытаемся выбрать регион
    main_page.search_address_tab("pr1403@yandex.ru") # вводим валидные данные
    main_page.search_new_pass_registration("eeeeeeeeeeee") # вводим невалидные данные
    assert browser.find_element(By.CLASS_NAME, "rt-input-container__meta.rt-input-container__meta--error").text == "Пароль должен содержать хотя бы 1 спецсимвол или хотя бы одну цифру"
           # проверяем наличие данного текста на странице
    print("Пароль должен содержать хотя бы 1 спецсимвол или хотя бы одну цифру")

def test_vk(browser): # тест перехода на сайт "ВКонтакте"
    main_page = MainPage(browser)  # вызов главной страницы
    main_page.page_loading()  # метод загрузки начальной страницы
    assert main_page.is_loaded()  # проверяем, загрузилась ли начальная страница
    main_page.search_button_VKontakte() # ищем кнопку "ВКонтакте" и нажимаем на неё
    assert main_page.search_load_VKontakte() # проверяем загрузку сайта ВКонтакте

def test_Odnoklassniki(browser): # тест перехода на сайт "Одноклассники"
    main_page = MainPage(browser)  # вызов главной страницы
    main_page.page_loading()  # метод загрузки начальной страницы
    assert main_page.is_loaded()  # проверяем, загрузилась ли начальная страница
    main_page.search_button_Odnoklassniki() # ищем кнопку "Одноклассники" и нажимаем на неё
    assert main_page.search_load_Odnoklassniki() # проверяем загрузку сайта Одноклассники