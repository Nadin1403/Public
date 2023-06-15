import pytest
from selenium import webdriver

# фикстура, которая будет открывать наш браузер,
# она будет использоваться во всей нашей сессии
@pytest.fixture(scope="session")
def browser():
    # сразу укажем путь к нашему драйверу
    driver = webdriver.Chrome(executable_path="./chromdriver")
    yield driver
    driver.quit() # для закрытия драйвера



