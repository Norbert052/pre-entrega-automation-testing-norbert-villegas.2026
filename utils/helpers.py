from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import os
from datetime import datetime


def wait_for_element(driver, locator, timeout=10):
    wait = WebDriverWait(driver, timeout)
    return wait.until(EC.presence_of_element_located(locator))


def wait_for_visibility(driver, locator, timeout=10):
    wait = WebDriverWait(driver, timeout)
    return wait.until(EC.visibility_of_element_located(locator))


def wait_for_clickable(driver, locator, timeout=10):
    wait = WebDriverWait(driver, timeout)
    return wait.until(EC.element_to_be_clickable(locator))


def click_element(driver, locator):
    element = wait_for_clickable(driver, locator)
    element.click()


def fill_text(driver, locator, text):
    element = wait_for_element(driver, locator)
    element.clear()
    element.send_keys(text)


def get_text(driver, locator):
    element = wait_for_visibility(driver, locator)
    return element.text


def take_screenshot(driver, test_name):
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    screenshot_dir = "reports/screenshots"
    
    if not os.path.exists(screenshot_dir):
        os.makedirs(screenshot_dir)
    
    filename = f"{screenshot_dir}/{test_name}_{timestamp}.png"
    driver.save_screenshot(filename)
    return filename
