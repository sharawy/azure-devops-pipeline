# #!/usr/bin/env python
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions


# Start the browser and login with standard_user
def login (driver, user, password):
    print('trying to login using credentials {} {}'.format(user,password) )
    driver.find_element_by_css_selector("#user-name").send_keys(user)
    driver.find_element_by_css_selector("#password").send_keys(password)
    driver.find_element_by_css_selector("#login_button_container > div > form > input.btn_action").click()
    assert "inventory.html" in driver.current_url, "Failed to login."
    print("login suscessfull")

