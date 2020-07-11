# #!/usr/bin/env python
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from cart import add_all_products_to_cart, remove_all_products_from_cart
from login import login
import constants 
from datetime import datetime


def main():
    print ('{0:%Y-%m-%d %H:%M:%S} '.format(datetime.now())+'Starting the browser...')
    options = ChromeOptions()
    options.add_argument("--headless") 
    driver = webdriver.Chrome(options=options)
    print ('{0:%Y-%m-%d %H:%M:%S} '.format(datetime.now())+'Browser started successfully. Navigating to the demo page to login.')
    driver.get(constants.BASE_URL)
    login(driver, 'standard_user', 'secret_sauce')
    add_all_products_to_cart(driver)
    remove_all_products_from_cart(driver)

main()