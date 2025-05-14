import pytest
import allure
from selenium import webdriver
from shop_page_10 import Shop

@allure.title("Тест оформления заказа на сайте saucedemo")
@allure.description("Авторизация и оформление заказа с проверкой суммы.")
@allure.feature("Магазин")
@allure.severity(allure.severity_level.CRITICAL)
def test_shop():
    with allure.step("Запуск браузера и создание драйвера"):
        driver = webdriver.Chrome()
    shop = Shop(driver)

    try:
        with allure.step("Авторизация под пользователем 'standard_user'"):
            shop.auth("standard_user", "secret_sauce")

        with allure.step("Добавление товаров в корзину"):
            shop.add_to_cart("add-to-cart-sauce-labs-backpack")
            shop.add_to_cart("add-to-cart-sauce-labs-bolt-t-shirt")
            shop.add_to_cart("add-to-cart-sauce-labs-onesie")

        with allure.step("Переход в корзину"):
            shop.go_to_cart()

        with allure.step("Начало оформления заказа"):
            shop.checkout()

        with allure.step("Заполнение данных покупателя"):
            shop.fill_info("Andrey", "Rybakov", "346901")

        with allure.step("Получение итоговой суммы заказа"):
            total = shop.get_sum()
            with allure.step(f"Итоговая сумма отображается как '{total}'"):
                assert total == "Total: $58.29"

    finally:
       with allure.step("Закрытие браузера"):
           driver.quit()