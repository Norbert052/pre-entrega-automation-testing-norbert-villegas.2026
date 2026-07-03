from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from utils.helpers import click_element, get_text, wait_for_clickable, wait_for_element, wait_for_visibility
from utils.logger import logger


class InventoryPage:
    TITLE = (By.CLASS_NAME, "title")
    PRODUCTS = (By.CLASS_NAME, "inventory_item")
    PRODUCT_NAME = (By.CLASS_NAME, "inventory_item_name")
    PRODUCT_PRICE = (By.CLASS_NAME, "inventory_item_price")
    MENU_BUTTON = (By.ID, "react-burger-menu-btn")
    FILTER_SELECT = (By.CLASS_NAME, "product_sort_container")
    ADD_TO_CART_BUTTON = (
        By.XPATH,
        "//button[contains(@class, 'btn_primary') and contains(., 'Add to cart')]"
    )
    CART_BADGE = (By.CLASS_NAME, "shopping_cart_badge")
    CART_LINK = (By.CLASS_NAME, "shopping_cart_link")
    PRODUCT_CONTAINER = (By.CLASS_NAME, "inventory_item")

    def __init__(self, driver):
        self.driver = driver

    def wait_until_loaded(self):
        return wait_for_visibility(self.driver, self.TITLE)

    def get_title(self):
        return get_text(self.driver, self.TITLE)

    def get_products_count(self):
        return len(self.driver.find_elements(*self.PRODUCTS))

    def get_first_product_name(self):
        return get_text(self.driver, self.PRODUCT_NAME)

    def get_first_product_price(self):
        return get_text(self.driver, self.PRODUCT_PRICE)

    def is_menu_button_present(self):
        return wait_for_element(self.driver, self.MENU_BUTTON)

    def is_filter_dropdown_present(self):
        return wait_for_element(self.driver, self.FILTER_SELECT)

    def add_first_product_to_cart(self):
        click_element(self.driver, self.ADD_TO_CART_BUTTON)

    def add_product_to_cart_by_name(self, product_name):
        logger.info("Agregando producto al carrito: %s", product_name)
        for product in self.driver.find_elements(*self.PRODUCT_CONTAINER):
            name = product.find_element(*self.PRODUCT_NAME).text.strip()
            if name == product_name:
                button = product.find_element(By.XPATH, ".//button[contains(@class, 'btn_primary') and contains(normalize-space(.), 'Add to cart')]")
                self.driver.execute_script("arguments[0].scrollIntoView(true);", button)
                button.click()
                logger.info("Producto agregado al carrito: %s", product_name)
                return
        logger.error("Producto no encontrado en inventario: %s", product_name)
        raise ValueError(f"Product '{product_name}' not found in inventory")

    def get_cart_badge_count(self):
        badge = wait_for_element(self.driver, self.CART_BADGE)
        return int(badge.text)

    def open_cart(self):
        wait = WebDriverWait(self.driver, 15)
        cart_link = wait.until(EC.element_to_be_clickable(self.CART_LINK))
        cart_link.click()

        current_url = self.driver.current_url
        if "/cart.html" not in current_url:
            self.driver.execute_script("arguments[0].click();", cart_link)

        wait.until(EC.url_contains("/cart.html"))
        return self.driver.current_url
