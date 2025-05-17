import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@allure.feature("Магазин на сайте saucedemo")
class Shop:
    def __init__(self, driver):
        """
        Инициализация страницы магазина.

        :param driver: экземпляр WebDriver для взаимодействия с браузером.
        :type driver: selenium.webdriver.remote.webdriver.WebDriver
        """
        self.driver = driver
        with allure.step("Переход на страницу магазина"):
            self.driver.get("https://www.saucedemo.com/")

    @allure.step("Авторизация с логином '{login}' и паролем '{password}'")
    def auth(self, login: str, password: str) -> None:
        """
        Выполняет вход в аккаунт.

        :param login: логин пользователя.
        :type login: str
        :param password: пароль пользователя.
        :type password: str
        """
        self.driver.find_element(By.ID, "user-name").send_keys(login)
        self.driver.find_element(By.ID, "password").send_keys(password)
        self.driver.find_element(By.ID, "login-button").click()

    @allure.step("Добавление товара '{item}' в корзину")
    def add_to_cart(self, item: str) -> None:
        """
        Добавляет товар в корзину по идентификатору.

        :param item: id элемента товара.
        :type item: str
        """
        self.driver.find_element(By.ID, item).click()

    @allure.step("Переход в корзину")
    def go_to_cart(self) -> None:
        """
        Переходит в корзину.
        """
        self.driver.find_element(By.CSS_SELECTOR, "a.shopping_cart_link").click()

    @allure.step("Переход к оформлению заказа")
    def checkout(self) -> None:
        """
        Начинает оформление заказа.
        """
        self.driver.find_element(By.ID, "checkout").click()

    @allure.step("Заполнение информации о покупателе: {first_name} {last_name}, {postal_code}")
    def fill_info(self, first_name: str, last_name: str, postal_code: str) -> None:
        """
        Заполняет форму данных покупателя.

        :param first_name: имя.
        :type first_name: str
        :param last_name: фамилия.
        :type last_name: str
        :param postal_code: почтовый индекс.
        :type postal_code: str
        """
        WebDriverWait(self.driver, 15).until(EC.presence_of_element_located((By.ID, "first-name")))
        self.driver.find_element(By.ID, "first-name").send_keys(first_name)
        self.driver.find_element(By.ID, "last-name").send_keys(last_name)
        self.driver.find_element(By.ID, "postal-code").send_keys(postal_code)
        self.driver.find_element(By.ID, "continue").click()

    @allure.step("Получение суммы заказа")
    def get_sum(self) -> str:
        """
         Получает сумму заказа из итоговой строки.

         :return: строка с суммой (например, 'Total: $9.99').
         :rtype: str
         """
        total = self.driver.find_element(By.CSS_SELECTOR, "div.summary_total_label").text
        return total