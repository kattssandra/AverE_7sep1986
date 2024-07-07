import allure
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from pages.MainPage import MainPage

@allure.title("Открытие сайта")
@allure.description("Тест проверяет наличие связи с сайтом")
@allure.feature("READ")
@allure.severity("blocker")
@pytest.mark.positive_test
def test_opening(): 
    with allure.step("Открытие веб-страницы в Chrome и выполнение поиска"):
        browser = webdriver.Chrome() 
        main_page = MainPage(browser)  

@allure.title("Добавление товара в корзину")
@allure.description("Тест проверяет, что товар добавляется в корзину и отображение суммы заказа")
@allure.feature("READ")
@allure.severity("blocker")
@pytest.mark.positive_test
def test_add_item():
    with allure.step("Открытие веб-страницы в Chrome"):
        browser = webdriver.Chrome()
        main_page = MainPage(browser)
    with allure.step("Проверка суммы покупки: 1280"):
        msg = main_page.add_item()
        assert msg == "1280"
    with allure.step("Закрытие браузера"):
        main_page.close_driver()