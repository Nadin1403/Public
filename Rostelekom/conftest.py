import pytest
from selenium import webdriver

# это фикстура, которая будет открывать наш браузер,
# она будет использоваться во всей нашей сессии
@pytest.fixture(scope="session")
def browser():
    driver = webdriver.Chrome()
    # сразу укажем путь к драйверу
    yield driver

    driver.quit() # закроем драйвер






