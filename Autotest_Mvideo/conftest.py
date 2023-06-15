import pytest
from selenium import webdriver

# фикстура, которая будет запускаться в начале каждого нашего теста
# она возвращает нам драйвер
@pytest.fixture(scope="module") # действует на уровне всего модуля
def driver():
    driver = webdriver.Chrome(executable_path="./chromdriver")
    yield driver
    driver.quit()


