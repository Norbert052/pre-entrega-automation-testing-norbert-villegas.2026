import pytest
from selenium.webdriver.common.by import By
from utils.driver_factory import get_driver
from utils.helpers import (
    click_element,
    fill_text,
    get_text,
    wait_for_element,
    wait_for_visibility,
    take_screenshot
)


class TestSauceDemo:
    
    @pytest.fixture(autouse=True)
    def setup_teardown(self):
        self.driver = get_driver()
        yield
        self.driver.quit()
    
    def test_login_successful(self):
        """Test successful login to SauceDemo"""
        self.driver.get("https://www.saucedemo.com")
        
        username_locator = (By.ID, "user-name")
        password_locator = (By.ID, "password")
        login_button_locator = (By.ID, "login-button")
        
        fill_text(self.driver, username_locator, "standard_user")
        fill_text(self.driver, password_locator, "secret_sauce")
        click_element(self.driver, login_button_locator)
        
        wait_for_visibility(self.driver, (By.CLASS_NAME, "title"))
        
        assert "/inventory.html" in self.driver.current_url, "URL should contain /inventory.html"
        
        page_title = get_text(self.driver, (By.CLASS_NAME, "title"))
        assert page_title == "Products", "Page title should be 'Products'"
    
    def test_catalog_elements(self):
        """Test catalog page displays products and elements"""
        self.driver.get("https://www.saucedemo.com")
        
        fill_text(self.driver, (By.ID, "user-name"), "standard_user")
        fill_text(self.driver, (By.ID, "password"), "secret_sauce")
        click_element(self.driver, (By.ID, "login-button"))
        
        wait_for_visibility(self.driver, (By.CLASS_NAME, "title"))
        
        page_title = get_text(self.driver, (By.CLASS_NAME, "title"))
        assert page_title == "Products", "Page title should be 'Products'"
        
        products = self.driver.find_elements(By.CLASS_NAME, "inventory_item")
        assert len(products) > 0, "At least one product should be visible"
        
        first_product_name = get_text(
            self.driver,
            (By.CLASS_NAME, "inventory_item_name")
        )
        assert first_product_name, "First product should have a name"
        
        first_product_price = get_text(
            self.driver,
            (By.CLASS_NAME, "inventory_item_price")
        )
        assert first_product_price, "First product should have a price"
        
        menu_button = wait_for_element(self.driver, (By.ID, "react-burger-menu-btn"))
        assert menu_button, "Menu button should be present"
        
        filter_select = wait_for_element(self.driver, (By.CLASS_NAME, "product_sort_container"))
        assert filter_select, "Filter dropdown should be present"
    
    def test_add_to_cart(self):
        """Test adding product to cart"""
        self.driver.get("https://www.saucedemo.com")
        
        fill_text(self.driver, (By.ID, "user-name"), "standard_user")
        fill_text(self.driver, (By.ID, "password"), "secret_sauce")
        click_element(self.driver, (By.ID, "login-button"))
        
        wait_for_visibility(self.driver, (By.CLASS_NAME, "title"))
        
        add_to_cart_button = self.driver.find_element(
            By.XPATH,
            "//button[contains(@class, 'btn_primary') and contains(., 'Add to cart')]"
        )
        add_to_cart_button.click()
        
        cart_badge = wait_for_element(self.driver, (By.CLASS_NAME, "shopping_cart_badge"))
        assert cart_badge.text == "1", "Cart badge should show 1 item"
        
        cart_link = self.driver.find_element(By.CLASS_NAME, "shopping_cart_link")
        cart_link.click()
        
        wait_for_visibility(self.driver, (By.CLASS_NAME, "cart_contents_container"))
        
        cart_items = self.driver.find_elements(By.CLASS_NAME, "cart_item")
        assert len(cart_items) == 1, "Cart should contain 1 item"
        
        product_in_cart = self.driver.find_element(By.CLASS_NAME, "inventory_item_name")
        assert product_in_cart, "Product should be visible in cart"
