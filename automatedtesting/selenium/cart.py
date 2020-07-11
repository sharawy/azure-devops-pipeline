from datetime import datetime

from selenium.common.exceptions import NoSuchElementException
import constants

def add_all_products_to_cart(driver):
    current_url = driver.current_url
    print('{0:%Y-%m-%d %H:%M:%S} '.format(datetime.now())+"checking products page")
    product_path = 'inventory.html'
    if product_path not in current_url:
        driver.get('{}{}'.format(constants.BASE_URL, product_path))
    print('{0:%Y-%m-%d %H:%M:%S} '.format(datetime.now())+"finding add to cart buttons")
    add_to_cart_btns = driver.find_elements_by_css_selector('div.pricebar > button.btn_primary.btn_inventory')
    print('{0:%Y-%m-%d %H:%M:%S} '.format(datetime.now())+"adding products to cart")
    for btn in add_to_cart_btns:
        btn.click()
    cart_count = driver.find_element_by_class_name("shopping_cart_badge")
    assert int(cart_count.text) == len(add_to_cart_btns), "Failed to add products to cart"
    print('{0:%Y-%m-%d %H:%M:%S} '.format(datetime.now())+"{} products added to cart ".format(cart_count.text))


def remove_all_products_from_cart(driver):
    current_url = driver.current_url
    print('{0:%Y-%m-%d %H:%M:%S} '.format(datetime.now())+"checking products page")
    cart_path = 'cart.html'
    if cart_path not in current_url:
        driver.get('{}{}'.format(constants.BASE_URL, cart_path))
    print('{0:%Y-%m-%d %H:%M:%S} '.format(datetime.now())+"finding remove from cart buttons")
    remove_from_cart_btns = driver.find_elements_by_css_selector('div.item_pricebar > button.btn_secondary.cart_button')
    print('{0:%Y-%m-%d %H:%M:%S} '.format(datetime.now())+"remove products from cart")
    for btn in remove_from_cart_btns:
        btn.click()
    try:
        cart_count = driver.find_element_by_class_name("shopping_cart_badge")
        assert not cart_count, "failed to remove products from cart"
    except NoSuchElementException as e:
        print('{0:%Y-%m-%d %H:%M:%S} '.format(datetime.now())+"{} products removed from cart ".format(len(remove_from_cart_btns)))