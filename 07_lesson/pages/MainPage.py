from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Calc:
    def __init__(self, driver):
        self.driver = driver
        self.driver.get("https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")

    def set_delay(self, delay):
        delay_input = self.driver.find_element(By.ID, "delay")
        delay_input.clear()
        delay_input.send_keys(delay)

    def press_button(self, button):
        self.driver.find_element(By.XPATH, f"//span[text() = '{button}']").click()

    def get_result(self, result):
        WebDriverWait(self.driver, 45).until(
            EC.text_to_be_present_in_element((By.CLASS_NAME, "screen"), f"{result}")
        )
        res = self.driver.find_element(By.CLASS_NAME, "screen").text
        return res