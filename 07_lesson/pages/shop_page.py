from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class Shop:
    def __init__(self, driver):
        self.driver = driver
        self.driver.get("https://www.saucedemo.com/")

    def auth(self, login, password):
        self.driver.find_element(By.ID, "user-name").send_keys(login)
        self.driver.find_element(By.ID, "password").send_keys(password)
        self.driver.find_element(By.ID, "login-button").click()

    def add_to_cart(self, item):
        self.driver.find_element(By.ID, item).click()

    def go_to_cart(self):
        self.driver.find_element(By.CSS_SELECTOR, "a.shopping_cart_link").click()

    def checkout(self):
        self.driver.find_element(By.ID, "checkout").click()

    def fill_info(self, first_name, last_name, postal_code):
        WebDriverWait(self.driver, 15).until(EC.presence_of_element_located((By.ID, "first-name")))
        self.driver.find_element(By.ID, "first-name").send_keys(first_name)
        self.driver.find_element(By.ID, "last-name").send_keys(last_name)
        self.driver.find_element(By.ID, "postal-code").send_keys(postal_code)
        self.driver.find_element(By.ID, "continue").click()

    def get_sum(self):
        total = self.driver.find_element(By.CSS_SELECTOR, "div.summary_total_label").text
        return total