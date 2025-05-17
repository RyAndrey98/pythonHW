import pytest
import allure
from selenium import webdriver
from MainPage_10 import Calc


@allure.title("Тест сложения 7 + 8 = 15")
@allure.description("Проверка корректности выполнения сложения в онлайн-калькуляторе.")
@allure.feature("Калькулятор")
@allure.severity(allure.severity_level.CRITICAL)
def test_calc():
    with allure.step("Запуск браузера и создание экземпляра драйвера"):
        driver = webdriver.Chrome()
    calc = Calc(driver)

    try:
        with allure.step("Установка задержки в 1 секунду для стабильности теста"):
            calc.set_delay(1)

        with allure.step("Ввод числа 7"):
            calc.press_button('7')

        with allure.step("Нажатие '+'"):
            calc.press_button('+')

        with allure.step("Ввод числа 8"):
            calc.press_button('8')

        with allure.step("Нажатие '=' для получения результата"):
            calc.press_button('=')

        with allure.step("Проверка результата равенства '15'"):
            result = calc.get_result('15')
            assert result == '15', f"Ожидалось '15', получено '{result}'"
    finally:
        with allure.step("Закрытие браузера"):
            driver.quit()