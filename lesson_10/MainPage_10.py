import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@allure.feature("Калькулятор на сайте")
class Calc:
    def __init__(self, driver):
        """
        Инициализация страницы калькулятора.

        :param driver: selenium.webdriver.Chrome / Firefox / и т.д. - драйвер браузера
        :type driver: selenium.webdriver.remote.webdriver.WebDriver
        """
        self.driver = driver
        with allure.step("Открытие страницы калькулятора"):
            self.driver.get("https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")

    @allure.step("Установка задержки равной {delay} секунд")
    def set_delay(self, delay):
        """
        Устанавливает задержку перед выполнением операций.

        :param delay: количество секунд задержки
        :type delay: str или int
        """
        delay_input = self.driver.find_element(By.ID, "delay")
        delay_input.clear()
        delay_input.send_keys(str(delay))

    @allure.step("Нажатие кнопки '{button}'")
    def press_button(self, button):
        """
        Нажимает кнопку калькулятора.

        :param button: текст кнопки (например, '1', '+', '=')
        :type button: str
        """
        self.driver.find_element(By.XPATH, f"//span[text() = '{button}']").click()

    @allure.step("Получение результата: ожидаемый результат '{result}'")
    def get_result(self, result):
        """
        Ожидает появления результата и возвращает текущий текст экрана.

        :param result: ожидаемый результат (например, '2')
        :type result: str
        :return: текущий текст на экране калькулятора
        :rtype: str
        """
        WebDriverWait(self.driver, 45).until(
            EC.text_to_be_present_in_element((By.CLASS_NAME, "screen"), f"{result}")
        )
        res = self.driver.find_element(By.CLASS_NAME, "screen").text
        return res