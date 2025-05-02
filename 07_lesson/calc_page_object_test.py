from selenium import webdriver
from pages.MainPage import Calc


def test_calc():
    driver = webdriver.Chrome()
    calc = Calc(driver)
    calc.set_delay("1")

    calc.press_button('7')
    calc.press_button('+')
    calc.press_button('8')
    calc.press_button('=')

    result = calc.get_result("15")

    assert result == "15"

    driver.quit()