from time import sleep

from selenium import webdriver
from pages.shop_page import Shop

def test_shop():
    driver = webdriver.Chrome()
    shop = Shop(driver)
    shop.auth("standard_user", "secret_sauce")

    shop.add_to_cart("add-to-cart-sauce-labs-backpack")
    shop.add_to_cart("add-to-cart-sauce-labs-bolt-t-shirt")
    shop.add_to_cart("add-to-cart-sauce-labs-onesie")
    shop.go_to_cart()
    shop.checkout()

    shop.fill_info("Andrey", "Rybakov", "346901")

    total = shop.get_sum()

    assert total == "Total: $58.29"

    driver.quit()