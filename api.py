import allure
import requests
import pytest
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait

base_url = "https://altaivita.ru/"

@allure.title("Добавление товара в корзину")
@allure.description("Тест проверяет добавление одного товара в корзину")
@allure.feature("ADD")
@allure.severity("blocker")
@pytest.mark.positive_test

def test_add_product():
     data = {
    "productID":"1280",
    "LANG_key":"ru",
    "S_wh":"1",
    "S_CID":"b1bd0ff9e785cf7d975fac493a88c023",
    "S_cur_code":"usd",
    "S_koef":"0.01401",
    "S_hint_code":""
   }
     headers = { 
    'content-type': "charset=UTF-8"
}
     resp = requests.get(base_url+'engine/ajax/ajax_ecommerce/ajax_ecommerce.php', data=data, headers=headers)
     assert resp.status_code == 200
     assert resp.headers["Content-Type"] == "charset=UTF-8"


@allure.title("Удаление товара из корзины")
@allure.description("Тест проверяет удаление товара из корзины")
@allure.feature("DELETE")
@allure.severity("blocker")
@pytest.mark.positive_test

def test_delete_product():
     
     data = {
    "productID":"1280",
    "LANG_key":"ru",
    "S_wh":"1",
    "S_CID":"b1bd0ff9e785cf7d975fac493a88c023",
    "S_cur_code":"usd",
    "S_koef":"0.01401",
    "S_hint_code":""
   } 
     headers = { 
    'content-type': 'charset=UTF-8'
}
     resp = requests.get(base_url+'engine/cart/delete_products_from_cart_preview.php', data=data, headers=headers)
     assert resp.status_code == 200
     assert resp.headers["Content-Type"] == "charset=UTF-8"

