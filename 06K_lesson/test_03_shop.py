from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_shop():
    driver = webdriver.Chrome()
    driver.get("https://www.saucedemo.com/")

    driver.find_element(By.ID, "user-name").send_keys("standard_user")
    driver.find_element(By.ID, "password").send_keys("secret_sauce")
    driver.find_element(By.ID, "login-button").click()

    driver.find_element(By.ID, "add-to-cart-sauce-labs-backpack").click()
    driver.find_element(By.ID, "add-to-cart-sauce-labs-bolt-t-shirt").click()
    driver.find_element(By.ID, "add-to-cart-sauce-labs-onesie").click()

    driver.find_element(By.CSS_SELECTOR, "a.shopping_cart_link").click()

    driver.find_element(By.ID, "checkout").click()

    WebDriverWait(driver, 15).until(EC.presence_of_element_located((By.ID, "first-name")))

    driver.find_element(By.ID, "first-name").send_keys("Andrey")
    driver.find_element(By.ID, "last-name").send_keys("Rybakov")
    driver.find_element(By.ID, "postal-code").send_keys("346901")
    driver.find_element(By.ID, "continue").click()

    total = driver.find_element(By.CSS_SELECTOR, "div.summary_total_label").text
    print(total)

    assert total == "Total: $58.29"

    driver.quit()

