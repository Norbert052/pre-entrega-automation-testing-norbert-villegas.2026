from selenium.webdriver.common.by import By
from utils.helpers import wait_for_element
from utils.logger import logger


class CartPage:
    CART_CONTAINER = (By.CLASS_NAME, "cart_contents_container")
    CART_ITEMS = (By.CLASS_NAME, "cart_item")
    PRODUCT_NAME = (By.CLASS_NAME, "inventory_item_name")

    def __init__(self, driver):
        self.driver = driver

    def wait_until_loaded(self):
        logger.info("Esperando carga de carrito")
        return wait_for_element(self.driver, self.CART_CONTAINER)

    def get_cart_items_count(self):
        count = len(self.driver.find_elements(*self.CART_ITEMS))
        logger.info("Elementos en carrito: %s", count)
        return count

    def get_product_name(self):
        return wait_for_element(self.driver, self.PRODUCT_NAME).text
