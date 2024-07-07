import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class MainPage:
      def __init__(self, driver):
        self._driver = driver
        self._driver.get("https://altaivita.ru/")
        self._driver.implicitly_wait(20)
        self._driver.maximize_window()

with allure.step("Добавить товар в корзину"):
            def add_product(self):
                 self._driver.get("https://altaivita.ru/")
                 self._driver.find_element(By.XPATH, '/div.product__add_2_0.js-product__add_2_0_cat_preview_1280').click()
                 counter = self._driver.find_element(By.XPATH,'/div.product__add_2_0.js-product__add_2_0_cat_preview_1280').text
                 return counter 
            
